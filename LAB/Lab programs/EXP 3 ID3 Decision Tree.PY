import pandas as pd
from io import StringIO
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
csv_data = """Outlook,Temperature,Humidity,Wind,Play
Sunny,Hot,High,Weak,No
Sunny,Hot,High,Strong,No
Overcast,Hot,High,Weak,Yes
Rain,Mild,High,Weak,Yes
Rain,Cool,Normal,Weak,Yes
Rain,Cool,Normal,Strong,No
Overcast,Cool,Normal,Strong,Yes
Sunny,Mild,High,Weak,No
Sunny,Cool,Normal,Weak,Yes
Rain,Mild,Normal,Weak,Yes
Sunny,Mild,Normal,Strong,Yes
Overcast,Mild,High,Strong,Yes
Overcast,Hot,Normal,Weak,Yes
Rain,Mild,High,Strong,No
"""
data = pd.read_csv(StringIO(csv_data))
encoder = LabelEncoder()
for column in data.columns:
    data[column] = encoder.fit_transform(data[column])
X = data.iloc[:, :-1]
y = data.iloc[:, -1]
model = DecisionTreeClassifier(criterion="entropy")
model.fit(X, y)
sample = [[2, 1, 1, 1]]
prediction = model.predict(sample)
if prediction[0] == 1:
    print("Prediction: Play Tennis")
else:
    print("Prediction: Don't Play Tennis")