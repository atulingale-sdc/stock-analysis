from abc import abstractmethod, ABC


class LLMAdaptor(ABC):

    @abstractmethod
    async def extract_tokens(self, user_inp: str) -> dict:
        raise NotImplemented

    @abstractmethod
    async def create_summery(self, data: str, period: str) -> str:
        raise NotImplemented
