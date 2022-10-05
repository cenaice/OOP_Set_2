"""
Author: Victer Phiathep
RUID : 179005525
Module for Problem 1, Homework 2
Object Oriented Programming (50:198:113), Fall 2022

This module contains functions to manipulate polynomials. 
"""

# INSERT ALL FUNCTION IMPLEMENTATIONS HERE
# Document all functions 

def testPolynomials():
    answer = "y"
    while (answer[0].lower() == "y"):
        print("                  ------------------------------")
        print("                   Testing Polynomial Functions ")
        print("                  ------------------------------")
        print(" ")
        print("I will first create two polynomials. You will")
        print("be asked to provide the names of the files   ")
        print("containing the polynomial data.")
        print(" ")
        filename = input("Enter the name of the first file: ")
        P1 = read_polynomial(filename)
        print("The first polynomial has been read, printed below: ")
        print_polynomial(P1)
        print(" ")
        filename = input("Enter the name of the second file: ")
        P2 = read_polynomial(filename)
        print("The second polynomial has been read, printed below: ")
        print_polynomial(P2)
        print(" ")
        print("Each of the remaining function implementations will")
        print("now be tested. Check the output to make sure that ")
        print("your function is producing the correct answer.")

        print(" ")
        dummy = input("Hit enter key to continue.")
        print(" ")
        print("                  ------------------------------")
        print("                  Testing degree, eval_polynomial")
        print("                  ------------------------------")
        print("The degree of the first polynomial is ", degree(P1))
        print("The first polynomial evaluated at x = 0 gives ", eva_polynomial(P1, 0))
        print("The first polynomial evaluated at x = 2 gives ", eval_polynomial(P1, 2))
        print("The first polynomial evaluated at x = -1 gives ", eval_polynomial(P1, -1))

        print(" ")
        dummy = input("Hit enter key to continue.")
        print(" ")
        print("                  ------------------------------")
        print("                   Testing addterm, removeterm  ")
        print("                  ------------------------------")
        print("I am adding the term 6x^5 to the first polynomial.")
        addterm(P1, 5, 6)
        print("The first polynomial is now: ")
        print_polynomial(P1)
        print("I am removing the term with exponent 5 from the first polynomial.")
        removeterm(P1, 5)
        print("The first polynomial is now: ")
        print_polynomial(P1)

        print(" ")
        dummy = input("Hit enter key to continue.")
        print(" ")
        print("                  ------------------------------")
        print("                     Testing scalePolynomial    ")
        print("                  ------------------------------")    
        sP = scale_polynomial(P1, 2)
        print("The first polynomial scaled by 2 is as follows:")
        print_polynomial(sP)

        print(" ")
        dummy = input("Hit the enter key to continue.")
        print(" ")
        print("                  ------------------------------")
        print("                       Testing sumPolynomial    ")
        print("                  ------------------------------")
        sum = sum_polynomial(P1, P2)
        print("(Sum) first polynomial + second polynomial equals: ")
        print_polynomial(sum)
        
        print(" ")
        dummy = input("Hit enter key to continue.")
        print(" ")
        print("                  ------------------------------")
        print("                      Testing diffPolynomial    ")
        print("                  ------------------------------")
        diff = diff_polynomial(P1, P2)
        print("(Difference) first polynomial - second polynomial equals: ")
        print_polynomial(diff)
        
        print(" ")
        dummy = input("Hit enter key to continue.")
        print(" ")
        print("                  ------------------------------")
        print("                      Testing prodPolynomial    ")
        print("                  ------------------------------")    
        prod = prod_polynomial(P1, P2)
        print("(Product) first polynomial * second polynomial equals: ")
        print_polynomial(prod)

        print(" ")
        answer = input("Run the tests again? [y/n] ")
    
    print("Goodbye!!")


def read_polynomial(filename):
    """
    This function converts our text file into a dictionary
    where the key:value pair is the term and the exponent.
    """
    # To open and read filename (poly1, poly2)

    poly_dict = {}
    
    file = open(filename, "r")
    data = file.readlines()

    # to sort data before reading
    for line in data:
        
        nums = line.split()
        print(nums)
        poly_dict[int(nums[0])] = int(nums[1])

        

    file.close()    

    return poly_dict

def print_polynomial(P):
    """This function converts our dictionary into a readable polynomial."""
    polynomial = ""
    print(P)

    # Find a way to sort our polynomial by exponent

    for key, val in P.items():
        if key or val != 0:
            polynomial += f"{val}x^{key} + "
        elif key == 1:
            polynomial += f"{val}x + "
        else:
            polynomial += f"{val} + "

    # Remove trailing + signs and print        
    print(polynomial.strip(" + "))

def degree(P):
    # Print the key of the first item in our sorted dictionary
    degree = list(P.keys())[0]
    return degree
    
def eva_polynomial(P, X):
    # function should evaluate P at x = x and return result
    for key, val in P.items():
        pass
def addterm(P, exp, coeff):
    pass

def removeterm(P,exp):
    pass

def scale_polynomial(P1, P2):

    pass

def sum_polynomial(P1, P2):
    pass

def diff_polynomial(P1, P2):
    pass

def prod_polynomial(P1, P2):
    pass



if __name__ == "__main__":
    testPolynomials()
