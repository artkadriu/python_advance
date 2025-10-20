import pandas as pd
import matplotlib.pyplot  as plt
df = pd.read_csv('avgIQpercountry.csv')
nobel_prizes_per_continent = df.groupby('Continent')['Nobel Prices'].sum()
no_of_continents = nobel_prizes_per_continent.count()
print(no_of_continents)


colors = ['red', 'blue', 'orange', 'gray', 'black','green','gold' ,'purple']
plt.figure(figsize=(10, 6))
nobel_prizes_per_continent.plot(kind="pie", colors=colors, autopct='%1.1f%%')


plt. title( 'Distribution of Noble Prizes by Continent')
plt.axis('equal')
plt.ylabel('')
plt.tight_layout()
plt.show()