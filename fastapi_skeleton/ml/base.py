import joblib
from loguru import logger

from fastapi_skeleton.core.messages import NO_VALID_PAYLOAD


class BaseModel(object):
    def __init__(self, path):
        self.path = path
        self._load_local_model()

    def _load_local_model(self):
        self.model = joblib.load(self.path)

    def _pre_process(self, payload):
        return payload

    def _post_process(self, prediction):
        return prediction

    def _predict(self, features):
        logger.debug("Predicting.")
        prediction_result = self.model.predict(features)
        return prediction_result

    def predict(self, payload):
        if payload is None:
            raise ValueError(NO_VALID_PAYLOAD.format(payload))

        pre_processed_payload = self._pre_process(payload)
        prediction = self._predict(pre_processed_payload)
        logger.info(prediction)
        post_processed_result = self._post_process(prediction)

        return post_processed_result
