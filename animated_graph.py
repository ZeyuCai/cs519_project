import matplotlib.pyplot as plt
import matplotlib.animation as ani
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

# df_clean = pd.read_csv("./out.csv", index_col=0)
# create animation
# animation in jupyter files
