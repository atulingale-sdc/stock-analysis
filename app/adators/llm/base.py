from abc import abstractmethod, ABC


class LLMAdaptor(ABC):

    @abstractmethod
    async def extract_tokens(self, user_inp: str) -> dict:
        raise NotImplemented

    @abstractmethod
    async def create_summery(self, data: str, period: str) -> str:
        raise NotImplemented

    @abstractmethod
    async def check_current_question_is_for_stock_market(self, text: str, model: str = None) -> bool:
        raise NotImplemented
