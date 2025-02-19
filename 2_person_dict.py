person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person)

# print out the name of the second child
print(person["children"][1])
print(person["children"][1])

# print out the name of the cat
print(type(person["pets"]))
print(person["pets"]["cat"])

# iterate through all children and print out each child
for i in person["children"]:
    print(i)

# print out the pets in this format
# type of pet: dog name of pet: Fido
for i, j in person["pets"].items():
    print("Type of pet:"), (i), ("name of pet:", (j))
