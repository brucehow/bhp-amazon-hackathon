import csv
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
#import pandas as pd

csv_file = open("data.csv", "r")
csv_reader = csv.reader(csv_file)

acid_file = open("modData.csv", "r")
read = csv.reader(acid_file)
ACID_LMIN = []
next(read)
for row in read:
    ACID_LMIN.append(float(row[5]))

for i in range(0,4):
    next(csv_reader)
CU_BOIL_FEED, CU_BOIL_FEED_TEMP, PUMP_AMPS_A, PUMP_AMPS_B, TS = [], [], [], [], []
CB_REBOILER_TEMP = []
FEED_PUMP = []
for row in csv_reader:
    TS.append(row[0].split(" ")[0])
    CU_BOIL_FEED_TEMP.append(float(row[44]))
    CU_BOIL_FEED.append(float(row[6]))
    PUMP_AMPS_A.append(float(row[20]))
    PUMP_AMPS_B.append(float(row[21]))
    CB_REBOILER_TEMP.append(float(row[47]))
    FEED_PUMP.append(float(row[27]))

def plotAmps():
    plt.figure()
    plt.title("Pump A vs Pump B")
    plt.plot(PUMP_AMPS_A, label="A")
    plt.plot(PUMP_AMPS_B, label="B")
    plt.xlabel("Time (Hours)")
    plt.ylabel("Amps (A)")
    plt.legend(loc='lower left')

def plotTemp():
    plt.figure()
    plt.title("Feed vs Boiler Temperature")
    plt.plot(CU_BOIL_FEED_TEMP, label="Cu Feed Temp")
    plt.plot(CB_REBOILER_TEMP, label="Reboiler Temp")
    plt.xlabel("Time (Hours)")
    plt.ylabel("Temperature (C)")
    plt.legend(loc='lower left')


def dataFrame():
    df = pd.DataFrame({"DATE":TS, "CU_FEED_TEMP":CU_BOIL_FEED_TEMP,
                       "CU_FEED_L/MIN":CU_BOIL_FEED,
                       "PUMPAMPS_A":PUMP_AMPS_A,
                       "PUMPAMPS_B": PUMP_AMPS_B})
    df.to_csv("modData.csv", index=False)

plotTemp()
plt.show()