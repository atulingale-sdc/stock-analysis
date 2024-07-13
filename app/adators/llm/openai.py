from typing import List, Any
from logging import getLogger

import inject
import json
from datetime import datetime

from langchain_core.outputs import Generation
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from langchain_core.chat_history import (
    BaseChatMessageHistory,
    InMemoryChatMessageHistory,
)
from langchain_core.utils.json import (
    parse_and_check_json_markdown,
    parse_json_markdown,
    parse_partial_json,
)
import json
from json import JSONDecodeError

from langchain_core.messages import ChatMessage
from langchain_core.runnables.history import RunnableWithMessageHistory
from app.adators.llm.base import LLMAdaptor
from app.settings import Settings

stock_question_history_hash = {}
chat_history_hash = {}


logger = getLogger(__name__)


class CustomJsonOutputParser(JsonOutputParser):
    """Custom JSON Parser to handle some unhandled responses."""

    def parse_result(self, result: List[Generation], *, partial: bool = False) -> Any:
        text = result[0].text
        text = text.strip()
        # Sanitize output
        text = text.replace("Output:", "")

        result[0].text = text
        try:
            return super().parse_result(result=result, partial=partial)
        except (OutputParserException, json.JSONDecodeError) as e:
            # If response is not able to converted in to JSON then raise the exception
            logger.error(f"Unable to parse response to with error {e} json: {text}", exc_info=True)
            return {}


class OpenAIAdaptor(LLMAdaptor):

    @inject.autoparams('conf')
    def __init__(self, conf: Settings):
        if not conf.openai_api_key:
            raise RuntimeError("OpenAI API Key is not configured.")

        self.api_key = conf.openai_api_key
        # self.client = OpenAI(api_key=str(conf.openai_api_key))
        self.default_model = 'gpt-3.5-turbo-instruct'
        self.stock_question_history = []
        self.chat_history = []

    async def extract_tokens(self, text, model: str | None = None) -> None | dict:
        # Define the prompt
        template = """
        You are a shock market adviser.
        Current date is '{current_date}' in YYYY-MM-DD format.
        User's question history is as follow:
        <context>
        {history}
        </context>

        User's current question is: 

        {input}

        Extract company name with corresponding stock symbol, relative time expression or month or year to check stock performance from current question using question history.

        Convert the period relative time expression to an actual date range.
        Provide the output in format: start_date, end_date, period, organisation and stock_symbol 
        where dates are in YYYY-MM-DD format.

        {format_instructions}

        """

        # model_name="gpt-3.5-turbo-instruct"
        llm = OpenAI(openai_api_key=self.api_key, temperature=0)
        json_output = CustomJsonOutputParser()

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
                "history": self.stock_question_history
            }
        )

        # Manage here chat history, it should not grow above 5 last messages
        # And it should not contain the duplicate messages
        # This is the basic logic to achieve the goal, more complex and robust logic is required on production
        hs = str(hash(message.content))
        if not stock_question_history_hash.get(hs):
            self.stock_question_history.append(message)
            # mark the position of message
            stock_question_history_hash[hs] = True
        if len(self.stock_question_history) > 2:
            for msg in self.stock_question_history[0:2]:
                # Delete the hashes
                hs = str(hash(msg.content))
                try:
                    del stock_question_history_hash[hs]
                except KeyError:
                    # Do not want to raise exception if key is not present
                    pass

            # trim history and only last 5 messages will be looked
            self.stock_question_history = self.stock_question_history[5:]

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
                "history": self.chat_history
            }
        )

        # Manage here chat history, it should not grow above 5 last messages
        # And it should not contain the duplicate messages
        # This is the basic logic to achieve the goal, more complex and robust logic is required on production
        hs = str(hash(message.content))
        if not stock_question_history_hash.get(hs):
            self.chat_history.append(message)
            # mark the position of message
            stock_question_history_hash[hs] = True
        if len(self.chat_history) > 5:
            for msg in self.chat_history[0:5]:
                # Delete the hashes
                hs = str(hash(msg.content))
                try:
                    del chat_history_hash[hs]
                except KeyError:
                    # Do not want to raise exception if key is not present
                    pass
            # trim history and only last 5 messages will be looked
            self.chat_history = self.chat_history[5:]
        return "true" in str(resp).lower()
