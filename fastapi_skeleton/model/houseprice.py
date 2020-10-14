from typing import List

import numpy as np
from loguru import logger

from fastapi_skeleton.model.base import BaseModel
from fastapi_skeleton.schemas.houseprice import (
    HousePredictionPayload,
    payload_to_list,
    HousePredictionResult,
)


class HousePriceModel(BaseModel):

    RESULT_UNIT_FACTOR = 100000

    def _pre_process(self, payload: HousePredictionPayload) -> List:
        logger.debug("Pre-processing payload.")
        result = np.asarray(payload_to_list(payload)).reshape(1, -1)
        return result

    def _post_process(self, prediction: np.ndarray) -> HousePredictionResult:
        logger.debug("Post-processing prediction.")
        result = prediction.tolist()
        human_readable_unit = result[0] * self.RESULT_UNIT_FACTOR
        hpp = HousePredictionResult(median_house_value=human_readable_unit)
        return hpp
