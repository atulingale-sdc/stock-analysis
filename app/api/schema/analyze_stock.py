from pydantic import BaseModel
from app.core.schema import BaseRequestSchema


class StockRequest(BaseRequestSchema):
    query: str


class StockResponse(BaseModel):
    query: str
    summery: str | None
    graphs: list[str] | None
