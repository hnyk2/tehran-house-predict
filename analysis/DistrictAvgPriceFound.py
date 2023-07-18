import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('preprocess/cleaned_dataset.csv')


foundation_ranges = [(i, i + 100) for i in range(0, 500, 100)]


data['foundation_range'] = pd.cut(data['foundation'], bins=[r[0] for r in foundation_ranges] + [foundation_ranges[-1][1]+1], labels=[f'{r[0]}-{r[1]}' for r in foundation_ranges], right=False)


avg_price_district_range = data.groupby(['district', 'foundation_range'])['price'].mean().reset_index()


pivot_table = avg_price_district_range.pivot(index='district', columns='foundation_range', values='price')


x_labels = [label.get_text() for label in plt.gca().get_xticklabels()]

plt.figure(figsize=(12, 6))
pivot_table.plot(kind='bar', stacked=True)
plt.title('Average House Price by District and Foundation Range')
plt.xlabel('District')
plt.ylabel('Average Price')
plt.xticks(rotation=45)
plt.legend(title='Foundation Range')
plt.savefig('analysis/result/DistrictAvgPriceFoundation.png')






