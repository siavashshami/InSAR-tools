import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt 
import numpy

plt.figure(figsize=(20,20))
plt.grid(True)
#plt.style.use('seaborn-v0_8-poster')
plt.style.use('classic')
matplotlib.rcParams['savefig.dpi'] = 500

font = {'family' : 'Times new roman'}
plt.rcParams["font.family"] = "Times New Roman"
matplotlib.rcParams.update({'font.size': 16})

df = pd.read_csv('A_SJB1.csv')
df.index = df['GPS_Date']
df.index = pd.to_datetime(df.index)

df1 = pd.read_csv('B_SJB1.csv')
df1.index = df1['InSAR_Date']
df1.index = pd.to_datetime(df1.index)

x = np.arange(len(df['GPS_up']))
slope, intercept = np.polyfit(x, df['GPS_up'], 1)
GPS_trendline = intercept + slope * x
GPS_velocity = slope

x1 = np.arange(len(df1['InSAR_up']))
slope1, intercept1 = np.polyfit(x1, df1['InSAR_up'], 1)
InSAR_trendline = intercept1 + slope1 * x1
InSAR_velocity = slope1

plt.plot(df['GPS_up'], color ='black')
plt.plot(df1['InSAR_up'], color ='blue')

plt.plot(df.index, GPS_trendline, color='black', label='GPS_trendline')
plt.plot(df1.index, InSAR_trendline, color='blue', label='InSAR_trendline')

plt.annotate('GPS velocity: %.2f mm/year'%(GPS_velocity*365.25), xy=(df.index[0],max(df['GPS_up'])), xytext=(-10, -280), textcoords='offset points', fontsize=16, fontname="Times new roman")
plt.annotate('InSAR velocity: %.2f mm/year'%(InSAR_velocity*(365.25/12)), xy=(df1.index[0],max(df1['InSAR_up'])), xytext=(-10, -310), textcoords='offset points', fontsize=16, fontname="Times new roman")

plt.xlabel('Date (Year-Month)', fontsize=16, fontname="Times new roman")
plt.ylabel('Displacement (mm)', fontsize=16, fontname="Times new roman")
plt.title('Comparison of the displacement time series of InSAR and GPS at SJB1 station', fontsize=14, fontname="Times new roman")
plt.legend(['GPS', 'InSAR', 'GPS_trendline', 'InSAR_trendline'], loc='upper right', prop={'family': 'Times New Roman', 'size': 14})

plt.show()