''' checking the number of differing positions between two equal length strings '''

def hamming(a, b):
    # given two strings a and b...
    # make sure both strings are the same
    if len(a) != len(b):
        raise ValueError(f"Both strings must have equal lengths!: {len(a)} vs {len(b)}")
    
    # as long as one of them has characters... 
    elif len(a) != 0:
        edits = 0

        for i in range(len(a)):
            # compare each character in both strings, add to edits when they are different...
            edits += 1 if a[i] != b[i] else 0
        return edits
    
    else: # putting this here because of the unit test
        edits = 0
        return edits