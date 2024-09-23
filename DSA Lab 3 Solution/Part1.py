# Solved Population Example
# import matplotlib.pyplot as plt 
# import pandas as pd
# df = pd.read_csv("Data/population_by_country_2020.csv") 
# print(df.dtypes)
# list1 = df['Country (or dependency)'].values.tolist() 
# list2 = df['Population (2020)'].values.tolist() 
# plt.bar(list1, list2,width = 1, color = ['red', 'green'])
# # plt.plot(list1[:5],list2[:5])
# # plt.pie(list2[:10])
# plt.show()

#Task 01
# import matplotlib.pyplot as plt
# import pandas as pd
# df=pd.read_csv("Data/dailySteps_merged.csv")
# Day=df['ActivityDay'].values.tolist()
# Steps=df['StepTotal'].values.tolist()
# plt.plot(Day,Steps)
# plt.show()

# Task 02
# import matplotlib.pyplot as plt
# import pandas as pd
# df=pd.read_csv("Data/dailyActivity_merged.csv")
# day=df['ActivityDate'].values.tolist()
# totaldistance=df['TotalDistance'].values.tolist()
# plt.bar(day,totaldistance,width=1,color=['red','green','blue'])
# plt.show()

# Task 03
# import matplotlib.pyplot as plt
# import pandas as pd
# df=pd.read_csv("Data/sleepDay_merged.csv")
# day=df['SleepDay'].values.tolist()
# bedtime=df['TotalTimeInBed'].values.tolist()
# plt.scatter(day,bedtime)
# plt.show()

# Task 04
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Data/hourlySteps_merged.csv")
df['ActivityHour'] = pd.to_datetime(df['ActivityHour'], format='%m/%d/%Y %I:%M:%S %p')
df_filtered = df[df['ActivityHour'].dt.date == pd.to_datetime('2016-04-12').date()]
Hours = df_filtered['ActivityHour'].dt.strftime('%I:%M %p').tolist()
Steps = df_filtered['StepTotal'].values.tolist() 
plt.pie(Steps, labels=Hours)
plt.show()






