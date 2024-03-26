#print  two numbers even or odd
a=int(input("enter a value:"))
b=int(input("enter b value:"))
if a%2==0 and b%2==0:
    print("even")
else:
    print("not even")




#using def fun
def num(a,b):
    if a%2==0 and b%2==0:
        return True
    else:
        return False
res=num(a,b)
a=int(input("enter a value:"))
b=int(input("enter b value:"))
print(res)
    
