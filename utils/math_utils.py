import math
def factorial():
    num=int(input("Enter a number : "))
    print("Factorial :", math.factorial(num))
def compound_interest(p,r,t):
    amount= p * (1+ r/100) **t 
    return amount
def trigonometry():
    angle=float(input("Enter angle in degrees : "))
    rad=math.radians(angle)
    print("Sin :", round(math.sin(rad), 2))
    print("Cos :", round(math.cos(rad), 2))
    print("Tan :", round(math.tan(rad), 2))
def area_circle(r):
    return math.pi*r*r
