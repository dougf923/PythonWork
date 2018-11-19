###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # TODO: Your code here
    cow_name_dict = {};

    f = open(filename);


    for line in f:
    	name,weight = line.split(",");
    	
    	if weight[-1:] == "\n":
    		cow_name_dict[name] = int(weight[:-1]);
    	else:
    		cow_name_dict[name] = int(weight);

    f.close();

    return cow_name_dict




# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    
    #Initialize Outer Variables
    outer_list = [];
    cowNames = [];
    for key in cows.keys():
        cowNames.append(key)
    nCowsToTransport = len(cowNames);

    while nCowsToTransport > 0:
        inner_list = [];
        nCowsOnTrip = 0;
        weight_left = limit;
        full_trip = False;

        while not full_trip:
            added_new_cow = False;
            for name in cowNames:
                if len(inner_list) == nCowsOnTrip and (cows[name] <= weight_left):
                    inner_list.append(name);
                    added_new_cow = True;
                elif (cows[name] >  cows[inner_list[-1]]) and (cows[name] <= weight_left):
                    inner_list[-1] = name;
                elif (name == cowNames[-1] and added_new_cow == False):
                    full_trip = True;

            if not full_trip: 
                weight_left -= cows[inner_list[-1]]; 
                cowNames.remove(inner_list[-1]);
                nCowsOnTrip += 1;

            if len(cowNames) == 0:
                full_trip = True;    
                

        outer_list.append(inner_list);
        nCowsToTransport -= len(inner_list)

    return outer_list







    

# Problem 3
def brute_force_cow_transport(cow_dict,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    cowNames = [];
    for key in cow_dict.keys():
        cowNames.append(key)

    nCowsToTransport = len(cowNames);
    

    #Create list of all potential trips
    partition_list = [];

    for partition in get_partitions(cowNames):
        partition_list.append(partition);


    # Initialize number of trips to try and move all cows
    nTrips = 1;

    #Since it is assumed that all individual cows are below the limit. A trivial
    #solution of one cow per trip is always available. Therfore, this while loop
    #doesn't need an explicit exit
    while True:

        for partition in partition_list:

            if len(partition) == nTrips:
                overweightFlag = False;

                for trip in partition:
                    weightOnTrip = 0;

                    for cow in trip:
                        weightOnTrip += cow_dict[cow];
    
                    if weightOnTrip > limit:
                        overweightFlag = True;

                if not overweightFlag:
                    return partition

        nTrips += 1;





        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    data = load_cows('ps1_cow_data.txt');

    start1 = time.time()
    out1 = greedy_cow_transport(data)
    end1 = time.time()

    print("Greedy Algorithm Output: " + str(out1))
    print("Greedy Algorithm Time: " + str(end1-start1) + " seconds")

    start2 = time.time()
    out2 = brute_force_cow_transport(data)
    end2 = time.time()

    print("Brute Force Algorithm Output: " + str(out2))
    print("Brute Force Algorithm Time: " + str(end2-start2) + " seconds")

    return None


compare_cow_transport_algorithms()