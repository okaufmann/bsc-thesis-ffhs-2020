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

allDataFile = path.join(cwd, f'../results/all-data.csv')
allDataHeadersWritten = False


def prepare():

    # clear all data
    allData = path.join(cwd, f'../results/all-data.csv')
    if path.exists(allData):
        os.remove(allData)

    # delete generated graphs
    files = glob.glob(
        path.join(cwd, '../results/graphs/*.png'), recursive=True)
    [os.remove(f) for f in files]


def appendDataFrames(content):
    file = open(allDataFile, 'a')
    file.write(content)
    file.close()


def createSingleBoxplot(data, name, filename):
    plt.figure()
    plt.boxplot(data)
    plt.title(name)
    plt.ylabel("Time, ms")
    plt.xticks([])
    plt.subplots_adjust(bottom=.2, left=.2)
    # plt.subplots_adjust(left=0.08, right=0.98, bottom=0.05, top=0.9,
    #     hspace=1.4, wspace=5.3)

    filename = path.join(cwd, f'../results/graphs/{filename}')
    plt.savefig(filename, dpi=200)
    # plt.show()
    plt.close()


def createSingleHistogram(data, name, filename):
    plt.figure()
    plt.hist(data, bins=10)
    plt.title(name)
    # plt.ylabel("Time, ms")
    # plt.xticks([])
    plt.subplots_adjust(bottom=.2, left=.2)
    # plt.subplots_adjust(left=0.08, right=0.98, bottom=0.05, top=0.9,
    #     hspace=1.4, wspace=5.3)

    filename = path.join(cwd, f'../results/graphs/{filename}')
    plt.savefig(filename, dpi=200)
    # plt.show()
    plt.close()


def createGraph(csvPath):
    global allDataHeadersWritten
    # path.join(cwd, "../results/do-testserver-results/results/Thesis2020.Experiments.ReverseExperiments-measurements.csv"
    df = pd.read_csv(csvPath,
                     usecols=["Target", "Target_Type", "Target_Method", "Params", "Measurement_IterationStage",
                              "Measurement_Value", "Measurement_Nanoseconds"],
                     )

    resultSet = path.basename(path.dirname(
        path.split(path.abspath(csvPath))[0]))

    results = df.query('Measurement_IterationStage == "Result"')
    results["Result_Set"] = resultSet

    writeHeaders = not allDataHeadersWritten
    appendDataFrames(results.to_csv(
        index=False, header=writeHeaders))
    allDataHeadersWritten = True
    data = results.groupby(['Target_Type', 'Target_Method', 'Params'])

    # plt.boxplot(experimentValues)
    # plt.title(f"{experiment[0]}{experiment[1]}")

    allData = []
    labels = []
    for experiment, values in data:
        experimentName = experiment[0].replace('Experiments', '')
        name = f"{experimentName}-{experiment[1]}-{experiment[2]}"
        experimentValues = [
            value for value in values["Measurement_Value"]]
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
    axs.set_ylabel("Time, ns")

    plt.subplots_adjust(bottom=.1, left=.1)

    filename = path.join(
        cwd, f'../results/graphs/{resultSet}-{csvFilename}.png')
    plt.savefig(filename, dpi=200)
    # plt.show()
    plt.close()


prepare()

pattern = path.join(cwd, '../results/**/*-measurements.csv')

files = glob.glob(
    path.join(cwd, '../results/**/*-measurements.csv'), recursive=True)
for f in files:
    createGraph(f)
