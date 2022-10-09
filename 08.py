# Calculating simple interest
# Taking principal,time and rate from user

principal = int(input("Enter Principal: "))
time = int(input("Enter Time: "))
rate = int(input("Enter Rate: "))

# Formula for simple interest
simple_interest = (principal*time*rate)/100

print("Simple Interest: ", simple_interest)
