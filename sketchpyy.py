x=int(input("Enter the value of x:"))
y=int(input("Enter the value of y:"))
def func(x,y):
    z=x*y
    x=x**y
    print(x,"multiplied with",y" is", z)
    print(x,"raised to poewer",y" is:",x)
def disp():
    for j in range(1,10):
        for i in range(j):
            print(i," ",j)
def another():
    lst = list(12,20,30,40,)
    lst[0] = 10
    print(lst)

another()
disp()
func()
