# https://jakevdp.github.io/PythonDataScienceHandbook/03.07-merge-and-join.html
# aggregation_functions = {'price': 'sum', 'amount': 'sum', 'name': 'first'}
# df_new = df.groupby(df['id']).aggregate(aggregation_functions)
#https://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/

import pandas as pd
data = pd.read_csv('c:/Users/DCUK/.PyCharmCE2018.1/PycharmProjects/Aspnet_user/final_column_3 - Copy.csv')
df = pd.DataFrame(data)
new_func = df.groupby(['id']).first()
new_func.to_csv("column_4.csv")

import pandas as pd
data = pd.read_csv('c:/Users/DCUK/.PyCharmCE2018.1/PycharmProjects/Aspnet_user/final_column_3 - Copy.csv')
df = pd.DataFrame(data)
new_func = df.groupby(['id']).nth(1)
new_func.to_csv("column_5.csv")

import pandas as pd
data1 = pd.read_csv('c:/Users/DCUK/.PyCharmCE2018.1/PycharmProjects/Aspnet_user/column_4.csv')
data2 = pd.read_csv('c:/Users/DCUK/.PyCharmCE2018.1/PycharmProjects/Aspnet_user/column_5.csv')
columns = ["id", "Claim Type", "Claim Value", "a", "b", "c", "d"]
df1 = data1[columns]
l_1 = count(data1["a"])
df2 = data2[columns]
df3 = pd.merge(df1, df2, on='id')
print(df3)
list = []
for i in range (0, 2):
    list.append(i)
print (list)

import pandas as pd
data = pd.read_csv('c:/Users/DCUK/.PyCharmCE2018.1/PycharmProjects/Aspnet_user/final_column_3 - Copy.csv')
df = pd.DataFrame(data)
for i in range(0, 30):
    frame = df.groupby(['id']).nth(i)
print(frame)
    csv = frame.to_csv("column_", [i], ".csv")
    result = pd.concat([csv[i-1], csv[i]], axis=1)

print(result.head())
all_data = all_data.append(df,ignore_index=True)

frames = [ process_your_file(f) for i in df ]
result = pd.concat(frames)
new = df.groupby('id').apply(pd.to_csv("merge.csv")
new.to_csv("merge.csv")
print(new.he





# AttributeError: Cannot access callable attribute 'append' of 'DataFrameGroupBy' objects, try using the 'apply' method
