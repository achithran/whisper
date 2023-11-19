binary_list = [1, 1,1,1,1,1,1,1,1,1, 0, 1,1, 1, 1,1,0, 1, 1]
current_ones = max_ones = 0

for x in binary_list:
    #print(x)
    if(x ==1):
        current_ones +=1
        max_ones = max(max_ones,current_ones)
    else:
        current_ones = 0

print(max_ones)


