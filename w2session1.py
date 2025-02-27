"""

Problem 1: The Library of Alexandria
In the ancient Library of Alexandria, a temporal rift has scattered several important scrolls across different rooms. 
You are given a dictionary library_catalog that maps room names to the number of scrolls that room should have and a second dictionary actual_distribution that maps room names to the number of scrolls found in that room after the temporal rift.

Write a function analyze_library() that determines if any room has more or fewer scrolls than it should. The function should return a dictionary where the keys are the room names and the values are the differences in the number of scrolls (actual number of scrolls - expected number of scrolls). You must loop over the dictionaries to compute the differences.

def analyze_library(library_catalog, actual_distribution):
    pass
Example Usage:

library_catalog = {
    "Room A": 150,
    "Room B": 200,
    "Room C": 250,
    "Room D": 300
}

actual_distribution = {
    "Room A": 150,
    "Room B": 190,
    "Room C": 260,
    "Room D": 300
}


print(analyze_library(library_catalog, actual_distribution))
Example Output:

{'Room A': 0, 'Room B': -10, 'Room C': 10, 'Room D': 0}

"""

def analyze_library(library_catalog, actual_distribution):

    #loop through both dictionaries
    differences = dict()
    for room in library_catalog:
        # try and catch

        try :
           differences[room] =  actual_distribution[room] - library_catalog[room]
        except:
           differences[room] = 0 - library_catalog[room]

    
    # create a new dictioanry with new values of the differences
    return differences

library_catalog = {
    "Room A": 150,
    "Room B": 200,
    "Room C": 250,
    "Room D": 300
}

actual_distribution = {
    "Room A": 150,
    "Room B": 190,
    "Room C": 260,
}

# O(N)
# O(N)

print(analyze_library(library_catalog, actual_distribution))


"""
Problem 4: Time Portals
In your time travel adventures, you are given an array of digit strings portals and a digit string destination. 
Return the number of pairs of indices (i, j) (where i != j) such that the concatenation of portals[i] + portals[j] equals destination.

Note: For index values i and j, the pairs (i, j) and (j, i) are considered different - order matters.

def num_of_time_portals(portals, destination):
    pass
Example Usage:

portals1 = ["777", "7", "77", "77"]
destination1 = "7777"
portals2 = ["123", "4", "12", "34"]
destination2 = "1234"
portals3 = ["1", "1", "1"]
destination3 = "11"

print(num_of_time_portals(portals1, destination1))
print(num_of_time_portals(portals2, destination2))
print(num_of_time_portals(portals3, destination3))
Example Output:

4
2
6

"""


from collections import Counter

def num_of_time_portals(portals, destination):
    count = 0
    portal_counts = Counter(portals)  # Count occurrences of each portal string
    
    for i, portal in enumerate(portals):
        complement = destination[len(portal):]  # Find required second half
        if portal != destination[:len(portal)]:
            continue  # If the first part doesn't match, skip
        
        if complement in portal_counts:
            count += portal_counts[complement]
            
            if complement == portal:  # Avoid double counting same index
                count -= 1
    
    return count



portals2 = ["123", "4", "12", "34"]
destination2 = "1234"

portals1 = ["777", "7", "77", "77"]
destination1 = "7777"

print(num_of_time_portals(portals1, destination1))

print(num_of_time_portals(portals2, destination2))


"""
Problem 5: Detect Temporal Anomaly
As a time traveler, you have recorded the occurrences of specific events at different time points. You suspect that some events might be occurring too frequently within short time spans, indicating potential temporal anomalies. Given an array time_points where each element represents an event ID at a particular time point, and an integer k, determine if there are two distinct time points i and j such that time_points[i] == time_points[j] and the absolute difference between i and j is at most k.

Note: The indices must be unique, but not the values i and j themselves.

def detect_temporal_anomaly(time_points, k):
    pass
Example Usage:


time_points1 = [1, 2, 3, 1]
k1 = 3

time_points2 = [1, 0, 1, 1]
k2 = 1

time_points3 = [1, 2, 3, 1, 2, 3]
k3 = 2

print(detect_temporal_anomaly(time_points1, k1))  
print(detect_temporal_anomaly(time_points2, k2)) 
print(detect_temporal_anomaly(time_points3, k3)) 
Example Output:

True
True
False
"""

def detect_temporal_anomaly(time_points, k):
    #make a dictionary where key is the integer and value is the index in list
    dictionary = {}
    for i, num in enumerate(time_points):
        if num in dictionary and i - dictionary[num] <= k:
            return True
        else:
            dictionary[num] = i
    
    return False


time_points1 = [1, 2, 3, 1]
k1 = 3

time_points2 = [1, 0, 1, 1]
k2 = 1

time_points3 = [1, 2, 3, 1, 2, 3]
k3 = 2

print(detect_temporal_anomaly(time_points1, k1))  
print(detect_temporal_anomaly(time_points2, k2)) 
print(detect_temporal_anomaly(time_points3, k3))


"""

Problem 6: Find Travelers with Zero or One Temporal Anomalies
In your time travel adventures, you are given an integer array anomalies where anomalies[i] = [traveleri, anomalyi] indicates that the traveler traveleri caused a temporal anomaly anomalyi.

Return a list answer of size 2 where:

answer[0] is a list of all travelers that have not caused any anomalies.
answer[1] is a list of all travelers that have caused exactly one anomaly.
The values in the two lists should be returned in increasing order.

Note: You should only consider the travelers that have experienced at least one anomaly.

def find_travelers(anomalies):
    pass
Example Usage:

anomalies1 = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
anomalies2 = [[2,3],[1,3],[5,4],[6,4]]

print(find_travelers(anomalies1)) 
print(find_travelers(anomalies2))
Example Output:

[[1, 2, 10], [4, 5, 7, 8]]
[[1, 2, 5, 6], []]

"""

def find_travelers(anomalies):

    #two lists
    list1 = []
    list2 = []

    tracker = {}
    travelers = set()

    for anomaly, traveler in anomalies:
        travelers.add(traveler)
        travelers.add(anomaly)
        tracker[traveler] = tracker.get(traveler,0) + 1

    for traveler in sorted(travelers):

        if traveler not in tracker:
            list1.append(traveler)
        elif tracker[traveler] == 1:
            list2.append(traveler)
        

    return [list1, list2]
        
        


        

    #if traveler is in index 0: list 1
    #if traveler is in index 1 at least once: list 2
    #if anomalyi is in index 2 at least once: list 2




    pass


anomalies1 = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
anomalies2 = [[2,3],[1,3],[5,4],[6,4]]

print(find_travelers(anomalies1)) 
print(find_travelers(anomalies2))