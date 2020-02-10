#!/usr/bin/python

"""
Python Core object Types
"""

import math

def numbers_and_strings():
    """
    This is to review numbers and strings and basic operations.
    """
    # Assign a string "EE551" to a variable x
    x = "EE551"

    # Assign a string "Stevens" to a variable y
    y = "Stevens"
   
    # Repeat variable y 5 times
    z = y * 5

    # What is the length of z?
    len(z)
    
    # Concatenate variable y with string " is good"
    y = "Stevens"
    print(y + " is good")
    
    # Replace "good" with "awesome" in variable m and assign it to a new variable n
    m = y + " is awesome"
    n = m
    return x, y, z, length, m, n


def lists():
    """
    This is to review basic operations with lists.
    """
    n = "Stevens is awesome"
    
    # Split variable n on a delimiter space into a list of substrings
    n.split()
 
    # Get all the items past the first of the third substring
    n.split()[1:]
    
    # Create a 3 x 3 matrix as nested list such that
    #   first row is [1, 4, 5]
    #   second row is [6, 10, 11]
    #   third row is [12, 17, 38]
    import numpy as np
    A = np.array[1, 4, 5, 6, 10, 11, 12, 17, 38]
    A.shape = 3,3
    A
    # Collect the items in the last column of matrix A using list comprehension
    colomn = []
    for row in A:
        column.append(row[2])
        print("3rd column =", column)
    # Collect only the even items of the diagonal of matrix A using list comprehension
    li = [10, 38, 12]
    # We can convert a single character to its underlying integer code (e.g., its ASCII byte value)
    # by passing it to the built-in ord function. Generate a list of these integers to represent
    # each character of the string "Stevens" using list comprehension.
    li = (ord('S'), ord('t'), ord('e'), ord('v'), ord('e'), ord('n'), ord('s'))
    return p, r, c, d, o


def dictionaries():
    """
    This is to review basic operations with dictionaries.
    """
    # Create a dictionary that maps:
    #   fruit => "apple"
    #   quantity => 4
    #   color => "green"
    d = {"fruit":"apple", "quantity":"4", "color":"green"}
    
    # Get the item in dictionary f that the key "fruit" maps to
    d["fruit"]
    
    # Increase the quantity of f by 1
    # IMPLEMENT IT HERE
    D = d["quantity"] += 1
    
    # Create a nested dictionary where:
    #   name => {first_name => "Grace", last_name => "Hopper"} (a dictionary)
    #   jobs => ["scientist", "engineer"] (a list)
    #   age => 85
    d = {"name":{'first_name':'Grace','last_name':'Hopper'}, 'jobs':['scientist', 'engineer'], 'age':85}
    
    # Add "programmer" to the list of jobs Grace has
    # IMPLEMENT IT HERE
    d['jobs'].append('programmer')
    
    # Get the third job Grace has that you recently added
    d['jobs'][2]
    
    # Use the sort() function to get sorted keys of amazing_grace in alphabetically ascending order
    sorted(d.keys())
    
    return a, f, p, k

numbers_and_strings()
lists()
dictionaries()





