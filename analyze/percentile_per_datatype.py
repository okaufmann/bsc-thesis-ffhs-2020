import pandas as pd
import os.path as path
import numpy as np

cwd = path.dirname(__file__)


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

data = df.groupby(['Target_Type', 'Target_Method', 'Params'])

results = {}
for experiment, values in data:
    method = experiment[0].replace('Experiments', '')
    datatype = experiment[1]
    size = experiment[2]

    name = f"{method}-{datatype}-{size}"
    experimentValues = [
        value for value in values["Measurement_Value"]]
    if not method in results:
        results[method] = {}

    if not datatype in results[method]:
        results[method][datatype] = {}

    results[method][datatype][size] = experimentValues


for method in results:
    for datatype in results[method]:
        for size in results[method][datatype]:
            name = f"{method}-{datatype} ({size})"
            print(name)
            data = [results[method][datatype][size]
                    for dataType in results[method][datatype][size]]

            flatData = np.hstack(data)

            percentiles(flatData, name)
