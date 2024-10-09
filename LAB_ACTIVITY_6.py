"""
Write a Python program that calculates the registration fee for a fitness class based on the following criteria:

1.) If the attendee is "under 18 years old":
    a.) If the attendee is a Member, the fee is 450.00 pesos.
    b.) If the attendee is is a Non-member, the fee is 650.00 pesos.

2.) If the attendee is "between 18 and 65 years old":
    a.) If the attendee is a Member, the fee is 550.00 pesos.
    b.) If the attendee is is a Non-member, the fee is 750.00 pesos.
    
2.) If the attendee is "over 65 years old":
    a.) If the attendee is a Member, the fee is 400.00 pesos.
    b.) If the attendee is is a Non-member, the fee is 600.00 pesos.
"""


# Identification and inputting of personal information of the attendee

print("Hello and welcome dear citizen, please state your age and clarify that if you are a member for the registration of this fitness class.")
age = float(input("Kindly state your age: "))
is_a_member = input("Are you a Member (yes or no)? ")


# Analytical Calculation of the requirements of the fitness class based on the attendee's personal information

if age < 18:
    if is_a_member == "yes":
        print("The registration fee for the fitness class is 450.00 pesos.")
    else:
        print("The registration fee for the fitness class is 650.00 pesos.")
        
elif age >= 18 and age <= 65:
    if is_a_member == "yes":
        print("The registration fee for the fitness class is 550.00 pesos.")
    else:
        print("The registration fee for the fitness class is 750.00 pesos.")

elif age > 65 and age < 100:
    if is_a_member == "yes":
        print("The registration fee for the fitness class is 400.00 pesos.")
    else:
        print("The registration fee for the fitness class is 600.00 pesos.")

# The inputted data is invalid or does not meet the requirements of the personal information required

else:
    print("Invalid age. Please enter a valid age.")


# Verification of the attendee's payment and registration fee
 
print("Please pay up to the registration fee.")
input()