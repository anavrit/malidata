import pandas as pd
import numpy as np
import os

df = pd.read_csv('data/gpw13_dashboard_regional_data_.csv', encoding = 'ISO-8859-1', engine='python')

""" Dropping columns with no values or the just one value """
df = df.drop(['type_detail', 'upload_detail', 'other_detail', 'use_dash', 'use_calc'], axis=1)

""" Fixing errors in medium and transformed names of indicators """
df.loc[df['ind']=='uhc_tobacco', ['transformed_name']] = 'Tobacco control'
df.loc[df['ind']=='water_rural', ['medium_name']] = 'Proportion of rural population using safely managed drinking water services (%)'

""" Assigning short name 'Surviving infants' to indicator surviving_infants """
df.loc[df['ind'] == 'surviving_infants', ['short_name']] = 'Surviving infants'
assert df['short_name'].isna().sum() == 0

""" Asserting lengths of indicator list and names are the same """
assert len(df['ind'].unique()) == len(df['short_name'].unique())
assert len(df['ind'].unique()) == len(df['medium_name'].unique())
assert len(df['ind'].unique()) == len(df['transformed_name'].unique())

""" Creating column for triple billion categories """
hep = ['cholera_campaign_denom', 'cholera_campaign_num', 'detect', 'detect_respond', 'espar', 'measles_routine',
       'meningitis_campaign_denom', 'meningitis_campaign_num', 'meningitis_routine', 'notify', 'polio_routine',
       'respond', 'surviving_infants', 'yellow_fever_campaign_denom', 'yellow_fever_campaign_num', 'yellow_fever_routine']
hpop = ['adult_obese', 'alcohol', 'child_obese', 'child_viol', 'devontrack', 'fuel', 'hpop_sanitation', 'hpop_sanitation_rural',
        'hpop_sanitation_urban', 'hpop_tobacco', 'ipv', 'overweight', 'pm25', 'road', 'stunting', 'suicide', 'transfats',
        'wasting', 'water', 'water_rural', 'water_urban']
uhc = ['anc4', 'art', 'beds', 'bp', 'doctors', 'dtp3', 'fh', 'fp', 'fpg', 'hwf', 'itn', 'nurses', 'pneumo', 'tb',
       'uhc_sanitation', 'uhc_tobacco']

df['billion'] = np.nan
df.loc[df['ind'].isin(hep), ['billion']] = 'HEP'
df.loc[df['ind'].isin(hpop), ['billion']] = 'HPP'
df.loc[df['ind'].isin(uhc), ['billion']] = 'UHC'

assert df['billion'].isna().sum() == 0

""" Function to save unique columns as tables """
def unique_table(data, cols):
    unique_df = pd.DataFrame({str(col): df[col].unique() for col in cols})
    unique_df['index'] = unique_df.index + 1

    return unique_df

df = df.sort_values(['iso3', 'ind', 'year'], ascending=True)
temp_iso = unique_table(df, ['iso3'])
temp_source = unique_table(df, ['source'])
temp_ind = unique_table(df, ['ind', 'short_name', 'medium_name', 'transformed_name'])

""" Merging country names with ISO3 """
temp_iso_country = pd.read_csv('data/data-verbose.csv', header=None, names=['iso3', 'country'])
temp_iso = temp_iso.merge(temp_iso_country, how='inner', on='iso3')
temp_iso = temp_iso.sort_values('iso3').reset_index(drop=True)
temp_iso.index += 1

""" Creating main GPW 13 dataframe """
df = df.drop(['short_name', 'medium_name', 'transformed_name'], axis=1)
def replace_columns(data, rdata, col):
    replacement = rdata.set_index(col)['index'].to_dict()
    return data[col].replace(replacement)
df['iso3'] = replace_columns(df, temp_iso, 'iso3')
df['source'] = replace_columns(df, temp_source, 'source')
df['ind'] = replace_columns(df, temp_ind, 'ind')

assert len(df['iso3'].unique()) == len(temp_iso)
assert len(df['source'].unique()) == len(temp_source)
assert len(df['ind'].unique()) == len(temp_ind)

""" Save all dataframes to csv """
def save_to_csv(data, name):
    if 'index' in data.columns:
        data.drop('index', axis=1, inplace=True)
    data.to_csv(os.path.join('data', f'{name}.csv'), sep=',', header=False, index=False)

save_to_csv(temp_iso, 'iso3')
save_to_csv(temp_source, 'source')
save_to_csv(temp_ind, 'ind')
save_to_csv(df, 'gpw13')
