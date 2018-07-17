df = data[data["Claim Type"].str.match("country")]


import pandas as pd

data = pd.read_csv('c:/Users/DCUK/.PyCharmCE2018.1/PycharmProjects/country-2.csv')
df = pd.DataFrame(data)
cv = df["Claim Value"]
cv_list = cv.tolist()
cv1 = df[cv.str.match("United Kingdom")]
cv2 = cv.str.replace("UK", "United Kingdom")
cv2 = cv2.str.replace("uk", "United Kingdom")
cv2 = [i.replace("0", "nan") for i in cv2]

cv3 = df.assign(UK=cv2)
df1 = pd.Series(v for v in cv2)
df1 = df1.value_counts()

import pandas as pd
import regex as re

# change to lowercase first
data = pd.read_csv ('c:/Users/DCUK/.PyCharmCE2018.1/PycharmProjects/country-2.csv')
df = pd.DataFrame (data)
col = ["Claim Value", "a", "b", "c", "d"]
df1 = df[col].apply (lambda x: x.astype (str).str.lower ())
df2 = df1.apply(lambda x: x.astype(str).str.replace("united kingdom", "uk"))
#delete the space in the end of string
df3 = df2.apply(lambda x: x.astype(str).str.strip())
uk1 = df3["Claim Value"].value_counts()
cv = df3["Claim Value"].tolist()
aa = []
for i in cv:
    a  = re.sub('\w+\s[u][k]$', "uk", i)
    aa.append(a)

uk = aa.count("uk")
df4 = df3.assign(aa=aa)
df4.to_csv("country-4.csv", index=False)

#join the column
import pandas as pd
data = pd.read_csv('c:/Users/DCUK/.PyCharmCE2018.1/PycharmProjects/country-4.csv')
df = pd.DataFrame(data)
df = df.rename({'a':'column1', 'b':'column2', 'c':'column3', 'd':'column4', 'aa':'country_lower'}, axis=1)

df2 = df.assign(country_merge= df["column1"].astype(str) + ', ' + df["column2"].astype(str) + ', '+df["column3"].astype(str))
df2.to_csv("country-5.csv", index=False)

#join the postcode and country
import pandas as pd
data = pd.read_excel('C:/Users/DCUK/.PyCharmCE2018.1/PycharmProjects/Aspnet_user/final_column_3 - Copy01.xlsx', sheet_name="postalcode")
df = pd.DataFrame(data)
df.columns = ["id", "postcode", "a", "b", "c", "d", "e"]
df1 = pd.read_csv('c:/Users/DCUK/.PyCharmCE2018.1/PycharmProjects/Aspnet_user/country-3.csv')
df1 = pd.DataFrame(df1)
col = ["id", "Claim Type", "a", "b", "c", "d", "aa"]
df1 = df1[col]
result = pd.merge(df, df1, on='id')
result["a_x"] = result["a_x"].str.strip()
num = result["a_x"].str.startswith(tuple('0123456789'),na=False)
a = num.value_counts()
#using data.loc[] to select the row that postcode only contain number in the front
num1 = result.loc[num]
num1.to_csv("post+country_num.csv", index=False)
#or use contains
ax = result["a_x"]
b = ax.str.contains('^[0-9]', na=False)
bb = b.value_counts()
alpha = ax.str.contains('^[a-zA-Z]+', na=False)
alpha_count = alpha.value_counts()
alpha = result.loc[alpha]
alpha.to_csv("post+country_alpha.csv", index=False)

#wrong output
num1 = ax.str.isnumeric()
b = num1.value_counts()

#NOt sure why is not working but maybe is because regex's pattern don't use series
c = result["a_x"].str()
import re
num2 = re.search('^\s*[0-9]',c)
c = num2.value_counts()


