from fastapi import APIRouter, Depends
from starlette.requests import Request

from fastapi_skeleton.core import security
from fastapi_skeleton.schemas.iris import (
    IrisPredictionPayload,
    IrisPredictionResult,
)
from fastapi_skeleton.ml import IrisModel

router = APIRouter()


@router.post("/iris", response_model=IrisPredictionResult, name="iris")
def post_predict(
    request: Request,
    # authenticated: bool = Depends(security.validate_request),
    block_data: IrisPredictionPayload = None,
) -> IrisPredictionResult:

    model: IrisModel = request.app.state.model["iris"]
    prediction: IrisPredictionResult = model.predict(block_data)

    return prediction
