

temperature = (28, 31, 29, 35, 32, 30, 27, 33, 31, 26)

print("Temperatures from Day 2 to Day 5:")
print(temperature[1:5])

print("Maximum Temperature:", max(temperature))
print("Minimum Temperature:", min(temperature))

count = 0
for temp in temperature:
    if temp > 30:
        count += 1

print("Days above 30°C:", count)

temp_list = list(temperature)
temp_list.append(34)

print("Updated Temperature List:")
print(temp_list)


