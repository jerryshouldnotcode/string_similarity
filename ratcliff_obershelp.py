'''find the similarity between two strings by identifying their longest common substrings'''

def ratcliff_obershelp(a, b):

    # if a or b, or both a and b are empty...(for empty strings)
    if not a and not b:
        return 1.0
    if not a or not b:
        return 0.0


    total_length = len(a) + len(b)
    # method: find the longest common substring in both, remove it, repeat 
    total_substr_length = 0
    
    def find_longest_common_substring(a, b, long_substrings):
        
        longest = ""
        
        # Try all possible starting positions in string A
        for i in range(len(a)):
            # Try all possible lengths starting from position i
            for length in range(1, len(a) - i + 1):
                substring = a[i:i+length]
                # Check if this substring appears in string B
                if substring in b:
                    if len(substring) > len(longest):
                        longest = substring


        # decomposition
        if longest:  # only if we found a common substring
            
            # add to bigger list for later
            long_substrings.append(longest)

            # Split both strings around the LCS
            a_parts = a.split(longest)
            b_parts = b.split(longest)
            
            # Process each remaining part separately
            for a_part in a_parts:
                for b_part in b_parts:
                    if a_part and b_part:  # if both parts have content
                        find_longest_common_substring(a_part, b_part, long_substrings)
        return long_substrings

    # add up the lengths of all found LCS, divide by total length of both strings 
    long_substrings = find_longest_common_substring(a, b, [])

    for str in long_substrings:
        total_substr_length += len(str)
    
    # formula
    return 2 * (total_substr_length/total_length) 

   
# word1 = input("Enter a word: ")
# word2 = input("Enter a word: ")
# print(f'The Similarity Ratio between {word1} and {word2} is: {ratcliff_obershelp(word1, word2)}')