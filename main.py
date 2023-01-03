import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
data = pd.read_csv('data_weather.csv')
print("Columns are: ",data.columns)
print("Data: \n",data)
print("Null Data: \n",data[data.isnull().any(axis=1)])
del data['number']
before_rows = data.shape[0]
print(before_rows)
data = data.dropna()
after_rows = data.shape[0]
print(after_rows)
print("Total rows dropped: ",before_rows - after_rows)
clean_data = data.copy()
clean_data['high_humidity_label'] = (clean_data['relative_humidity_3pm'] > 24.99)*1
print(clean_data['high_humidity_label'])
y=clean_data[['high_humidity_label']].copy()
clean_data['relative_humidity_3pm'].head()
print("Y Data: \n",y.head())
morning_features = ['air_pressure_9am', 'air_temp_9am', 'avg_wind_direction_9am', 'avg_wind_speed_9am','max_wind_direction_9am', 'max_wind_speed_9am', 'rain_accumulation_9am','rain_duration_9am']
X = clean_data[morning_features].copy()
print("Columns in X: ", X.columns)
print("Columns in Y: ", y.columns)
X_train, X_test, y_train, y_test = train_test_split(X, y,
test_size=0.33, random_state=324)
print ("X_train is as under:")
print(X_train.head())
print ("X_test is as under:")
print(X_test.head())
print ("y_train is as under:")
print(y_train.head())
print ("y_test is as under:")
print(y_test.head())
print ("Let us describe y_train")
y_train.describe()
humidity_classifier = DecisionTreeClassifier(max_leaf_nodes=10,
random_state=0)
humidity_classifier.fit(X_train, y_train)
type(humidity_classifier)
predictions = humidity_classifier.predict(X_test)
print("Sample Predictions: \n",predictions[:10])
print("Sample Y Test(Actual Data):\n",y_test['high_humidity_label'][:10])
print("Accuracy: \n",accuracy_score(y_true = y_test, y_pred = predictions))

