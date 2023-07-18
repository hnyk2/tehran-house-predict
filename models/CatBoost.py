import pandas as pd
from catboost import CatBoostRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.impute import SimpleImputer

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
X = df[['rooms', 'foundation', 'estate_age', 'year', 'month','lat', 'lng']]
X = imputer.fit_transform(X)

y = df['price']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = CatBoostRegressor()


model.fit(X_train, y_train)


y_train_pred = model.predict(X_train)


y_test_pred = model.predict(X_test)


mse_train = mean_squared_error(y_train, y_train_pred)
rmse_train = mean_squared_error(y_train, y_train_pred, squared=False)
r2_train = r2_score(y_train, y_train_pred)


mse_test = mean_squared_error(y_test, y_test_pred)
rmse_test = mean_squared_error(y_test, y_test_pred, squared=False)
r2_test = r2_score(y_test, y_test_pred)


print("Training Set:")
print("Mean Squared Error (MSE):", mse_train)
print("Root Mean Squared Error (RMSE):", rmse_train)
print("R-squared (R2) Score:", r2_train)

print("\nTest Set:")
print("Mean Squared Error (MSE):", mse_test)
print("Root Mean Squared Error (RMSE):", rmse_test)
print("R-squared (R2) Score:", r2_test)
