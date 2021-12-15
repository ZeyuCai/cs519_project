import csv
from tqdm import tqdm


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import folium


# id,population,name,dosesAdministered,peopleVaccinated,completedVaccination,completedOneDoseVaccination,boosterDosesAdministered,cdcDosesDistributed

# date,state,fips,cases,deaths,confirmed_cases,confirmed_deaths,probable_cases,probable_deaths

url = (
    "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data"
)
state_geo = f"{url}/us-states.json"

infect_data = pd.read_csv(open('infect.csv', 'r'))
vaccine_data = pd.read_csv(open('vaccine.csv', 'r'))

# print(vaccine_data.columns)
# state2id = pd.Series(vaccine_data.id.values,index=vaccine_data.name).to_dict()
# print(state2id)
# infect_data['id']= infect_data['state'].map(state2id)
# print(infect_data.head())

total_data = infect_data.merge(vaccine_data, left_on='state', right_on='name')
total_data['infect_rate'] = total_data['confirmed_cases']/total_data['population']


total_data['vaccine_rate'] = total_data['peopleVaccinated']/total_data['population']

m = folium.Map(location=[48, -102], zoom_start=3)

folium.Choropleth(
    geo_data=state_geo,
    name="choropleth",
    data=total_data,
    columns=["id", "infect_rate"],
    key_on="feature.id",
    fill_color="YlGn",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Infection rate",
).add_to(m)

folium.Choropleth(
    geo_data=state_geo,
    data=total_data,
    columns=["id", "vaccine_rate"],
    key_on="feature.id",
    fill_color="BuPu",
    fill_opacity=0.7,
    line_opacity=0.5,
    legend_name="Vaccination rate",
).add_to(m)
folium.LayerControl().add_to(m)
m.save("index.html")
