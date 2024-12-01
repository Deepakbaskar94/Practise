#Operators Practise

# Find small among 3
a = 6
b = 50
c = 5

if a <= b and a <= c:
    print("a is smaller")
elif b <= a and b <= c:
    print("b is smaller")
else:
    print("c is smaller")



# Find mid among 3 
if a == b or a == c or b == c:
    print("all three number should be different")
elif a <= b and a >= c:
    print("a is mid")
elif b <= a and b >= c:
    print("b is mid")
else:
    print("c is mid")