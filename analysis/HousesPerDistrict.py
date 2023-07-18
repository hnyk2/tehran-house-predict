import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('preprocess/cleaned_dataset.csv')


house_counts = data['district'].value_counts()


plt.figure(figsize=(10, 6))
house_counts.plot(kind='bar',color=["#4CC552","#54C571","#89C35C","#A0D6B4","#8FBC8F"])
plt.title('Count of Houses by District')
plt.xlabel('District')
plt.ylabel('Number of Houses')
plt.xticks(rotation=45)
plt.savefig('analysis/result/HousePerDistrict.png')
