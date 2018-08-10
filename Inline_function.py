Output: [(3, -6, 1), (0, -1, 3), (-1, 0, 1), (4, 2, 7), (1, 3, -2), (-2, 8, -5)]

#Using lambda in an inline function
A = [(1, 3, -2),(4, 2, 7),   #list of 3-tuples
    (-1, 0, 1),(0, -1, 3),
    (-2, 8, -5),(3, -6, 1)]

#If we want sort A (in increasing order) by the first element in each list we can use:
print sorted(A)
#Output: [(-2, 8, -5), (-1, 0, 1), (0, -1, 3), (1, 3, -2), (3, -6, 1), (4, 2, 7)]

#If we want sort A (in increasing order) by the second element in each list we can use:
def sortkey(A):
    return A[1]

print sorted(A, key=sortkey)
#Output: [(3, -6, 1), (0, -1, 3), (-1, 0, 1), (4, 2, 7), (1, 3, -2), (-2, 8, -5)]

#Now we can do the same thing as above by creating an inline function
#Which saves space and memory
#We will use lambda, also know as an anonymous function, as the key
print sorted(A, key=lambda A: A[1])
#Output: [(3, -6, 1), (0, -1, 3), (-1, 0, 1), (4, 2, 7), (1, 3, -2), (-2, 8, -5)]

#We can even change the order to decreasing and just use the first 3 lists
print sorted(A, key=lambda A: A[1], reverse = True)[:3]
#Output: [(-2, 8, -5), (1, 3, -2), (4, 2, 7)]
