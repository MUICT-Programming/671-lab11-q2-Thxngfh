# YOUR CODE HERE
ef summation(list1,list2,n):
    updated_list = []
    for i in range(n):
        updated_list.append(list1[i]+list2[i])
    return updated_list
def find_min_max(lst):
    return (min(lst),max(lst))
x = []
y = []
n = int(input())
for i in range(n):
    x.append(int(input()))
for i in range(n):
    y.append(int(input()))
result = summation(x,y,n)
print(result)
minmax = find_min_max(result)
print(minmax)
