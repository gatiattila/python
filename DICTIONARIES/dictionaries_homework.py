country_name = [
    'Belgium',
    'Bulgaria',
    'Czechia',
    'Denmark',
    'Germany',
    'Estonia',
    'Ireland',
    'Greece',
    'Spain',
    'France',
    'Croatia',
    'Italy',
    'Cyprus',
    'Latvia',
    'Lithuania',
    'Luxembourg',
    'Hungary',
    'Malta',
    'Netherlands',
    'Austria',
    'Poland',
    'Portugal',
    'Romania',
    'Slovenia',
    'Slovakia',
    'Finland',
    'Sweden',
    'United Kingdom',
    'Iceland',
    'Norway',
    'Switzerland',
    'Montenegro',
    'North Macedonia',
    'Serbia',
    'Turkey']
raw_data = [
    ('Belgium',2017,'M',33.1),
    ('Bulgaria',2017,'M',24.4),
    ('Czechia',2017,'M',22.8),
    ('Denmark',2017,'M',26.8),
    ('Germany',2017,'M',19.8),
    ('Estonia',2017,'M',10.6),
    ('Ireland',2017,'M',44.5),
    ('Greece',2017,'M',47.4),
    ('Spain',2017,'M',20.5),
    ('France',2017,'M',26.3),
    ('Croatia',2017,'M',30.8),
    ('Italy',2017,'M',15.1),
    ('Cyprus',2017,'M',50.5),
    ('Latvia',2017,'M',4.3),
    ('Lithuania',2017,'M',9.1),
    ('Luxembourg',2017,'M',24.9),
    ('Hungary',2017,'M',20.4),
    ('Malta',2017,'M',30.6),
    ('Netherlands',2017,'M',24.6),
    ('Austria',2017,'M',33.5),
    ('Poland',2017,'M',18.4),
    ('Portugal',2017,'M',12.2),
    ('Romania',2017,'M',31.5),
    ('Slovenia',2017,'M',23.8),
    ('Slovakia',2017,'M',25.7),
    ('Finland',2017,'M',20.2),
    ('Sweden',2017,'M',30.2),
    ('United Kingdom',2017,'M',37),
    ('Iceland',2017,'M',42),
    ('Norway',2017,'M',27.9),
    ('Switzerland',2017,'M',37.5),
    ('Montenegro',2017,'M',44),
    ('North Macedonia',2017,'M',29.6),
    ('Serbia',2017,'M',21),
    ('Turkey',2017,'M',6.6),
    ('Belgium',2018,'M',30.4),
    ('Bulgaria',2018,'M',22.2),
    ('Czechia',2018,'M',22.1),
    ('Denmark',2018,'M',27.2),
    ('Germany',2018,'M',18.5),
    ('Estonia',2018,'M',9.3),
    ('Ireland',2018,'M',45.7),
    ('Greece',2018,'M',48.1),
    ('Spain',2018,'M',24.1),
    ('France',2018,'M',24.3),
    ('Croatia',2018,'M',31.2),
    ('Italy',2018,'M',16.4),
    ('Cyprus',2018,'M',47.9),
    ('Latvia',2018,'M',6.8),
    ('Lithuania',2018,'M',9),
    ('Luxembourg',2018,'M',23.8),
    ('Hungary',2018,'M',18.5),
    ('Malta',2018,'M',26.3),
    ('Netherlands',2018,'M',26.9),
    ('Austria',2018,'M',32.8),
    ('Poland',2018,'M',16.9),
    ('Portugal',2018,'M',11),
    ('Romania',2018,'M',30.2),
    ('Slovenia',2018,'M',23.1),
    ('Slovakia',2018,'M',24.4),
    ('Finland',2018,'M',19.4),
    ('Sweden',2018,'M',31.7),
    ('United Kingdom',2018,'M',34),
    ('Iceland',2018,'M',0),
    ('Norway',2018,'M',28.8),
    ('Switzerland',2018,'M',36.8),
    ('Montenegro',2018,'M',0),
    ('North Macedonia',2018,'M',31.2),
    ('Serbia',2018,'M',22.6),
    ('Turkey',2018,'M',7.6),
    ('Belgium',2017,'F',28.5),
    ('Bulgaria',2017,'F',19.1),
    ('Czechia',2017,'F',18.4),
    ('Denmark',2017,'F',24.4),
    ('Germany',2017,'F',17.3),
    ('Estonia',2017,'F',11.3),
    ('Ireland',2017,'F',44.8),
    ('Greece',2017,'F',42.8),
    ('Spain',2017,'F',17.7),
    ('France',2017,'F',22.4),
    ('Croatia',2017,'F',25.5),
    ('Italy',2017,'F',12.2),
    ('Cyprus',2017,'F',48.7),
    ('Latvia',2017,'F',2.8),
    ('Lithuania',2017,'F',6.2),
    ('Luxembourg',2017,'F',22.1),
    ('Hungary',2017,'F',14.1),
    ('Malta',2017,'F',26.4),
    ('Netherlands',2017,'F',20.1),
    ('Austria',2017,'F',31.7),
    ('Poland',2017,'F',14.5),
    ('Portugal',2017,'F',8.9),
    ('Romania',2017,'F',24.4),
    ('Slovenia',2017,'F',19),
    ('Slovakia',2017,'F',20.9),
    ('Finland',2017,'F',19.2),
    ('Sweden',2017,'F',27.7),
    ('United Kingdom',2017,'F',33.8),
    ('Iceland',2017,'F',36.2),
    ('Norway',2017,'F',28.5),
    ('Switzerland',2017,'F',32.6),
    ('Montenegro',2017,'F',35.8),
    ('North Macedonia',2017,'F',25),
    ('Serbia',2017,'F',16.1),
    ('Turkey',2017,'F',4.5),
    ('Belgium',2018,'F',26.5),
    ('Bulgaria',2018,'F',17.1),
    ('Czechia',2018,'F',18.2),
    ('Denmark',2018,'F',24.7),
    ('Germany',2018,'F',17.3),
    ('Estonia',2018,'F',8.4),
    ('Ireland',2018,'F',45.5),
    ('Greece',2018,'F',44.1),
    ('Spain',2018,'F',21.1),
    ('France',2018,'F',21.7),
    ('Croatia',2018,'F',26.2),
    ('Italy',2018,'F',13.6),
    ('Cyprus',2018,'F',45.3),
    ('Latvia',2018,'F',4.4),
    ('Lithuania',2018,'F',5.7),
    ('Luxembourg',2018,'F',23.3),
    ('Hungary',2018,'F',14.1),
    ('Malta',2018,'F',22.5),
    ('Netherlands',2018,'F',20.2),
    ('Austria',2018,'F',31.1),
    ('Poland',2018,'F',14.2),
    ('Portugal',2018,'F',8.6),
    ('Romania',2018,'F',22.9),
    ('Slovenia',2018,'F',17.2),
    ('Slovakia',2018,'F',20.1),
    ('Finland',2018,'F',16.5),
    ('Sweden',2018,'F',26.7),
    ('United Kingdom',2018,'F',32.5),
    ('Iceland',2018,'F',0),
    ('Norway',2018,'F',27.4),
    ('Switzerland',2018,'F',33.7),
    ('Montenegro',2018,'F',0),
    ('North Macedonia',2018,'F',27.2),
    ('Serbia',2018,'F',19.5),
    ('Turkey',2018,'F',5.3)]


health_index_2017 = {
    country: [sex, health_index]
    for country, year, sex, health_index in raw_data if year == 2017
}
health_index_2018 = {
    country: [sex, health_index]
    for country, year, sex, health_index in raw_data if year == 2018
}

print(health_index_2017)
print(health_index_2018)

germany = {
    year: [sex, health_index]
    for country, year, sex, health_index in raw_data if country == 'Germany'
}

print(germany)

health_index_dict = {
    str(country)+"_"+str(year): [year, sex, health_index]
    for country, year, sex, health_index in raw_data
}

print(health_index_dict)
#starting from the previous health_index dict, display only the data where the health_index >5
for element in health_index_dict:
   if health_index_dict[element][2] > 5:
       print(element, health_index_dict[element])

#starting from the previous health_index dict, display only the data where the health_index >5 and sex is ‘F’
for element in health_index_dict:
   if health_index_dict[element][2] > 5 and health_index_dict[element][1] == 'F':
       print(element, health_index_dict[element])

#starting from the previous health_index dict, create a for loop to print the health_index
for element in health_index_dict:
   print(health_index_dict[element][2])