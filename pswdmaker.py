import random

letters =["a","A","v","S","s","q","W", "z", "G"] 
symbols=["!","@","#","$","%","^"]

pl= int(input("Enter password length :"))
n=int(input("numbers : "))
s=int(input("symbols : "))
pswd=""

for x in range(0,pl-s):
    pswd+= random.choice(letters)

for x in  range(0,n):
    pswd+= random.choice(symbols)



print(pswd)

