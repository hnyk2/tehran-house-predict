import pandas as pd


df = pd.read_csv('updated_dataset.csv')

missing_values = df.isnull().sum()
print("Missing Values:\n", missing_values)


drop_columns = ['rooms','foundation','estate_age','price','approve_time','district']
df.dropna(subset=drop_columns, inplace=True)


z_score = (df['price'] - df['price'].mean()) / df['price'].std()
df = df.loc[abs(z_score) < 3] 



df.drop_duplicates(inplace=True)


selected_features = ['rooms','foundation','estate_age','price','approve_time','district','lat','lng']
df = df[selected_features]


df.to_csv('cleaned_dataset.csv', index=False)

