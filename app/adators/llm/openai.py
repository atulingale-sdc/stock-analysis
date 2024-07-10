import inject
import json
from datetime import datetime
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.chat_history import (
    BaseChatMessageHistory,
    InMemoryChatMessageHistory,
)
from langchain_core.messages import ChatMessage
from langchain_core.runnables.history import RunnableWithMessageHistory
from app.adators.llm.base import LLMAdaptor
from app.settings import Settings

stock_question_history = []
chat_history = []


class OpenAIAdaptor(LLMAdaptor):

    @inject.autoparams('conf')
    def __init__(self, conf: Settings):
        if not conf.openai_api_key:
            raise RuntimeError("OpenAI API Key is not configured.")

        self.api_key = conf.openai_api_key
        # self.client = OpenAI(api_key=str(conf.openai_api_key))
        self.default_model = 'gpt-3.5-turbo-instruct'

    async def extract_tokens(self, text, model: str | None = None) -> None | dict:
        # Define the prompt
        template = """
        Use the following user question history to extract the named entities:

        {history}

        Consider current date '{current_date}' in YYYY-MM-DD format.
        Extract named entities with corresponding stock symbol considering Question history from the text:

        {input}

        {format_instructions}
         Convert the period relative time expression to an actual date range."
         Provide the output in format: start_date, end_date, period, organisation and stock_symbol 
         where dates are in YYYY-MM-DD format.
        """

        # model_name="gpt-3.5-turbo-instruct"
        llm = OpenAI(openai_api_key=self.api_key, temperature=0.3)
        json_output = JsonOutputParser()

        prompt = PromptTemplate(
            template=template,
            input_variables=["input", "current_date", "history"],
            partial_variables={"format_instructions": json_output.get_format_instructions()},
        )

        chain = prompt | llm | json_output
        message = ChatMessage(content=text, role="User")
        resp = chain.invoke(
            {
                "input": message,
                "current_date": datetime.now().date(),
                "history": stock_question_history
            }
        )
        stock_question_history.append(message)
        return resp

    async def create_summery(self, data: str, period: str, model: str | None = None,) -> str:
        """
        Create summery for the given data

        :param data:
        :param period:
        :param model:
        :return:
        """

        summery_prompt = """
        You are a best stock market analyzer.
        Generate a summary of the following stock market data for period {period}:
        
        {context_data}

        Summary:
        """

        chat_prompt = PromptTemplate(input_variables=["context_data", "period"], template=summery_prompt)

        # Prepare the prompt for the GPT model
        llm = OpenAI(openai_api_key=self.api_key, temperature=0.7)
        chain = chat_prompt | llm

        response = chain.invoke(
            {"context_data": data, "period": period},
        )
        return response

    async def check_current_question_is_for_stock_market(self, text: str, model: str = None) -> bool:
        template = """
        You are a shock market adviser.
        Use the following user question history for context:
        
        {history}
        
        Using user's question history context categorize following text is about stock market:
        {input}
        
        Convert the output in boolean.
        """

        # model_name="gpt-3.5-turbo-instruct"
        llm = OpenAI(openai_api_key=self.api_key, temperature=0.3)

        prompt = PromptTemplate(
            template=template,
            input_variables=["input", "history"],
        )

        chain = prompt | llm

        message = ChatMessage(content=text, role="User")
        resp = chain.invoke(
            {
                "input": message,
                "history": chat_history
            }
        )
        chat_history.append(message)

        return "true" in str(resp).lower()

