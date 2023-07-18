import pandas as pd
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score,mean_absolute_percentage_error
from sklearn.impute import SimpleImputer

# Load the dataset
df = pd.read_csv('preprocess/cleaned_dataset.csv')


df['lat'] = df['lat'].str.replace('٫', '.').astype(float)
df['lng'] = df['lng'].str.replace('٫', '.').astype(float)




df['approve_time'] = pd.to_datetime(df['approve_time'])
df['year'] = df['approve_time'].dt.year
df['month'] = df['approve_time'].dt.month
df['day'] = df['approve_time'].dt.day
df['hour'] = df['approve_time'].dt.hour
df['minute'] = df['approve_time'].dt.minute


imputer = SimpleImputer(strategy='mean')
X = df[['rooms', 'foundation', 'estate_age', 'year', 'month','day','lat', 'lng']]
X = imputer.fit_transform(X)

y = df['price']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)



model = SVR()


model.fit(X_train, y_train)


y_pred = model.predict(X_test)


mpr = mean_absolute_percentage_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred, squared=False)
r2 = r2_score(y_test, y_pred)


print(mpr)
print("Mean Squared Error (MSE):", mse)
print("Root Mean Squared Error (RMSE):", rmse)
print("R-squared (R2) Score:", r2)