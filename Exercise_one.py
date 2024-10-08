# The volume of a sphere with radius r is (4/3)* pie * r**2.
# What is the volume of the sphere with radius 5.
# Make sure the program enters the  radius from the keyboard and provide the answer in 2 decimal places.
radius = float(input("Enter the radius: "))
pie = (22/7)
volume_of_sphere = (4/3) * pie * radius**2.
print(f"The volume of the sphere is {volume_of_sphere:.2f}")

# Create a program to calculate the area of a traingle (1/2 * base * height).
# Base and height should be entered using the keyboard.
base = int(input("Enter the base: "))
height = int(input("Enter the height: "))
area_of_triangle = (1/2 * base * height)
print(f"The area of a triangle is {area_of_triangle:.2f} ")
# Question One 
# WITI has tasked you to automate a simple grading system.
# As a python student, write a program using to display the grades that
# the students will be receiving based on the mark scored in a subject.
# The grades are :
# 90%- 100% Grade is A
# 80% - 89%  Grade is B
# 70% - 79% Grade is C
# 60% - 69% Grade is D
# 50% - 59% Grade is E
# <50% Fail

score = int(input("Enter the student's score "))
if 90<= score <=100:
    print("A")
elif 80<= score <=89:
    print("B")
elif 70<= score <=79:
    print("C")
elif 60<=score <=69:
    print("D")
elif 50<= score <=59:
    print("E")
else:
    print("Fail")


# WITI Academy is proposing a Sacco to help students save their money.
# Design a platform that will do the following.
# Welcome to , WITIAcademy Sacco.
# 1. Deposit Money
# 2. Withdraw Money# 3. Check balance
# Ensure if the student selects 1, money is deposited and the minimum deposit should be 1000.
#  If the student selsects 2,money should be withdrawn and a minumum withdrawal is 500.
# If the student selects 3, the account balance should be displayed.

initial_balance = 0
print("Welcome to WITI Academy Sacco.")
print("1.Deposit Money")
print("2.Withdrawa Money")
print("3.Check Balane")

choice = int(input("Select option (1/2/3: "))
if choice == 1:
    amount = int(input("Enter amount to deposit: "))
    if amount >= 1000:
        initial_balance =+ amount
        print(f"Successfully deposited {amount}. New baalance is {initial_balance}")
    else:
        print("Minimum deposit is 1000")
elif choice == 2:
      amount = int(input("Enter amount to withdraw: "))
      if amount >= 500:
        if initial_balance >= amount:
           initial_balance -= amount
           print(f"Sucessfully withdrawn {amount}. New balance is {initial_balance}")
        else:
          print("Insufficient balance.")
      else:
        print("Minimum withdraw")
elif choice == 3:
     print(f"Current balance is {initial_balance}.")
else:
      print("Invalid request.")


    
    