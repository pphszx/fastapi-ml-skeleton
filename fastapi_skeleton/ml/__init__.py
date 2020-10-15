from fastapi_skeleton.ml.houseprice import HousePriceModel
from fastapi_skeleton.ml.iris import IrisModel
from fastapi_skeleton.ml.haier import HaierModel

dct_model = {
    "houseprice": HousePriceModel,
    "iris": IrisModel,
    "haier": HaierModel,
}
