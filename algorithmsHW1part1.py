
def sum():
    n = input("Please enter a number:");
    n=int(n);
    sum = 0;
    
    for i in range(1,n+1):
        sum = sum +i
    return sum

x = sum()
print(x)