import copy

israel_info = {
    "name": "Israel",
    "birth": 1948,
    "population_millions": 9.3,
    "capital": "Jerusalem",
    "language": "Hebrew",
    "cities": ["Jerusalem", "Tel Aviv", "Haifa", "Rishon LeZion", "Petah Tikva", "Ashdod"],
    "currency": "ILS",
    "area_Kilometer": 22_145,
    "gdp_billion": 450
}

print(israel_info.get("capital"))
##################################
print(israel_info.keys())
##################################
upper_israel_info = [key.upper() for key in israel_info.keys()]
print(upper_israel_info)
##################################
print(israel_info.values())
##################################
len_israel_info_values = [len(str(value)) for value in israel_info.values()]
print(len_israel_info_values)
#################################
for key, value in israel_info.items():
    print(f"{key}: {value}")
#################################
israel_info_copy = israel_info.copy()
print(israel_info_copy)
#################################
israel_info_copy.clear()
print(israel_info_copy)
#################################
none_values_dict = dict.fromkeys(israel_info.keys(), None)
print(none_values_dict)
#################################
del none_values_dict['currency']
#################################
none_values_dict.pop('area_Kilometer')
#################################
none_values_dict.update([
    ('National sport', 'Soccer'),
    ('population_millions', 9.4)
])
print(none_values_dict)