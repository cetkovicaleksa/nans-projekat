from typing import Tuple
import pandas as pd

from constants import (
    DATA_FILE, COLS, INDEX_COLS
)




def get_dataset(path: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
    
    dataset = pd.read_csv(path, usecols=COLS, index_col=INDEX_COLS)
    
    mask = dataset.index.get_level_values('Region') == 'РЕПУБЛИКА СРБИЈА'
    serbia = dataset[mask].droplevel('Region')

    years = dataset.index.get_level_values('Year').to_list()
    dataset['Year'] = pd.Categorical(years)

    regions = dataset[~mask].groupby('Region').apply(lambda group: group.droplevel('Region'))

    return regions, serbia



if __name__ == "__main__":
    # quick demo
    regions_df, serbia_df = get_dataset(DATA_FILE)

    if "serbia df demo":
        print(serbia_df.head(), serbia_df.index) # data frame containing data for every year as index for Serbia
        #print(serbia_df.loc[2020].head(7)) # get all cols for year
        print(serbia_df.loc[2012:2015]) # loc[[2012, 2013, 2014, 2015]]
        print("Total tourists in 2020: ", serbia_df.loc[2020, 'TotalTourists'])

    if "regions df demo":
        print(regions_df.head()) # data frame indexed by region and year
        print("Belegrade data all years:\n", regions_df.loc["Београдски регион"].head())
        print("Belegrade data 2014: \n", regions_df.loc["Београдски регион", 2014].head())
        print("Belegrade data for years 2013-2017: \n", regions_df.loc["Београдски регион"].loc[2013:2017]) # can be done with one loc but idk how :)
        print("All regions: ", regions_df.index.unique('Region').to_list())