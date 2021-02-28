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

    interquartileRange = higherQuartile - lowerQuartile

    print(name + " 0th percentile: " + str(minimum))
    print(name + " 25th percentile: " + str(lowerQuartile))
    print(name + " 50th percentile (media): " + str(median))
    print(name + " 75th percentile: " + str(higherQuartile))
    print(name + " 100th percentile: " + str(maximum))
    print(name + " interquartile range: " + str(interquartileRange))
    print(name + " std dev: " + str(stdDev))
    print('-----------------------------------------')

csvPath = path.join(cwd, '../results/all-data.csv')

df = pd.read_csv(csvPath)

data = df.groupby(['Target_Type', 'Target_Method', 'Params', 'Result_Set'])

results = {}
for experiment, values in data:
    experimentName = experiment[0].replace('Experiments', '')
    name = f"{experiment[3]}-{experimentName}-{experiment[2]}-{experiment[1]}"
    experimentValues = [
            value for value in values["Measurement_Value"]]
    if not experimentName in results:
        results[experimentName] = {}

    if not experiment[2] in results[experimentName]:
        results[experimentName][experiment[2]] = {}

    if not experiment[1] in results[experimentName][experiment[2]]:
        results[experimentName][experiment[2]][experiment[1]] = {}

    # print(name)
    # print(len(experimentValues))
    results[experimentName][experiment[2]][experiment[1]][experiment[3]] = experimentValues

print(results["Reverse"]["Size=10"]["Array"]["do-testserver"])
percentiles(results["Reverse"]["Size=10"]["Array"]["do-testserver"], "do-testserver")
exit()
for method in results:
    for size in results[method]:

        name = f"{method} ({size})"
        data = [results[method][size][dataType] for dataType in results[method][size]]

        flattData = np.hstack(data)

        percentiles()