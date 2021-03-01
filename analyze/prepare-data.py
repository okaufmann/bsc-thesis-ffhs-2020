import pandas as pd
import os.path as path
import os
import glob

cwd = path.dirname(__file__)

allDataFile = path.join(cwd, f'../results/all-data.csv')
allDataHeadersWritten = False


def prepare():

    # clear all data
    allData = path.join(cwd, f'../results/all-data.csv')
    if path.exists(allData):
        os.remove(allData)


def appendDataFrames(content):
    file = open(allDataFile, 'a')
    file.write(content)
    file.close()


def prepareData(csvPath):
    global allDataHeadersWritten

    df = pd.read_csv(csvPath,
                     usecols=["Target", "Target_Type", "Target_Method", "Params", "Measurement_IterationStage",
                              "Measurement_Value", "Measurement_Nanoseconds", "Allocated_Bytes"],
                     )

    resultSet = path.basename(path.dirname(
        path.split(path.abspath(csvPath))[0]))

    results = df.query('Measurement_IterationStage == "Result"')
    results["Result_Set"] = resultSet

    writeHeaders = not allDataHeadersWritten
    appendDataFrames(results.to_csv(
        index=False, header=writeHeaders))
    allDataHeadersWritten = True


prepare()

pattern = path.join(cwd, '../results/_raw/**/*-measurements.csv')

files = glob.glob(
    path.join(cwd, '../results/**/*-measurements.csv'), recursive=True)
for f in files:
    prepareData(f)
