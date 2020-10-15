from fastapi import APIRouter, Depends
from starlette.requests import Request

from fastapi_skeleton.core import security
from fastapi_skeleton.schemas.haier import (
    HaierPredictionPayload,
    HaierPredictionResult,
)
from fastapi_skeleton.ml import HaierModel

router = APIRouter()


@router.post("/haier", response_model=HaierPredictionResult, name="haier")
def post_predict(
    request: Request,
    # authenticated: bool = Depends(security.validate_request),
    block_data: HaierPredictionPayload = None,
) -> HaierPredictionResult:
    """
    海尔模型
    """
    model: HaierModel = request.app.state.model["haier"]
    prediction: HaierPredictionResult = model.predict(block_data)

    return prediction
