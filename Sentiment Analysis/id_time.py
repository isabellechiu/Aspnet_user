import pandas as pd
df = pd.read_csv("C:/Users/DCUK/Desktop/isabelle/Krish/Sentiment analysis/td_questions.csv", usecols=["user_id", "course_id", "timestamp"])
user_cv = df["user_id"].value_counts()
course_cv = df["course_id"].value_counts()

from datetime import datetime, date, time
dt_now = datetime.now()
time = df["timestamp"].astype(str)
dt = [datetime.strptime(i,"%d/%m/%Y %H:%M") for i in time]
for i in dt:
    tt = i.timetuple()
    print(tt[0])
2006    # year
11      # month
21      # day
16      # hour
30      # minute
0       # second
1       # weekday (0 = Monday)
325     # number of days since 1st January
-1      # dst - method tzinfo.dst() returned None
df['year'] = pd.DatetimeIndex(df['timestamp']).year
year_cv = df['year'].value_counts()
df['day'] = pd.DatetimeIndex(df['timestamp']).day
day_cv = df['day'].value_counts()
df['dayofweek'] = pd.DatetimeIndex(df['timestamp']).dayofweek
dayofweek_cv = df['dayofweek'].value_counts()
df['dayofyear'] = pd.DatetimeIndex(df['timestamp']).dayofyear
dayofyear_cv = df['dayofyear'].value_counts()

df['time'] = pd.DatetimeIndex(df['timestamp']).time
time_d = df['time'].describe()

##or
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['y_m_d'] = df['timestamp'].dt.to_period('D')
##or
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['month'] = df['timestamp'].dt.month
month_cv = df['month'].value_counts()

dt1 = df['y_m_d'].describe()
import numpy as np
df_d = df.describe(include = [np.number])
print(df_d)

df_a = df.describe(include='all')
print(df_a)
cols = ['user id', 'course id', 'date', 'time', 'year', 'month', 'day', 'day of week']
index = ['max', 'freq','total']
id_time = pd.DataFrame(columns=cols, index=index)
id_time[cols[0]] = ["205783", "82", '8169']
id_time[cols[1]] = ["2", "3445", '']
id_time[cols[2]] = ["15-04-2016", '50', '']
id_time[cols[3]] = ["07:46:00", "19", '']
id_time[cols[4]] = ["2016", "4662", '']
id_time[cols[5]] = ["April", "951", '']
id_time[cols[6]] = ["4", "466", '']
id_time[cols[7]] = ["Wednesday", "1326",'']

id_time.to_excel("id_time.xlsx")



