import random 
import string
def random_number():
    print("Random Number :", random.randint(1,100))
def random_list():
    lst=[random.randint(1,20) for _ in range(5)]
    print("Random List :", lst)
def random_password():
    length=int(input("Enter password length : "))
    chars=string.ascii_letters+string.digits+"!@#$"
    password=""
    for _ in range(length):
        password+=random.choice(chars)
    print("Generated Password :", password)
def random_otp():
    otp=random.randint(100000, 999999)
    print("Generated OTP :", otp)
