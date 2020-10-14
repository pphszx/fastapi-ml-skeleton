from fastapi import APIRouter, Depends
from starlette.requests import Request

from fastapi_skeleton.core import security
from fastapi_skeleton.schemas.houseprice import (
    HousePredictionPayload,
    HousePredictionResult,
)
from fastapi_skeleton.model import HousePriceModel

router = APIRouter()


@router.post(
    "/houseprice", response_model=HousePredictionResult, name="houseprice"
)
def post_predict(
    request: Request,
    # authenticated: bool = Depends(security.validate_request),
    block_data: HousePredictionPayload = None,
) -> HousePredictionResult:

    model: HousePriceModel = request.app.state.model["houseprice"]
    prediction: HousePredictionResult = model.predict(block_data)

    return prediction
