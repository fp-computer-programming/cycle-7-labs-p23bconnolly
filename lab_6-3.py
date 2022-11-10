# lab 6-3
colors = ['red','blue','yellow','green']
colors.extend(['purple','pink','black']) 
print(colors) 
#3 colors are added to the end of the list 
colors.append("gray") 
print(colors)
# adds the color gray to the end of the statement using a different method 
colors.insert(3, "white")
print(colors) 
#inserts white at posititon 3
colors_copy = colors[:]
print(colors_copy) 
#creates a copy of the 1st variable 
colors.remove("red")
print(colors) 
#prints the whole list and removes the 1st color from the list 
