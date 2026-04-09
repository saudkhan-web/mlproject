import os 
import sys
import pickle

import numpy as np
import pandas as pd
import pickle
from sklearn.metrics import r2_score

from src.exception import CustomException



def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)


    

def evaluat_models(x_train, y_train, x_test, y_test, models):
    try:
        report = {}
        for i in range(len(models)):
            model = list(models.values())[i]
            model.fit(x_train, y_train)  # Train model
            y_test_pred = model.predict(x_test)  # Predict Testing data
            train_model_score = r2_score(y_train, model.predict(x_train))  # Evaluate model
            test_model_score = r2_score(y_test, y_test_pred)  # Evaluate model
            report[list(models.keys())[i]] = test_model_score  # Save model score in report

    except Exception as e:
        raise CustomException(e, sys)