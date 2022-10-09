# Taking data from user
from ast import Num


num = input("Enter Number: ")

# Take input from user only number
while num.isdigit() != True:
    num = input("Input must be Number: ")

# At last printing number enter by user
print(num)
