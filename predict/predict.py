from sklearn.datasets import load_iris

import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
import pickle
import os


def predict():
	iris = load_iris()
	filename='/app/output/model.pkl'
	model = pickle.load(open(filename, 'rb'))
    	#features = np.array(data['features']).reshape(1, -1)

	prediction = model.predict(iris.data[0].reshape(1,-1))[0]

	response = {'prediction': prediction}
	print(response)
	return response


if __name__ == '__main__':
	predict()
