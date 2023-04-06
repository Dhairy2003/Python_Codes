dict={
    "dhairy":"123",
    "smarth":"345"
}

def auth(fun):
    def ver(username, pswd, *args, **kwargs):
        if username in dict and dict[username]==pswd:
            fun(*args,**kwargs)
        else :
            print("Access denied")
    return ver

def add( a, b):
    print(a+b)

locked = auth(add)
locked("dhairy", "13", 1, 2)

