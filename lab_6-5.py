# lab 6-5
numbers = [2, 6, 4, 9, 3]
maxnumber = max(numbers)
minnumber = min(numbers)  
print(maxnumber)
print(minnumber)
#prints the max and the min of the list of numbers 
if len(numbers) < 2:
    print("error: list does not meet specifications")
#when there is less than 2 unique numbers, prints the message