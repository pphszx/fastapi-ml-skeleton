# -*- coding: utf-8 -*-
from pathlib import Path

import joblib


BASE_DIR = Path(__file__).resolve(strict=True).parent
file_name = Path(BASE_DIR).joinpath("model.joblib")

model = joblib.load(file_name)

X = [[1, 0, 20000, 0, 0, 590, 1, 0, 12, 14, 1, 716, 18]]

print(model.predict_proba(X))
