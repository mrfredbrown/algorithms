def count_odd_even():
    odd=0;
    even=0;
    n = input("enter a number:");

    for element in n:
        if ((int(element))%2==0):
            even = even +1
        else:
            odd = odd + 1
            
    print("odd number of digits", odd)
    print("even number of digits", even)

count_odd_even();
