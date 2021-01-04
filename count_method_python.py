a = [4,6, 7, 9, 4, 5, 4, 5, 6, 4, 7, 7, 3, 2, 4, 5, 6, 6, 7, 8, -1]

#built-in count method
ans= a.count(4)  #conting how many 4's in a
print(ans)

#How it works excatly
def my_count(num):
    my_num=0
    for i in a:
        if num==i:
             my_num+=1

    return my_num

print(my_count(4))