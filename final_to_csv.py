import pandas as pd
data = pd.read_csv('c:/Users/DCUK/Desktop/isabelle/Krish/aspnet_user/aaa.csv')
col = pd.DataFrame(data["a,a,a"].str.split(',').tolist(), columns=['id', 'Claim Type', 'Claim Value', 'a', 'b', 'c', 'd'])
col.to_csv("column_3.csv")
