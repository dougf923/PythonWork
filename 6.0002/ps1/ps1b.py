###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

import time

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always an egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    # TODO: Your code here
    if target_weight in egg_weights:
        return 1
    try:
        return memo[target_weight]
    except KeyError:

        if target_weight > egg_weights[-1]:
            weight_max = egg_weights[-1];
        else:
            for weight_idx in range(len(egg_weights)):
                if target_weight > egg_weights[weight_idx] and target_weight < egg_weights[weight_idx+1]:
                    weight_max = egg_weights[weight_idx];



        result = dp_make_weight(egg_weights,weight_max,memo)+dp_make_weight(egg_weights,target_weight-weight_max,memo);
        memo[target_weight] = result;
        return result    


# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 99
    #print("Egg weights = (1, 5, 10, 25)")
    #print("n = 99")
    #print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")

    tstart = time.time()
    print("Actual output:", dp_make_weight(egg_weights, n))
    tend = time.time()
    print("Time to run DP: " + str(tend-tstart) + " seconds")
    print()