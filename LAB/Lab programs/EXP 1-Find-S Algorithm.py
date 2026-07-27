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

specific_h = concepts[0].copy()

print("Initial Hypothesis:")
print(specific_h)

for i, instance in enumerate(concepts):
    if target[i] == "Yes":
        for j in range(len(specific_h)):
            if instance[j] != specific_h[j]:
                specific_h[j] = "?"
    print(f"Step {i+1}: {specific_h}")

print("\nFinal Hypothesis:")
print(specific_h)