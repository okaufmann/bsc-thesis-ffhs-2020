import pandas as pd
import os.path as path
from scipy.stats import levene

cwd = path.dirname(__file__)

csvPath = path.join(cwd, '../results/all-data.csv')

df = pd.read_csv(csvPath)

data = df.groupby(['Target_Type', 'Target_Method', 'Params'])

results = {}
for experiment, values in data:
    experimentName = experiment[0].replace('Experiments', '')
    name = f"{experimentName}-{experiment[2]}-{experiment[1]}"
    experimentValues = [
            value for value in values["Measurement_Value"]]
    if not experimentName in results:
        results[experimentName] = {}

    if not experiment[2] in results[experimentName]:
        results[experimentName][experiment[2]] = {}

    # print(name)
    # print(len(experimentValues))
    results[experimentName][experiment[2]][experiment[1]] = experimentValues

for method in results:
    print(method)
    for size in results[method]:
        data = [results[method][size][dataType] for dataType in results[method][size]]
        stat, p = levene(*data)
        nullHypothesisRejected = p <= 0.05
        print(f"{method}, {size}: p=", p, ", reject null hypothesis:", nullHypothesisRejected)