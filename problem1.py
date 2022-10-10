"""
Author: Victer Phiathep
RUID : 179005525
Module for Problem 1, Homework 2
Object Oriented Programming (50:198:113), Fall 2022

This module contains functions to manipulate polynomials. 
"""

# INSERT ALL FUNCTION IMPLEMENTATIONS HERE
def read_polynomial(filename):
    """
        This function converts our text file into a dictionary
        where the key:value pair is the term and the exponent.
    """
    
    file = open(filename, "r")
    data = file.readlines()
    numbers = []
    poly_dict = {}

    for line in data:
        nums = list(map(int, line.split(" ")))
        numbers.append(nums)

    numbers.sort()                          # Sort our terms by highest degree
    numbers.reverse()                       # Reverse for highest to least.

    # Transfer polynomials to dictionary
    for num in numbers:
        poly_dict[num[0]] = num[1]
    file.close()

    return poly_dict


def print_polynomial(P):
    """
        This function converts our dictionary into a readable polynomial string.
    """

    polynomial = ""

    # Find a way to sort our polynomial  by exponent
    index = 0
    for term, coeff in P.items():
        if term > 1 and coeff > 1: 
            if index > 0:
                polynomial += f" + {coeff}x^{term}"
            else:
                polynomial += f"{coeff}x^{term}"
        elif term > 1 and coeff < -1:
                # Index will check if the polynomial is the first number
            if index > 0:
                polynomial += f" - {abs(coeff)}x^{term}"
            else:
                polynomial += f"-{abs(coeff)}x^{term}"

        # For coefficient with no exponents
        elif term == 1:
            if coeff > 1: # Number is positive
                polynomial += f" + {coeff}x"
            elif coeff == 1:
                polynomial += f" + x "
            elif coeff <= -1: # Negative number
                polynomial += f" - {abs(coeff)}x"
        
        else:
            if coeff > 0:
                polynomial += f" + {coeff}"
            else:
                polynomial += f" - {coeff}"

        index += 1
            

    # Remove trailing + signs and print
    #print(polynomial.strip(" + "))
    print(polynomial)


def degree(P):
    """
        Function returns the highest degree term in our polynomial.
    """
    degree = list(P.keys())[0]
    return degree


def eval_polynomial(P, X):
    """
        Takes in a polynomial and an "x" value. Function will solve the polynomial with the given x value.
    """
    
    result = 0
    for term, coeff in P.items():
        if term > 1:
            result += coeff * (X**term)
        else:
            result += coeff
    return result


def addterm(P, exp, coeff):
    """
        Function will take a new coeff and exponent and add the 
        new coefficient and exponent to our polynomial while keeping 
        the dictionary in order by terms
    """

    # Creating a new dictionary for our new polynomial
    new_dict = {}

    for key, val in P.items():
        # Once we find the correct positioning of our added term, add it into our polynomial before the next
        if key < exp:
            new_dict[exp] = coeff
            new_dict[key] = val
        elif key == exp:
            new_dict[exp] = (P[exp]+coeff)
        else:
            new_dict[key] = val
    return new_dict



def removeterm(P, exp):
    """
        This function will remove the exponent if it exists as a key value pair
    """
    if exp in P:
        del P[exp]        


def scale_polynomial(P1, s):
    """
        The function will take in a polynomial dictionary (P1), 
        and multiply the coefficients (value pairs) by two
    """

    sP = {}
    # Loop through our dictionary and mutliply the value by two
    for key in P1:
        sP[key] = P1[key]*2

    return sP



def sum_polynomial(P1, P2):
    """
        This function will create a new dictionary of the two polynomials 
        passed in added together
    """

    sum_poly = P1
    for term, coeff in P2.items():
            sum_poly = addterm(sum_poly,term, coeff)

    return sum_poly

def diff_polynomial(P1, P2):
    """This function creates a new polynomial that is the difference of the two polynomials
    passed into the function.
    """
    diff_poly = P1

    for term, coeff in P2.items():
            diff_poly = addterm(diff_poly, term, coeff*-1)            
    return diff_poly
    
    


def prod_polynomial(P1, P2):
    """
        Takes in two polynomials inside a dictionary and multiplies them together into a new
        polynomial inside a dictionary.
    """
    
    prod_poly = {}

    #Loop through each term and multiply it by each term in the second polynomial
    for key, val in P1.items():
        for term, coeff in P2.items():
            new_term = term + key
            new_coeff = coeff * val
            if new_term in prod_poly:
                prod_poly[new_term] += new_coeff
            else:
                prod_poly[new_term] = new_coeff
    
    return prod_poly
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
        #filename = "poly1.txt"
        P1 = read_polynomial(filename)
        print("The first polynomial has been read, printed below: ")
        print_polynomial(P1)
        print(" ")
        filename = input("Enter the name of the second file: ")
        #filename = "poly2.txt"
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
        print("The first polynomial evaluated at x = 0 gives ",
              eval_polynomial(P1, 0))
        print("The first polynomial evaluated at x = 2 gives ",
              eval_polynomial(P1, 2))
        print("The first polynomial evaluated at x = -1 gives ",
              eval_polynomial(P1, -1))

        print(" ")
        dummy = input("Hit enter key to continue.")
        print(" ")
        print("                  ------------------------------")
        print("                   Testing addterm, removeterm  ")
        print("                  ------------------------------")
        print("I am adding the term 6x^5 to the first polynomial.")
        P1 = addterm(P1, 5, 6)
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




if __name__ == "__main__":
    testPolynomials()