from pathlib import Path

from sklearn import svm
from sklearn import datasets


BASE_DIR = Path(__file__).resolve(strict=True).parent
clf = svm.SVC()
iris = datasets.load_iris()
X, y = iris.data, iris.target
clf.fit(X, y)


import joblib


file_name = Path(BASE_DIR).joinpath("model.joblib")
joblib.dump(clf, file_name)

model = joblib.load(file_name)
# X[0:1]: array([[5.1, 3.5, 1.4, 0.2]])
print(model.predict(X[0:1]))
