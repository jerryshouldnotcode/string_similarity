''' measures the minimum number of single-character edits needed 
    to change one string to the other
'''

def levenshtein(a, b):

    # if either a or b is empty, return the non-empty one...
    if not a:
        return len(b)
    elif not b:
        return len(a)

    # set up a matrix (2D list) with the lengths of both strings...
    rows = len(a) + 1  
    columns = len(b) + 1
    matrix = [[0 for _ in range(columns)] for _ in range(rows)]

    # initialize matrix [row x column]
    for i in range(1, len(a) + 1):
       # populate each row
       matrix[i][0] = i 

    for j in range(1, len(b) + 1):
        # populate each column, adding 1 because it's 1-indexed
        matrix[0][j] = j 

    '''main computation below'''

    # loop through each combination of characters in both strings
        # starting from 1 since we initialized this already
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):

            # apply conditions of the formula's piecewise equation
            # apparently booleans can work as just 0 and 1, the sigma?!

            sub_value = matrix[i-1][j-1] + (a[i-1] != b[j-1]) #substution counter, only adds if a != b
            ins_value = matrix[i][j-1] + 1   # insertion counter
            del_value = matrix[i-1][j] + 1    # deletion counter

            # the cell with the least value of the three is the value at (i,j)
            matrix[i][j] = min(sub_value, ins_value, del_value)

            '''essentially, the levenshtein equation solves the question: does it cost
            more to substitute, insert or delete a character? '''

    return matrix[len(a)][len(b)] # the final answer 
                


# word1 = input("Enter a word: ")
# word2 = input("Enter a word: ")

# # for consistency sake, without messing the printback
# lev_dist = levenshtein(word1.lower().strip(), word2.lower().strip())
# print(f'The Levenshtein Distance between {word1} and {word2} is: {lev_dist}')


# this took a minute lol
        

  