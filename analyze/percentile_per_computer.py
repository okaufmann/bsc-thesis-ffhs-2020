import pandas as pd
import os.path as path
import numpy as np

cwd = path.dirname(__file__)

# CPU Measurements
measurementColumn = 'Measurement_Value'

# RAM Measurements
# measurementColumn = 'Allocated_Bytes'

def percentiles(data, name):
    minimum = np.percentile(data, 0)
    lowerQuartile = np.percentile(data, 25)
    median = np.percentile(data, 50)
    higherQuartile = np.percentile(data, 75)
    maximum = np.percentile(data, 100)
    stdDev = np.std(data)
    stdErr = np.std(data, ddof=1) / np.sqrt(np.size(data))
    interquartileRange = higherQuartile - lowerQuartile

    print(f"{name}, sample size: {len(data)})")
    print("0th percentile: " + str(minimum))
    print("25th percentile: " + str(lowerQuartile))
    print("50th percentile (media): " + str(median))
    print("75th percentile: " + str(higherQuartile))
    print("100th percentile: " + str(maximum))
    print("interquartile range: " + str(interquartileRange))
    print("standard dev: " + str(stdDev))
    print("standard err: " + str(stdErr))
    print('-----------------------------------------')


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

for method in results:
    for size in results[method]:
        for computer in results[method][size]:
            name = f"{computer}-{method} ({size})"
            data = results[method][size][computer][dataType]

            flatData = np.hstack(data)

            percentiles(flatData, name)
