import random
import os

def numb():
 number=random.randint(1,100)
 return number


def play():
 print("""\n\n\n\n\n
 ________  ___  ___  _______   ________   ________           ________   ___  ___  _____ ______   ________  _______   ________     
|\   ____\|\  \|\  \|\  ___ \ |\   ____\ |\   ____\         |\   ___  \|\  \|\  \|\   _ \  _   \|\   __  \|\  ___ \ |\   __  \    
\ \  \___|\ \  \\\  \ \   __/|\ \  \___|_\ \  \___|_        \ \  \\ \  \ \  \\\  \ \  \\\__\ \  \ \  \|\ /\ \   __/|\ \  \|\  \   
 \ \  \  __\ \  \\\  \ \  \_|/_\ \_____  \\ \_____  \        \ \  \\ \  \ \  \\\  \ \  \\|__| \  \ \   __  \ \  \_|/_\ \   _  _\  
  \ \  \|\  \ \  \\\  \ \  \_|\ \|____|\  \\|____|\  \        \ \  \\ \  \ \  \\\  \ \  \    \ \  \ \  \|\  \ \  \_|\ \ \  \\  \| 
   \ \_______\ \_______\ \_______\____\_\  \ ____\_\  \        \ \__\\ \__\ \_______\ \__\    \ \__\ \_______\ \_______\ \__\\ _\ 
    \|_______|\|_______|\|_______|\_________\\_________\        \|__| \|__|\|_______|\|__|     \|__|\|_______|\|_______|\|__|\|__|
                                 \|_________\|_________|                                                                          
                                                                                                                                  
                                                                                                                                    
                                                                                                                                                                                     
 """)
 a=input("Enter Difficulty Easy or Hard : ")
 d=numb()
 if a=="Easy":
     i=10 
     while i>=0:
        n=int(input("Enter your Guess : " )   )
        i-=1
        if n>d :
            print("Too High ! \n\n")
        elif n<d:
            print("Too Low ! \n\n")
        elif n==d:
            print("You Got it ")
            break
     if i==0:
        print(f"You Lost \n The number is : {d}")


 elif a=="Hard":
     i=5
     while i>=0:
        n=int(input("Enter your Guess : " )   )
        i-=1
        if n>d :
            print("Too High ! \n\n")
        elif n<d:
            print("Too Low ! \n\n")
        elif n==d:
            print("You Got it ")
            break
     if i==0:
        print(f"You Lost \n The number is : {d}")


play()