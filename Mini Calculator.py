                                             #Mini Calculator


""""GOAL : Let the user enter two numbers and choose the operation and then return the result,
          remember this mini calculator is like a pocket calculator for basic operations only, 
          so make it simple and user friendly """


def calculator() :
    print("MINI CALCULATOR")

calculator()

NUMBER1 = float(input("Enter your first number here :"))

operation = input("choose any of the operations +,-,*,/ :")

NUMBER2 = float(input("Enter your first number here :"))

if operation == '+':
    print("Result:", NUMBER1 + NUMBER2)

elif operation == '-':
    print("Result:",NUMBER1 - NUMBER2)

elif operation == '*':
    print("Result:", NUMBER1 * NUMBER2)

elif operation == '/':
    if NUMBER2!= 0:
        print("Result : ", NUMBER1 / NUMBER2)
    else :
        print("ERROR ")

else :
    print("Invalid operator")



