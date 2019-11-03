import ast
m=list()
list_str=input()
my_list=ast.literal_eval(list_str)
my_list=sorted(my_list)
print(my_list)
for i in range(len(my_list)-1):
    if my_list[i][1]>=my_list[i+1][0]:
        my_list[i+1]=[min(*my_list[i],*my_list[i+1]),max(*my_list[i],*my_list[i+1])]
        my_list[i]=['a','b']
        print(my_list)
print(my_list)
while my_list.count(['a','b']):
    my_list.remove(['a','b'])
print(my_list)
