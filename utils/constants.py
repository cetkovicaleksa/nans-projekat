DATA_FILE = 'data\main-table.csv'
EXTRAPOLATED_DATA_FILE = 'data\extrapolated_data.csv'

COLS = (
    'Region', 'Year', 'TotalTourists', 'ForeignTourists', 'HousesWithInternet%',
    'CompaniesWithWebSites%', 'AmountOfPeopleWithHighEducation',
    'PeopleWithHighEducationWithoutJob', 'AmountOfPeopleWithSecondaryEducation',
    'PeopleWithSecondaryEducationWithoutJob', 'AmountOfPeopleWithoutEducation',
    'PeopleWithoutEducationWithoutJob', 'AmountOfMales',
    'AmountOfMalesWithoutJob', 'AmountOfFemales',
    'AmountOfFemalesWithoutJob', 'AmountOfPeopleInRegion',
    'AmountOfPeopleInRegionWithoutJob', 'AmountOf_15-24_PeopleInRegion',
    'AmountOf_15-24_PeopleInRegionWithoutJob', 'AmountOf_15-64_PeopleInRegion',
    'AmountOf_15-64_PeopleInRegionWithoutJob', 'AmountOf_25-34_PeopleInRegion',
    'AmountOf_25-34_PeopleInRegionWithoutJob', 'AmountOf_35-44_PeopleInRegion',
    'AmountOf_35-44_PeopleInRegionWithoutJob', 'AmountOf_45-54_PeopleInRegion',
    'AmountOf_45-54_PeopleInRegionWithoutJob', 'AmountOf_55-64_PeopleInRegion',
    'AmountOf_55-64_PeopleInRegionWithoutJob', 'AmountOf_65+_PeopleInRegion'
)

DEPENDENT_COL = 'TotalTourists'

INDEX_COLS = 'Region', 'Year'

INDEPENDENT_COLS = tuple( set(COLS) - set(INDEX_COLS) - {DEPENDENT_COL} )

REGIONS = ( 
    'РЕПУБЛИКА СРБИЈА',
    'Београдски регион', 
    'Регион Војводине', 
    'Регион Шумадије и Западне Србије', 
    'Регион Јужне и Источне Србије' 
)