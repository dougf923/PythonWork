# Problem Set 4A
# Name: Doug Famularo

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    perm_list = [];

    if len(sequence) == 1:
    	perm_list = [sequence]
    else:
    	temp_perm_list = get_permutations(sequence[1:len(sequence)])  	

    	for entry in temp_perm_list:
    		for i in range(len(entry)+1):
    			perm_list.append(entry[0:i]+sequence[0]+entry[i:len(entry)])

    perm_list.sort()			
    return perm_list



if __name__ == '__main__':
#    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    

#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)


