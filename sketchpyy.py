x=int(input("Enter the value of x:"))
y=int(input("Enter the value of y:"))
def func(x,y):
    z=x*y
    x=x**y
    print(x,"multiplied with",y" is", z)
    print(x,"raised to poewer",y" is:",x)
func()
def disp():
    for j in range(1,10):
        for i in range(j):
            print(i," ",j)