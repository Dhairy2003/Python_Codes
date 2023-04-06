import random
random.seed(1)


names= input("Enter names : ")
lst= names.split(',')

choice= lst[random.randint(0,len(lst)-1)]

print(f"{choice} is going to pay the bill")