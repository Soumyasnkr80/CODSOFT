import random
password = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+"
length_password = int(input("Enter the lengthof the password : "))
a = "".join(random.sample(password,length_password))
print(f"Your password is {a}")
