# get user input
name1 = input("Enter one name: ")
name2 = input("Enter another name: ")

space = name1.find(" ")
name1_first = name1[0:space]
name1_last = name1[space+1:len(name1)]
space = name2.find(" ")
name2_first = name2[0:space]
name2_last = name2[space+1:len(name2)]

# find combinations
name1_first_1sthalf = name1_first[0:int(len(name1_first)/2)]
name1_first_2ndhalf = name1_first[int(len(name1_first)/2):len(name1_first)]
name1_last_1sthalf = name1_last[0:int(len(name1_last)/2)]
name1_last_2ndhalf = name1_last[int(len(name1_last)/2):len(name1_last)]

name2_first_1sthalf = name2_first[0:int(len(name2_first)/2)]
name2_first_2ndhalf = name2_first[int(len(name2_first)/2):len(name2_first)]
name2_last_1sthalf = name2_last[0:int(len(name2_last)/2)]
name2_last_2ndhalf = name2_last[int(len(name2_last)/2):len(name2_last)]

new_name1_first = name1_first_1sthalf + name2_first_2ndhalf
new_name1_last = name1_last_1sthalf + name2_last_2ndhalf
new_name2_first = name2_first_1sthalf + name1_first_2ndhalf
new_name2_last = name2_last_1sthalf + name1_last_2ndhalf

# print results
print(new_name1_first, new_name1_last)
print(new_name2_first, new_name2_last)
