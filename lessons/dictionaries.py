"""Demostration of dictionary capabilities."""

# declaring a type of dictionary
schools: dict[str, int]
# initialize to an empty dictionary
schools = dict()
# set a key value pairing in dictionary
schools["UNC"] = 19_400
schools["Duke"] = 6717
schools["NCSU"] = 26150
print(schools)
# access a value by its key
print(f"UNC has {schools['UNC']}student")
# remove a key-value from a dictionary by its key
schools.pop("Duke")

# Test for the existence of key
is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")
# Test for the existence of a key
if "Duke" in schools:
    print("found the key 'Duke' in schools")
else: 
    print("no key 'Duke' in schools")

# reassign value to key
schools["UNC"] = 20000
schools["NCSU"] = 16000
print(schools)

# print(schools["UNCC"])
for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")