def hello():
    return "Hello World!"

def greet_me(a, b):
    return a + ' says ' + b + '!'

def say_hello(name):
    return 'Hi, ' + name + ' how are you doing today?'

def greetings(a, b, c):
    return a, b, c

def greet_all(greet):
    for i in greet:
        print (i)
    return

greet = greetings(hello(), say_hello('every-one'), greet_me('Ongebo', 'good-morning my friends'))

print(greetings(hello(), say_hello('Innocent'), greet_me('Ongebo', 'good-morning friend')))

greet_all(greet)