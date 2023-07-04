import joblib
import numpy
import pandas as pd


def make_prediction(form_data: dict):
    # data = pd.DataFrame(
    #     {'OpenDays': [numpy.int64(int(form_data['open_days']))],
    #      'Big Cities': form_data['big_cities'], 'Other': not form_data['big_cities'],
    #      'P2': form_data['P2'], 'P8': form_data['P8'], 'P22': form_data['P22'],
    #      'P24': form_data['P24'], 'P28': form_data['P28'], 'P26': form_data['P26']})
    data = pd.DataFrame(
        {'OpenDays': [numpy.int64(2)],
         'Big Cities': True, 'Other': False,
         'P2': 1, 'P8': 2, 'P22': 1,
         'P24': 1, 'P28': 2, 'P26': 3})
    model = joblib.load("../random_forest.joblib")
    predicted_results = model.predict(data)
    print(predicted_results)

data = pd.DataFrame(
        {'OpenDays': [numpy.int64(2)],
         'Big Cities': True, 'Other': False,
         'P2': 1, 'P8': 2, 'P22': 1,
         'P24': 1, 'P28': 2, 'P26': 3})
model = joblib.load("../random_forest.joblib")
predicted_results = model.predict(data)
print(predicted_results)
