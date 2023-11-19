# Create a list
my_list = [1, 2, 3, 4, 5]
my_list2 = [1, 2, 6,7,8]


new_list = list(set(my_list) & set(my_list2))

print(new_list)

