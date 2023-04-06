import random
import os

dict=["lust" , "greed" , "pride" , "sloth" , "rage" , "envy" , "gluttony"]
word=random.choice(dict)
guess=[]
for x in word:
    guess+="_"

life=6
eol= False

while life!=0 and not eol:
    os.system("clear")
    for x in guess:
        print(x, end = " ")
    print("\n\n")

    a=input("Guess a Alphabet : ")
    i=0
    b=False
    while i<len(word):
        if word[i]==a:
            guess[i]=a
            b=True
        
        i+=1

    if b!=True:
        life-=1
        if life==0:
            print(f"\nYou Lost \n The word is : {word}")
            print("\n\nGame Over")
            break
    
    if "_" not in guess:
        eol=True
        os.system("clear")
        print(f"{word}\n\n You Won ")
  





