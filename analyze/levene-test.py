import pandas as pd
import os.path as path
from scipy.stats import levene
import numpy as np

cwd = path.dirname(__file__)

# CPU Measurements
measurementColumn = 'Measurement_Value'

# RAM Measurements
# measurementColumn = 'Allocated_Bytes'

csvPath = path.join(cwd, '../results/all-data.csv')

df = pd.read_csv(csvPath)

data = df.groupby(['Target_Type', 'Target_Method', 'Params'])

results = {}
for experiment, values in data:
    experimentName = experiment[0].replace('Experiments', '')
    name = f"{experimentName}-{experiment[2]}-{experiment[1]}"
    experimentValues = [
        value for value in values[measurementColumn]]
    if not experimentName in results:
        results[experimentName] = {}

    if not experiment[2] in results[experimentName]:
        results[experimentName][experiment[2]] = {}

    results[experimentName][experiment[2]][experiment[1]] = experimentValues

for method in results:
    for size in results[method]:
        data = [results[method][size][dataType]
                for dataType in results[method][size]]
        stat, p = levene(*data)
        nullHypothesisRejected = (p <= 0.05)
        print(f"{method}, {size}: p=", p,
              ", reject null hypothesis:", nullHypothesisRejected)

        data = [results[method][size][dataType]
                for dataType in results[method][size] if dataType != 'Array']
        stat, p = levene(*data)
        nullHypothesisRejected = (p <= 0.05)
        print(f"{method}, {size} (Span vs. Memory): p=", p,
              ", reject null hypothesis:", nullHypothesisRejected)
