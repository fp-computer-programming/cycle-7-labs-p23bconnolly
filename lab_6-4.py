#lab 6-4 

subjects =['economics','geometry','theology']
subjects.append('biology') 
print(subjects) 
#prints all 4 subjects, adding bio to the list
subjects_2 = subjects.index('theology')
print(subjects_2)
#prints the list and reads the index of theology
subjects.sort()
print(subjects) 
#sorts each subject in alphabetical order
subjects_3 = subjects.copy()
subjects_3.reverse() 
print(subjects_3)
#prints the line of subjects in reverse alphabetical order
