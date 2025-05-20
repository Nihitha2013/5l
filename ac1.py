n1=[10,11,13]
n2=[14,15,16]
sum=map(lambda x,y:x+y, n1, n2)
print("sum list:",list(sum))

a=[34,56,47,89]
def cube(n):
    return n*n*n
d=list(map(cube,a))
print(d)