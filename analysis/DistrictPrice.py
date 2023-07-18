import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('preprocess/cleaned_dataset.csv')


avg_price_district = data.groupby('district')['price'].mean().sort_values()


plt.figure(figsize=(10, 6))
avg_price_district.plot(kind='bar', color = ["#659EC7","#3090C7","#357EC7","#368BC1","#6495ED","#77BFC7"])
plt.title('Average House Price by District')
plt.xlabel('District')
plt.ylabel('Average Price')
plt.xticks(rotation=45)
plt.savefig('analysis/result/DistrictAvgPrice.png')
