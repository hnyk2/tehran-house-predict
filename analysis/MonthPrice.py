import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('preprocess/cleaned_dataset.csv')


data['month'] = pd.to_datetime(data['approve_time']).dt.month
data['year'] = pd.to_datetime(data['approve_time']).dt.year


avg_price_by_month_year = data.groupby(['year', 'month'])['price'].mean()


avg_price_by_month_year = avg_price_by_month_year.reset_index()


plt.figure(figsize=(12, 6))
for year in avg_price_by_month_year['year'].unique():
    data_year = avg_price_by_month_year[avg_price_by_month_year['year'] == year]
    plt.plot(data_year['month'], data_year['price'], marker='o', label=year)
plt.title('Average House Price by Month and Year')
plt.xlabel('Month')
plt.ylabel('Average Price')
plt.xticks(range(1, 13))  # Set the x-axis ticks to show all months
plt.grid(True)
plt.legend(title='Year')
plt.savefig('analysis/result/AvgPricePerMonth.png')

