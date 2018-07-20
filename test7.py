# probability of results of coin experiment

import random
import csv

def coin_trial():
    heads = 0
    for i in range(100):
        if random.random() <= 0.5:
            heads += 1
    return heads


def simulate(n):
    trials = []
    for i in range(n):
        trials.append(coin_trial())
    return (sum(trials)/n)


# print(simulate(100000))

with open("wine-data.csv", "r", encoding="latin-1") as f:
    wines = list(csv.reader(f))

print(wines)

# Extract the Tokaji scores
tokaji = []
non_tokaji = []
for wine in wines:
    if wine[4] != '':
        wine[4] = wine[4]
    if wine[9] == "Tokaji":
        tokaji.append(float(wine[4]))
    else:
        non_tokaji.append(wine[4])

# Extract the Lambrusco scores
lambrusco = []
non_lambrusco = []
for wine in wines:
    if wine[4] != '':
        wine[4] = wine[4]
    if wine[9] == "Lambrusco":
        lambrusco.append(float(wine[4]))
    else:
        non_lambrusco.append(float(wine[4]))
