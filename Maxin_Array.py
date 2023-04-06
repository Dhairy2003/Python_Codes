numbers=[1,2,3,4,5,1,22,12,3,4]
max=numbers[0]
for x in range(len(numbers)):
    if numbers[x] >max:
        max=numbers[x]

print(max)