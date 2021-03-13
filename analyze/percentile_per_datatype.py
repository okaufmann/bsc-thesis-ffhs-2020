import pandas as pd
import os.path as path
import numpy as np
from tabulate import tabulate

cwd = path.dirname(__file__)


# CPU Measurements
# outputFolder = "cpu"
# measurementColumn = 'Measurement_Value'

# RAM Measurements
outputFolder = "ram"
measurementColumn = 'Allocated_Bytes'

csvPath = path.join(cwd, '../results/all-data.csv')

df = pd.read_csv(csvPath)

data = df.groupby(['Target_Type', 'Target_Method', 'Params'])

results = {}
for experiment, values in data:
    method = experiment[0].replace('Experiments', '')
    datatype = experiment[1]
    size = experiment[2]

    experimentValues = [
        value for value in values[measurementColumn]]
    if not method in results:
        results[method] = {}

    if not datatype in results[method]:
        results[method][datatype] = {}

    results[method][datatype][size] = experimentValues

    # print(f"{method}-{datatype}-{size} {len(experimentValues)}")

df = pd.DataFrame(columns=['Name', '0th percentile', '25th percentile',
                           '50th percentile (media)', '75th percentile', '100th percentile', 'interquartile range', 'standard deviation', 'standard error'])
for method in results:
    for datatype in results[method]:
        for size in results[method][datatype]:
            data = results[method][datatype][size]
            name = f"{method}-{datatype} ({size})"
            print(f"{name}, count: {len(data)}")

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
df.to_html(path.join(cwd, f'../results/statistics/{outputFolder}-percentile_per_datatype.html'))
