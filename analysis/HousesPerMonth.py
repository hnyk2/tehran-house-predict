import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('preprocess/cleaned_dataset.csv')


data['approve_time'] = pd.to_datetime(data['approve_time'])


data['month'] = data['approve_time'].dt.month


houses_per_month = data['month'].value_counts().sort_index()


plt.figure(figsize=(10, 6))
houses_per_month.plot(kind='bar',color= "#800085")
plt.title('Count of Houses per Month')
plt.xlabel('Month')
plt.ylabel('Number of Houses')
plt.xticks(rotation=0)
plt.savefig('analysis/result/HousePerMonth.png')
