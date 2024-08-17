import random, turtle

def create_turtle1():
    turtle1 = turtle.Turtle()
    turtle1.color("green")
    turtle1.setheading(0) 
    return turtle1

def move(turtle1, turtle2):
    dist = random.randrange(10, 10)
    turtle1.forward(dist)
    turtle2.forward(dist)
def main():
   t1 =  create_turtle1()
   num = random.randrange(20)
   
   for i in range(num):
       move(t1,t2)
       