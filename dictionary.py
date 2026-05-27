CC={"India":"New Delhi","China":"Beijing","Pakistan":"Islamabad","France":"Paris"}
print(CC)
#extracting the keys
print(CC.keys())
#extracting the values
print(CC.values())
#retrieve value using key
print(CC["India"])
#retrieve all items
for i in CC:
    print(i,CC[i])
#add item
CC["Spain"]="Madri"
print(CC)
# update item
CC["Spain"]="Madrid"
print(CC)
#deleting item
del CC["Pakistan"]
print(CC)