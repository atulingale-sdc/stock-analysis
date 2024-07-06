import inject
import json
from datetime import datetime
from openai import OpenAI
from app.adators.llm.base import LLMAdaptor
from app.settings import Settings


class OpenAIAdaptor(LLMAdaptor):

    @inject.autoparams('conf')
    def __init__(self, conf: Settings):
        if not conf.openai_api_key:
            raise RuntimeError("OpenAI API Key is not configured.")

        self.client = OpenAI(api_key=conf.openai_api_key)
        self.default_model = 'gpt-3.5-turbo-instruct'

    @staticmethod
    def _parse_json(output: str):
        output.replace('Output:', '')
        try:
            return json.loads(output)
        except Exception as e:
            raise e

    async def extract_tokens(self, text, model: str | None = None) -> None | dict:
        # Define the prompt
        prompt = (
            f"Extract named entities with corresponding stock symbol from the following text:"
            f"\n\n{text}\n\n Provide output in JSON format with categories: "
            f"Organization, Symbol, Period. "
            f"Convert the period relative time expression to an actual date range. Consider current date '{datetime.now().date()}'"
            f"Provide the output in format: 'start_date' and 'end_date' where dates are in YYYY-MM-DD format, "
            # f"along with extracted Organization, Period."
        )

        # Call the OpenAI API
        response = self.client.completions.create(
            model=model or self.default_model,
            prompt=prompt,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.3
        )

        # Parse the response
        output = response.choices[0].text.strip()
        return self._parse_json(output)

    async def create_summery(self, data: str, period: str, model: str | None = None,) -> str:
        """
        Create summery for the given data

        :param data:
        :param period:
        :param model:
        :return:
        """
        # Prepare the prompt for the GPT model
        prompt = f"Generate a summary of the following stock data for period {period}:\n\n{data}\n\nSummary:"

        response = self.client.completions.create(
            model=model or self.default_model,
            prompt=prompt,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.5,
        )

        summary = response.choices[0].text.strip()
        return summary
