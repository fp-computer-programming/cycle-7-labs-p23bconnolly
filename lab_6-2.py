#lab 6-2
my_row = ["Ethan", "Will"] 
#create row variable including first two names
my_row[1:2] = ["Brian"]
print(my_row) 
#prints the row with will replaced with Brian 
my_row2 = my_row
print(my_row2)
#prints the 2nd variable, which is equal to the first
del my_row[1] 
print(my_row) 