import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from scipy.interpolate import make_interp_spline


df = pd.read_csv('s23.csv')
df.index = df['Time1']
df.index = pd.to_datetime(df.index.astype(str), format='%Y%m%d', errors='ignore')
df1 = pd.read_csv('s23.csv')
df1.index = df1['Time2']
df1.index = pd.to_datetime(df1.index.astype(str), format='%Y%m%d', errors='ignore')
df2 = pd.read_csv('s23.csv')
df2.index = df2['Time3']
df2.index = pd.to_datetime(df2.index)

fig = plt.figure()
ax = fig.add_subplot()
lns1 = ax.plot(df2['well'], color="blue", marker="", label='Piezometer', linestyle='solid', linewidth=0.8)
ax.set_xlabel("Time [year]", fontsize=14)
ax.set_ylabel("Grounwater Level Change [m]", color="black", fontsize=14)

ax2 = ax.twinx()
lns2 = ax2.plot(df['as'], color="red", marker="", label='Ascending', linestyle='solid', linewidth=1)
lns3 = ax2.plot(df1['des'], color="green", marker="", label='Descending', linestyle='solid', linewidth=1)
ax2.set_ylabel("LOS Displacement [mm]",color="black",fontsize=14)


lns = lns1+lns2+lns3
#lns = np.array(lns1+lns2+lns3)
labs = [l.get_label() for l in lns]
ax.legend(lns, labs, loc='upper left')
plt.show()

fig.savefig('test.jpg',
            format='jpeg',
            dpi=400,
            bbox_inches='tight')