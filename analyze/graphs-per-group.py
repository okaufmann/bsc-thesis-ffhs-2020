import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon
import pandas as pd
import os.path as path
import os
import glob
from matplotlib import style

style.use('ggplot')

cwd = path.dirname(__file__)

# CPU Measurements
outputFolder = 'cpu'
measurementColumn = 'Measurement_Value'
yLabel = "Time, ns"

# RAM Measurements
# outputFolder = 'ram'
# measurementColumn = 'Allocated_Bytes'
# yLabel = "Allocated, bytes"

def plotBoxplot(title, data, labels, filename):
    fig, axs = plt.subplots()

    axs.set_title(title)
    axs.boxplot(data)
    axs.set_xticklabels(labels)
    axs.set_ylabel(yLabel)

    filename = path.join(
        cwd, f'../results/graphs/{outputFolder}/{filename}')
    plt.savefig(filename, dpi=200)
    plt.close()

def main():
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
            labels = [dataType for dataType in results[method][size]]
            data = [results[method][size][dataType] for dataType in results[method][size]]

            plotBoxplot(f"{method} ({size})", data, labels, f"{method}-{size}-boxplot.png")

            memoryOnlyLabels = labels[1:]
            memoryOnlyData = data[1:]

            plotBoxplot(f"{method} ({size})", memoryOnlyData, memoryOnlyLabels, f"{method}-{size}-memory-boxplot.png")

main()
