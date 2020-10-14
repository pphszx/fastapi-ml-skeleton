from typing import List

import numpy as np
from loguru import logger

from fastapi_skeleton.model.base import BaseModel
from fastapi_skeleton.schemas.iris import (
    IrisPredictionPayload,
    payload_to_list,
    IrisPredictionResult,
)


class IrisModel(BaseModel):

    dct_iris = {0: "Setosa", 1: "Versicolour", 2: "Virginica"}

    def _pre_process(self, payload: IrisPredictionPayload) -> List:
        logger.debug("Pre-processing payload.")
        result = np.asarray(payload_to_list(payload)).reshape(1, -1)
        return result

    def _post_process(self, prediction: np.ndarray) -> IrisPredictionResult:
        logger.debug("Post-processing prediction.")
        result = prediction.tolist()[0]

        ipp = IrisPredictionResult(
            id_of_iris=result, types_of_iris=self.dct_iris[result]
        )
        return ipp
