from typing import List, Any

# delete the duplicate way-1(only 1 column)
import pandas as pd
data = pd.read_csv('c:/Users/DCUK/.PyCharmCE2018.1/PycharmProjects/Aspnet_user/final_column_3.csv')
df = data[data["Claim Type"].str.match("gender")]
print(df.head())
columns = ["id", "Claim Type", "Claim Value"]
df1 = df[columns]
print(df1.head())
df1.to_csv("gender.csv", index=False)

seen = {}
dupes = []

for x in a:
    if x not in seen:
        seen[x] = 1
    else:
        if seen[x] == 1:
            dupes.append(x)
        seen[x] += 1


#Delete the duplicate way-2 (only 1 column)
import pandas as pd
data = pd.read_csv('c:/Users/DCUK/.PyCharmCE2018.1/PycharmProjects/gender.csv')
id = data["id"]
val = data["Claim Value"]
non_du_id = []
for x in sorted(set(id)):
    non_du_id.append(x)


#Delete the duplicate way-3 (whole dataframe)
import pandas as pd
data = pd.read_csv('c:/Users/DCUK/.PyCharmCE2018.1/PycharmProjects/gender.csv')
df = pd.DataFrame(data)
mask = df.duplicated(keep=False)
print(pd.value_counts(mask))
# False    239712
# True         79
# dtype: int64
mask1 = df.drop_duplicates(keep=False)
print(len(mask1))
# directly return   239712

non_du_id = df[~mask]
non_du_id.to_csv('non_du_id-2.csv')

import pandas as pd
data = pd.read_csv('c:/Users/DCUK/.PyCharmCE2018.1/PycharmProjects/Aspnet_user/final_column_3.csv')
df = data[data["Claim Type"].str.match("diabetes_type")]
columns = ["id", "Claim Type", "Claim Value"]
df1 = df[columns]
print(len(df1))
mask = df1.duplicated(keep=False)
print(len(mask))
print(pd.value_counts(mask))
mask1 = df1.drop_duplicates(keep=False)
print(len(mask1))

mask1.to_csv('non_du_id_db_type.csv', index=False)