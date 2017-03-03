import re


str = "ab8c1234-8m0.6"
find_int = re.findall(r'[+-]?\d+(?:\.\d+)?', str)
print (find_int)

#print(sum(int(find_int))

def sum(list):
    sum = 0
 
    # Add every number in the list.
    for i in range(0, len(list)):
        sum = sum + list[i]
 
    # Return the sum.
    return sum
