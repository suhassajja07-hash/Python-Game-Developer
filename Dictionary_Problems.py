# #Count the occurence of each vowel in the sentense
# v={"a":0,"e":0,"i":0,"o":0,"u":0}
# sent=input("Write me a sentense please.").lower()
# for c in sent:
#     print(c)
#     if c in v:
#         v[c]=v[c]+1

# print(v)


#counting every letter
v={}
sent=input("Write me a sentense please.").lower()
for c in sent:
    if c.isalpha():
        if c in v:
            v[c]=v[c]+1
        else:
            v[c]=1
print(v)

    





