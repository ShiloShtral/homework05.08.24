countries = [ {'name': 'Israel', 'population': 9.3, 'birth': 1948},
{'name': 'United States', 'population': 331.9, 'birth': 1776}, {'name': 'Japan',
'population': 125.8, 'birth': 660 }, {'name': 'Australia', 'population': 25.7, 'birth': 1901},
{'name': 'Canada', 'population': 38.0, 'birth': 1867} ]

filtered_countries = list(filter(lambda country: country['population'] > 30, countries))
print(filtered_countries)

#############################################

filtered_countries_by_year = list(filter(lambda country: country['birth'] < 1800, countries ))
print(filtered_countries_by_year)

#############################################

countries_names = list(map(lambda x: x['name'], countries))
print(countries_names)

#############################################

countries_birth = list(map(lambda x: x['birth'], countries))
print(countries_birth)

##############################################

countries.sort(key=lambda country: country['birth'], )
print(countries)

countries.sort(key=lambda population: population['population'])
print(countries)