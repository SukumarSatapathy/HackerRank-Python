x = int(input())
y = int(input())
z = int(input())
n = int(input())
i_list = list(range(x+1))
j_list = list(range(y+1))
k_list = list(range(z+1))
p_list = [list([i,j,k]) for i in i_list for j in j_list for k in k_list if(i+j+k!=n)]
print(p_list)
