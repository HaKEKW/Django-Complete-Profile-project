from random import randint

import joblib
import numpy
import pandas as pd
import csv


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


def find_min_max_revenue(csv_file_path):
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        revenues = [float(row['revenue']) for row in reader]

    min_revenue = min(revenues)
    max_revenue = max(revenues)

    return min_revenue, max_revenue


def find_random_value(path):
    min, max = find_min_max_revenue(path)
    random_value = randint(min, max)
    return random_value



def calculate_column_averages(path):
    column_averages = {}

    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        columns = [f'P{i}' for i in range(1, 38)]
        column_sums = {column: 0 for column in columns}
        column_counts = {column: 0 for column in columns}

        for row in reader:
            for column in columns:
                if row[column] != '':
                    column_sums[column] += float(row[column])
                    column_counts[column] += 1

        for column in columns:
            if column_counts[column] > 0:
                column_averages[column] = round(column_sums[column] / column_counts[column], 2)
            else:
                column_averages[column] = None

    return column_averages


