from matplotlib import pyplot as plt
import pandas as pd
import requests

df = pd.read_csv('thor_wwii.csv')

summed_df = df.groupby(['COUNTRY_FLYING_MISSION']).sum()
summed_df = summed_df / 1000
summed_df = summed_df.reset_index()

print(summed_df)

countries = summed_df['COUNTRY_FLYING_MISSION'].tolist()
###
tons_he = summed_df['TONS_HE'].tolist()
tons_ic = summed_df['TONS_IC'].tolist()
tons_frag = summed_df['TONS_FRAG'].tolist()
###


fig, ax = plt.subplots()

ax.bar(countries, tons_he, label='High Explosive')
ax.bar(countries, tons_ic, label='Incendiary')
ax.bar(countries, tons_frag, label='Fragmentation')

ax.set_ylabel('Kilotons of Munitions')
ax.set_xlabel('Countries')
ax.set_title('Munitions Dropped by Allied Country')

ax.legend()

plt.yticks(fontsize ='xx-small')
plt.xticks(rotation=-90, fontsize='xx-small')
plt.show()
