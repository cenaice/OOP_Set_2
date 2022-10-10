"""
Author: Victer Phiathep
RUID : 179005525
Module for Problem 2, Homework 2
Object Oriented Programming (50:198:113), Fall 2022

This module contains functions to compare files for cosine similarity. 
"""



from math import sqrt


def freq_dictionary(infile):
    """
        Takes a text file and creates a dictionary with key-value pairs
        with the number of appearances of a word.
    """

    file = open(infile, 'r')
    data = file.read()
    freq_dict = {}

    for word in data.split():
        word = word.lower()
        word_in = ""

        # Removes any characters that are not alphabetical in our word
        for let in word:
            if let.isalpha() == False:
                break
            else:
                word_in += let

        # Check for word occurence in dictionary
        if word_in not in freq_dict:
            freq_dict[word_in] = 1
        else:
            freq_dict[word_in] += 1

    file.close()
    
    return freq_dict



def cosine_similarity(docfile1, docfile2):
    """
        Takes two text files, creates a dictionary of word frequencies,
        and finds the cosine similarity of the two.
    """
    # Open both files for reading inside our freq_dictionary function
    file_1_dict = freq_dictionary(docfile1)
    file_2_dict = freq_dictionary(docfile2)

    cosine_sum = 0
    for key, val in file_1_dict.items():
        if key in file_2_dict:
            cosine_sum += (file_1_dict[key] * file_2_dict[key])


    # Created a function to find the sqrt of a-nth^2/b-nth^2
    def cosine_root(file_dict):
        val = 0
        for item in file_dict:
            val += file_dict[item]**2
        return sqrt(val)

    a = cosine_root(file_1_dict)
    b = cosine_root(file_2_dict)




    # Plug in final formula values, rounding to remove floating point 
    ans = cosine_sum / round((a * b),4)
    return ans


freq_dictionary("doc3.txt")
print(cosine_similarity("doc1.txt","doc2.txt"))
