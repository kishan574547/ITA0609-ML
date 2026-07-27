import pandas as pd
from io import StringIO

csv_data = """Sky,AirTemp,Humidity,Wind,Water,Forecast,EnjoySport
Sunny,Warm,Normal,Strong,Warm,Same,Yes
Sunny,Warm,High,Strong,Warm,Same,Yes
Rainy,Cold,High,Strong,Warm,Change,No
Sunny,Warm,High,Strong,Cool,Change,Yes
"""

data = pd.read_csv(StringIO(csv_data))

concepts = data.iloc[:, :-1].values
target = data.iloc[:, -1].values

specific = concepts[0].copy()
general = [["?" for _ in range(len(specific))] for _ in range(len(specific))]

for i, instance in enumerate(concepts):
    if target[i] == "Yes":
        for j in range(len(specific)):
            if instance[j] != specific[j]:
                specific[j] = "?"
                general[j][j] = "?"
    else:
        for j in range(len(specific)):
            if instance[j] != specific[j]:
                general[j][j] = specific[j]
            else:
                general[j][j] = "?"

print("Specific Hypothesis:")
print(specific)

print("\nGeneral Hypothesis:")
for g in general:
    print(g)