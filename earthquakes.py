"""
the eq_data file is a json file that contains detailed information about
earthquakes around the world for a period of a month.

NOTE: No hard-coding allowed except for keys for the dictionaries

1) print out the number of earthquakes

2) iterate through the dictionary and extract the location, magnitude, 
   longitude and latitude of the location and put it in a new
   dictionary, name it 'eq_dict'. We are only interested in earthquakes that have a 
   magnitude > 6. Print out the new dictionary.

3) using the eq_dict dictionary, print out the information as shown below (first three shown):

Location: Northern Mid-Atlantic Ridge
Magnitude: 6.2
Longitude: -36.0923
Latitude: 35.4364


Location: 166km SSE of Muara Siberut, Indonesia
Magnitude: 6.1
Longitude: 100.0208
Latitude: -2.8604


Location: 14km ENE of Puerto Madero, Mexico
Magnitude: 6.6
Longitude: -92.2981
Latitude: 14.7628

"""

import json

infile = open("eq_data.json", "r")
earthquakes = json.load(infile)

# 1 Print out # of earthquakes

print()
print("Total Number of Earthquakes:", earthquakes["metadata"]["count"])
print()


# 2 Print out new dictionary

required_magnitude = 6
eq_dict = {"earthquakes": []}
new_dictionary = {}
eq_features = earthquakes["features"]

for row in range(len(eq_features)):
    if eq_features[row]["properties"]["mag"] > required_magnitude:
        new_dictionary["location"] = eq_features[row]["properties"]["place"]
        new_dictionary["magnitude"] = eq_features[row]["properties"]["mag"]
        new_dictionary["longitude"] = eq_features[row]["geometry"]["coordinates"][0]
        new_dictionary["latitude"] = eq_features[row]["geometry"]["coordinates"][1]
        eq_dict["earthquakes"].append(new_dictionary)

print(eq_dict["earthquakes"])


# 3 Print out formatted info

print()

for row in earthquakes["features"]:
    if row["properties"]["mag"] > required_magnitude:
        print(f"Location: {row['properties']['place']}")
        print(f"Magnitude: {row['properties']['mag']}")
        print(f"Longitude: {row['geometry']['coordinates'][0]}")
        print(f"Latitude: {row['geometry']['coordinates'][1]}")
        print()
