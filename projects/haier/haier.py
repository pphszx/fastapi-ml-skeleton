# -*- coding: utf-8 -*-
import joblib

file_name = Path(BASE_DIR).joinpath("model.joblib")

model = joblib.load(r'D:\git\ml\projects\haier\model.joblib')

X = [[1,0,20000,0,0,590,1,0,12,14,1,716,18]]

print(model.predict_proba(X))
