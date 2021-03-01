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

def prepare():

    # delete generated graphs
    files = glob.glob(
        path.join(cwd, f"../results/graphs/{outputFolder}/*.png"), recursive=True)
    [os.remove(f) for f in files]


def createSingleBoxplot(data, name, filename):
    plt.figure()
    plt.boxplot(data)
    plt.title(name)
    plt.ylabel(yLabel)
    plt.xticks([])
    plt.subplots_adjust(bottom=.2, left=.2)

    filename = path.join(
        cwd, f'../results/graphs/{outputFolder}/single/{filename}')
    plt.savefig(filename, dpi=200)
    plt.close()


def createSingleHistogram(data, name, filename):
    plt.figure()
    plt.hist(data, bins=10)
    plt.title(name)
    plt.subplots_adjust(bottom=.2, left=.2)
    plt.xlabel(yLabel)

    filename = path.join(
        cwd, f'../results/graphs/{outputFolder}/single/{filename}')
    plt.savefig(filename, dpi=200)
    plt.close()


def createGraph(csvPath):
    global allDataHeadersWritten

    results = pd.read_csv(csvPath)

    resultSet = path.basename(path.dirname(
        path.split(path.abspath(csvPath))[0]))

    data = results.groupby(['Target_Type', 'Target_Method', 'Params'])

    allData = []
    labels = []
    for experiment, values in data:
        experimentName = experiment[0].replace('Experiments', '')
        name = f"{experimentName}-{experiment[1]}-{experiment[2]}"
        experimentValues = [
            value for value in values[measurementColumn]]
        allData.append(experimentValues)
        labels.append(f"{experiment[1]} ({experiment[2]})")

        filename = f"{resultSet}-{name}"
        createSingleBoxplot(experimentValues, name, f"{filename}-boxplot.png")
        createSingleHistogram(experimentValues, name, f"{filename}-hist.png")

    fig, axs = plt.subplots(figsize=(20, 15))

    csvFilename = path.basename(csvPath).replace("-measurements.csv", "")
    axs.set_title(f"{resultSet}-{csvFilename}")
    axs.boxplot(allData)
    axs.set_xticklabels(labels)
    axs.set_ylabel(yLabel)

    plt.subplots_adjust(bottom=.1, left=.1)

    filename = path.join(
        cwd, f'../results/graphs/{outputFolder}/{resultSet}-{csvFilename}.png')
    plt.savefig(filename, dpi=200)
    # plt.show()
    plt.close()


prepare()

pattern = path.join(cwd, '../results/all-data.csv')

createGraph(path.join(cwd, '../results/all-data.csv'))
