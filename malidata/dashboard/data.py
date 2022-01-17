import pandas as pd
from .connect_database import conn

def uhc_data(indicator, country_list):
    # Extracting graph data from the database
    uhc = pd.read_sql(f"SELECT iso3, year, value, upper, lower FROM gpw13 WHERE indicator={indicator}", conn)
    uhc = uhc[uhc['iso3'].isin(country_list)]
    uhc[['value', 'lower', 'upper']] = uhc[['value', 'lower', 'upper']].round(2)
    iso = pd.read_sql(f"SELECT id, iso3 FROM iso3", conn)
    iso = iso[iso['id'].isin(country_list)]
    return uhc, iso
