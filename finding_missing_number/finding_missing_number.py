import random

HOW_MANY_NUMBERS = 100

sneaky_array = [None] * HOW_MANY_NUMBERS
comparing = [None] * HOW_MANY_NUMBERS
missing_number = 0

x = 0

for i in range(HOW_MANY_NUMBERS):
    comparing[i] = i
    sneaky_array[i] = i

random_number = random.randint(0, HOW_MANY_NUMBERS)

sneaky_array.pop(random_number)
random_number = comparing[random_number]
print(random_number)
for i in range(len(comparing)):
    #print(f"{comparing[i]} {sneaky_array[i]}")
    if comparing[i] != sneaky_array[i]:
        print
        missing_number = comparing[i]
        break

print(missing_number)