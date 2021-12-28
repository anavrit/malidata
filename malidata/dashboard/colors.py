import random
from .connect_database import conn
import pandas as pd

iso = pd.read_sql(f"SELECT iso3 FROM iso3", conn)
iso_list = iso['iso3'].values.tolist()

# Random color generation
fillcolors = {}
colors = {}
for iso in iso_list:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    fillcolors[iso] = 'rgba(' + str(r) + ', ' + str(g) + ', ' + str(b) + ', 0.2)'
    colors[iso] = 'rgba(' + str(r) + ', ' + str(g) + ', ' + str(b) + ', 1)'

fillcolors['MLI'] = 'rgba(0, 100, 80, 0.2)'
colors['MLI'] = 'rgba(0, 100, 80, 1)'
