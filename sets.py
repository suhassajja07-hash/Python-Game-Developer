numbers=[1,2,3,4,1,7,6,9,6,]
new_numbers=set(numbers)
print(new_numbers)
print(type(new_numbers))
#adding to sets
new_numbers.add(0)
print(new_numbers)
#removing items
new_numbers.remove(0)
print(new_numbers)
#new_numbers.remove(0)
#discarding
new_numbers.discard(0)
new_numbers.discard(6)
print(new_numbers)
#creating sets
fruits={"apple","banana","strawberrry","lemon","grape","lime"}
citrus_fruits={"lemon","lime","orange","grapefruit"}
#union
print(fruits.union(citrus_fruits))
print(fruits|citrus_fruits)
#intersection
print(fruits.intersection(citrus_fruits))
print(fruits & citrus_fruits)
#difference
print(fruits.difference(citrus_fruits))
print(fruits-citrus_fruits)
#symmetric difference
print(fruits.symmetric_difference(citrus_fruits))
print(fruits^citrus_fruits)