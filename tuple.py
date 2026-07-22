adress=(6,"warbler view","sutton courtenay","uk","rg29bx")
print(adress)
print(type(adress))
print(adress[1])
for i in adress:
    print(i)

#unpacking
numbers=(7,0)
n1,n2=numbers
print(n1)
print(n2)
#one item tuple
shops=("aldi",)
print(type(shops))
print(len(shops))


shops.append("animal")
