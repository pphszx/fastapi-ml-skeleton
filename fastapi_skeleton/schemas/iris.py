from typing import List
from pydantic import BaseModel


class IrisPredictionPayload(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


class IrisPredictionResult(BaseModel):
    id_of_iris: int
    types_of_iris: str


def payload_to_list(IPP: IrisPredictionPayload) -> List:
    return [
        IPP.sepal_length,
        IPP.sepal_width,
        IPP.petal_length,
        IPP.petal_width,
    ]
