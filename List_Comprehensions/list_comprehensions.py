if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    my_list=[]
    for i in range(x+1):
        for j in range(y+1):
            for q in range(z+1): 
                if i+j+q!=n:
                    my_list.append([i,j,q])
    print(my_list)