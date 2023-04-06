dict={
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four"
}
output=''
cmd= input("Enter number")
for x in cmd:
    output+= dict[x] +' '

print(output)

#use dict.get(x,'!') to not get error with invalid input and get sign instead