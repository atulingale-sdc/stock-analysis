from pathlib import Path
from app.api.schema import analyze_stock
from app.core.router import APIRouter
from fastapi import Depends
from fastapi.responses import FileResponse
from app.core.deps import get_authorised_user
from app.service.stock_analysis import StockAnalysisService

router = APIRouter(tags=["Stock Analysis"])


@router.post("/analyze", response_model=analyze_stock.StockResponse)
async def analyse_query(
        req: analyze_stock.StockRequest,
        current_user_id: str = Depends(get_authorised_user)
):
    """Give analysis of stock."""
    service = StockAnalysisService()
    summery, image = await service.analyse_user_query(user_inp=req.query)
    return analyze_stock.StockResponse(
        query=req.query, summery=summery, graphs=[image]
    )


@router.get("/images/{image}")
async def get_image(image: str):
    """Show image."""
    image_path = Path(f"images/{image}")
    if not image_path.is_file():
        return {"error": "Image not found on the server"}
    return FileResponse(image_path)
