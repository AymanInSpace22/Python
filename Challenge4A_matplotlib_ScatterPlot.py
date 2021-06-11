from matplotlib import pyplot as plt
import pandas as pd
import requests

print('***Environment Successfully Configured***')

df = pd.read_csv('thor_wwii.csv')
print(df)
print(df.columns.tolist())

sample = df.sample(50)
print('Sample DataFrame:')
print(sample)

aircraft = sample['AC_ATTACKING'].tolist()
print("Aircraft List:")
print(aircraft)
munition = sample['TOTAL_TONS'].tolist()
print('Munition List:')
print(munition)

text = 'Bombing Run'

plt.scatter(aircraft, munition, label=text)
plt.xlabel('Tons of Munition Dropped')
plt.ylabel('Number of Attacking Aircraft')
plt.title('Attacking Aircraft and Tonnage')
plt.grid(True, linewidth=1, linestyle='--')
plt.show()