#clean 0 and -1
data = pd.read_csv('c:/Users/DCUK/.PyCharmCE2018.1/PycharmProjects/Aspnet_user/post+country_num.csv', index_col="aa")
clean = data.drop(["0","-1"])
clean["country"] = clean.index
aa = clean["country"].value_counts()
data1 = pd.read_csv('c:/Users/DCUK/.PyCharmCE2018.1/PycharmProjects/Aspnet_user/post+country_alpha.csv', index_col="aa")
clean1 = data1.drop(["0","-1"])
clean1["country"] = clean1.index
bb = clean1["country"].value_counts()
aa = pd.DataFrame(aa)
aa["freq"] = aa["country"]
aa["country"] = aa.index
bb = pd.DataFrame(bb)
bb["freq"] = bb["country"]
bb["country"] = bb.index
bb = bb.drop("country1", axis=1)
result1 = pd.concat([aa, bb], axis=1, join_axes=[bb.index])
result = pd.merge(bb, aa, how='left', on=['country'])
import numpy as np
result["freq_y"] = result["freq_y"].replace(np.nan, 0)
result["freq_x"] = result["freq_x"].replace(np.nan, 0)
result["z"] = result["freq_x"]+result["freq_y"]
result.to_csv("country_map.csv", index=False)
#make a map
import pandas as pd
import vincent
data = pd.read_csv("c:/Users/DCUK/.PyCharmCE2018.1/PycharmProjects/Aspnet_user/country_map.csv")
col = ["country", "z"]
data = data[col]
world_countries = r'world-countries.json'
geo_data = [{'name': 'countries',
             'url': world_countries,
             'feature': 'world-countries'}]
vis = vincent.Map(data=data,
                  geo_data=geo_data,
                  scale=1100,
                  data_bind='z',
                  data_key='country',
                  map_key={'countries': 'id'})

from IPython.display import display
vis.display()

print(vis)
vis.to_json("c:/Users/DCUK/.PyCharmCE2018.1/PycharmProjects/Aspnet_user/map.json")
world = vincent.Map(width=1200, height=1000)
world.geo_data(projection='winkel3', scale=200, world=world_countries)


import json
map = json.load(open("c:/Users/DCUK/.PyCharmCE2018.1/PycharmProjects/Aspnet_user/map.json"))
print(map)
#not working

#try basemap but pycharm can't install basemap

#If you do want literal replacement of a string (equivalent to str.replace()),
# you can set the optional regex parameter to False, rather than escaping each character.
# In this case both pat and repl must be strings:

import pandas as pd

cols = ['country', 'z']
df = pd.read_csv("c:/Users/DCUK/.PyCharmCE2018.1/PycharmProjects/Aspnet_user/country_map.csv", usecols=cols)
df["country"] = df["country"].str.title()
df = pd.DataFrame(df)
index = df.set_index('country', inplace=True)
values = df['z']

import pycountry
import pandas as pd

cols = ['country', 'z']
df = pd.read_csv("c:/Users/DCUK/.PyCharmCE2018.1/PycharmProjects/Aspnet_user/country_map.csv", usecols=cols)
df["country"] = df["country"].str.title()
df = df.replace("Bolivia", 'Bolivia, Plurinational State of')
df = df.replace("Uk", "United Kingdom")
df = df.replace("Usa", "United States")
df = df.replace("Isle Of Man", 'Isle of Man')
df = df.replace('Korea', 'Korea, Republic of')
df = df.replace('Curaã§Ao', 'Curaçao')
df = df.replace('Trinidad And Tobago', 'Trinidad and Tobago')
df = df.replace('Tanzania', 'Tanzania, United Republic of')
df = df.replace('Vietnam', 'Viet Nam')
df = df.replace('Iran', 'Iran, Islamic Republic of')
df = df.replace('Virgin Islands', 'Virgin Islands, U.S.')
df = df.replace('Czech Republic', 'Czechia')
df = df.replace('Saint Barthã©Lemy', 'Saint Barthélemy')
input_countries = df["country"]
countries = {}
for country in pycountry.countries:
    countries[country.name] = country.alpha_3
codes = [countries.get(country, 'Unknown code') for country in input_countries]
df = df.assign(code = codes)
df[5] = df[5] + df[31]
