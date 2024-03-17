""" assume that n people are put into a circle and that they are eliminated in steps of k elements
n=7, k=3 => means 7 people in a circle
one every 3 is eliminated until one remains
[1,2,3,4,5,6,7] - initial sequence
[1,2,4,5,6,7] => 3 is counted out
[1,2,4,5,7] => 6 is counted out
[1,4,5,7] => 2 is counted out
[1,4,5] => 7 is counted out
[1,4] => 5 is counted out
[4] => 1 counted out, 4 is the last element - the survivor! """

def find_survivor(n, k):
    people = list(range(1, n + 1))
    
    # Initialize the index of the person to be eliminated
    index = 0
    while len(people) > 1:
        # Calculate the index of the person to be eliminated
        index = (index + k - 1) % len(people)
        people.pop(index)
    return people[0]
n = 7
k = 3
survivor = find_survivor(n, k)
print("The survivor is:", survivor)


       
        