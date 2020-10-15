from typing import List

from loguru import logger

from fastapi_skeleton.ml.base import BaseModel
from fastapi_skeleton.schemas.haier import (
    HaierPredictionPayload,
    payload_to_list,
    HaierPredictionResult,
)


class HaierModel(BaseModel):

    def _pre_process(self, payload: HaierPredictionPayload) -> List:
        logger.debug("Pre-processing payload.")
        result = [payload_to_list(payload)]
        return result

    def _post_process(self, prediction: List) -> HaierPredictionResult:
        logger.debug("Post-processing prediction.")
        logger.debug(prediction)
        result = prediction.tolist()

        ipp = HaierPredictionResult(
            good_prob=result[0][0], bad_prob=result[0][1]
        )
        return ipp

    def _predict(self, features):
        logger.debug("Predicting.")
        prediction_result = self.model.predict_proba(features)
        return prediction_result
