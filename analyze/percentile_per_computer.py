import pandas as pd
import os.path as path
import numpy as np
from tabulate import tabulate

cwd = path.dirname(__file__)


# CPU Measurements
outputFolder = "cpu"
measurementColumn = 'Measurement_Value'

# RAM Measurements
# outputFolder = "ram"
# measurementColumn = 'Allocated_Bytes'

csvPath = path.join(cwd, '../results/all-data.csv')

df = pd.read_csv(csvPath)

data = df.groupby(['Target_Type', 'Target_Method', 'Params', 'Result_Set'])

results = {}
for experiment, values in data:
    method = experiment[0].replace('Experiments', '')
    name = f"{experiment[3]}-{method}-{experiment[2]}-{experiment[1]}"
    experimentValues = [
        value for value in values[measurementColumn]]
    if not method in results:
        results[method] = {}

    if not experiment[2] in results[method]:
        results[method][experiment[2]] = {}

    if not experiment[3] in results[method][experiment[2]]:
        results[method][experiment[2]][experiment[3]] = {}

    results[method][experiment[2]][experiment[3]][experiment[1]] = experimentValues

df = pd.DataFrame(columns=['Name', '0th percentile', '25th percentile',
                           '50th percentile (media)', '75th percentile', '100th percentile', 'interquartile range', 'standard deviation', 'standard error'])
for method in results:
    for size in results[method]:
        for computer in results[method][size]:
            name = f"{computer}-{method} ({size})"
            data = [results[method][size][computer][dataType]
                    for dataType in results[method][size][computer]]

            for dataTypeData in data:
                print(f"{name}, count: {len(dataTypeData)}")

            data = np.hstack(data)

            minPercentile = np.percentile(data, 0)
            lowerQuartile = np.percentile(data, 25)
            median = np.percentile(data, 50)
            higherQuartile = np.percentile(data, 75)
            maxPercentile = np.percentile(data, 100)
            stdDev = np.std(data)
            stdErr = np.std(data, ddof=1) / np.sqrt(np.size(data))
            interquartileRange = higherQuartile - lowerQuartile

            row = [name, minPercentile, lowerQuartile, median, higherQuartile, maxPercentile,interquartileRange, stdDev, stdErr]
            append = {}
            for i in range(len(df.columns)):
                append[df.columns[i]] = row[i]
            df = df.append(append, ignore_index=True)

print(df.to_markdown())
df.to_html(path.join(cwd, f'../results/statistics/{outputFolder}-percentile_per_computer.html'))
