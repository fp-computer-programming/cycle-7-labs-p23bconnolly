#lab_6=8
value_1 = int(input("please input your first numeric value")) 
value_2 = int(input("please input your second numeric value")) 
value_3 = int(input("please input your third numeric value"))
#prompts the user to input 3 numeric values
list = [value_1, value_2, value_3]
#creates a list in the order they were inputted
if value_1 %2 == 0 and value_2 %2 == 0 and value_3 %2 == 0:
    print("the numbers are all even")
elif value_1 %2 != 0 and value_2 %2 != 0 and value_3 %2 != 0:
    print("the numbers are odd")
else:
    print("numbers are both even and odd") 
#detects if the numbers are even, odd, or a mix of the two
