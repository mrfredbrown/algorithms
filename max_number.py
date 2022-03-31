
def max_number():
    n = [];
    max = 0;
    for i in range(3):
        x = input("Please enter a number:")
        x = int(x)
        n.append(x)
        if x > max:
            max = x

    print(n);
    return max;

print(max_number());
