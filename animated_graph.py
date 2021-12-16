import matplotlib.pyplot as plt
import matplotlib.animation as ani
import matplotlib.dates as mdates
from matplotlib.pyplot import cm
import numpy as np
import pandas as pd 
import itertools

DATA_DIR = "/".join([".", "data"])
DATA_FILE = "us-states.csv"
DATA_PATH = "/".join([DATA_DIR, DATA_FILE])
COL_STATE = "state"
COL_CASES = "cases"

# read info in the source
df_src = pd.read_csv(DATA_PATH)
all_dates = list(df_src.index.drop_duplicates())
all_states = list(df_src[COL_STATE].drop_duplicates())
# create a new df 
# prep data 
data = np.zeros((len(all_dates), len(all_states)))
for i in range(len(all_dates)):
    for j in range(len(all_states)):
        cur_date = all_dates[i]
        cur_state = all_states[j]
        df_row = df_src.loc[df_src.index.isin([cur_date]) 
                & df_src[COL_STATE].isin([cur_state])]
        if(df_row.empty): continue
        cases = df_row.at[cur_date, COL_CASES]
        data[i,j] = cases
df_clean = pd.DataFrame(data = data,
    index = all_dates,
    columns = all_states)

# Draw the graph
region_of_interest = ["Washington", "Illinois", "California", "Arizona", "Alabama"]
df = df_clean.loc[:, region_of_interest]
n = len(region_of_interest)

# create animation
# set the line color
color = ['red', 'green', 'blue', 'orange','yellow']
fig, ax = plt.subplots()
ax.xaxis.set_major_locator(mdates.AutoDateLocator())
plt.xticks(rotation=45, ha="right", rotation_mode="anchor") 
plt.subplots_adjust(bottom = 0.2, top = 0.9) 
plt.ylabel('No of Cases')
plt.xlabel('Dates')

def stepfunc(i=int):
    plt.legend(df.columns)
    p = plt.plot(df[:i].index, df[:i].values) #note it only returns the dataset, up to the point i
    for i in range(0,n):
        p[i].set_color(color[i]) #set the colour of each curve
animator = ani.FuncAnimation(fig, stepfunc, interval = 200)
plt.show()
