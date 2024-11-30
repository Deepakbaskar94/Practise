"""1. Given an array of N integers. Your task is to print the sum of all of the integers.
Example 1:
Input:
4
1 2 3 4
Output:
10
Example 2:
Input:
6
5 8 3 10 22 45
Output:
93"""

count = int(input("How many numbers need to be added? "))
try: 
    data = list(map(int, input("Enter the numbers with a space in between: ").split()))
    print("entered data: ", data)
    if count != len(data):
        print("Error: The number of integers provided does not match the count.")
except ValueError:
    print("Please Enter only numbers")

added = sum(data)
print(added)

"""Q2. Given an array A[] of N integers and an index Key. Your task is to print the element present at
index key in the array.
Example 1:
Input:
5 2
10 20 30 40 50
Output:
30
Example 2:
Input:
7 4
10 20 30 40 50 60 70
Output:
50"""

try:
    metadata = list(map(int, input("Enter the number of elements and position of the array seperated by Space: ").split()))
    values = list(map(int, input("Enter the values: ").split()))
except ValueError:
    print("Please enter only numbers")
    
if metadata[0] != len(values):
    print("Number of elements doesnot match the count")
elif metadata[1] > len(values):
    print("Given index position is greater than the array count")
elif metadata[1] <= 0:
    print("position number should be greater than 0.")
else:
    position = metadata[1] - 1  
    print(values[int(position)]) 





"""Q3. Given an sorted array A of size N. Find number of elements which are less than or equal to given
element X.
Example 1:
Input:
N = 6
A[] = {1, 2, 4, 5, 8, 10}
X = 9
Output:
5
Example 2:
Input:
N = 7
A[] = {1, 2, 2, 2, 5, 7, 9}
X = 2
Output:
4
"""



try:
    count = int(input("Size of the array: "))
    data = list(map(int, input("Enter the elements seperated by Space: ").split(",")))
    lessthan = int(input("Less than number: "))
except ValueError:
    print("Please enter only numbers")
    
if len(data) != count:
    print("Count is not matching with the array element")
else:
    total = 0
    for n in data:
        if n < lessthan:
            total += 1
    print(total)
    
    
"""Q4. You are given an array A of size N. You need to print elements of A in alternate order (starting
from index 0).
Example 1:
Input:
N = 4
A[] = {1, 2, 3, 4}
Output:
1 3
Example 2:
Input:
N = 5
A[] = {1, 2, 3, 4, 5}
Output:
1 3 5"""

try:
    count = int(input("Enter the count of the array: "))
    elements = list(map(int, input("Enter the elements of the array, seperated by space: ").split(",")))
    if count != len(elements):
        print("Entered elements are not matching the count number")
    else:
        for n in range(count):
            if (n+1)%2 != 0:
                print(elements[n], end=" ")
    print("")
except ValueError:
    print("Kindly provide a Valid input")


"""Q5. Given an array Arr of N positive integers. Your task is to find the elements whose value is equal
to that of its index value ( Consider 1-based indexing ).
Example 1:
Input:
N = 5
Arr[] = {15, 2, 45, 12, 7}
Output: 2
Explanation: Only Arr[2] = 2 exists here.
Example 2:
Input:
N = 1
Arr[] = {1}
Output: 1
Explanation: Here Arr[1] = 1 exists."""


try:
    count = int(input("Enter the count of the array: "))
    elements = list(map(int, input("Enter the elements of the array, seperated by space: ").split(",")))
    if count != len(elements):
        print("Entered elements are not matching the count number")
    else:
        for n in range(count):
            if (n+1) == elements[n]:
                print(elements[n], end=" ")
    print("")
except ValueError:
    print("Kindly provide a Valid input")
    



"""Q6. Given an array of size N and you have to tell whether the array is perfect or not. An array is said
to be perfect if it's reverse array matches the original array. If the array is perfect then print
"PERFECT" else print "NOT PERFECT".
Example 1:
Input : Arr[] = {1, 2, 3, 2, 1}
Output : PERFECT
Explanation:
Here we can see we have [1, 2, 3, 2, 1]
if we reverse it we can find [1, 2, 3, 2, 1]
which is the same as before.
So, the answer is PERFECT.
Example 2:
Input : Arr[] = {1, 2, 3, 4, 5}
Output : NOT PERFECT"""

try:
    elements = list(map(int, input("Enter the elements of the array, seperated by space: ").split(",")))
    count = len(elements)
    
    for n in range(count):
        if elements[n] == elements[count-1]:
            perfect = True
        else:
            perfect = False
            break
        count -=1
    if perfect:
        print("PERFECT")
    else:
        print("NOT PERFECT")      
            
except ValueError:
    print("Kindly provide a Valid input")



"""Q7. Given an array of length N, at each step it is reduced by 1 element. In the first step the maximum
element would be removed, while in the second step minimum element of the remaining array would
be removed, in the third step again the maximum and so on. Continue this till the array contains only 1
element. And find the final element remaining in the array.
Example 1:
Input:
N = 7
A[] = {7, 8, 3, 4, 2, 9, 5}

Ouput:
5
Explanation:
In first step '9' would be removed, in 2nd step
'2' will be removed, in third step '8' will be
removed and so on. So the last remaining
element would be '5'.
Example 2:
Input:
N = 8
A[] = {8, 1, 2, 9, 4, 3, 7, 5}
Ouput:
4"""

try:
    count = int(input("Enter the count of the array: "))
    elements = list(map(int, input("Enter the elements of the array, seperated by space: ").split(",")))
    if count != len(elements):
        print("Entered elements are not matching the count number")
    else:
        output = elements
        for n in range(count):
            if len(output) > 1:
                if (n+1)%2 != 0:
                    print("remove greater number: ", end="")
                    max = output[0]
                    for n in range(len(output)):
                        if max < output[n]:
                            max = output[n]
                    print(max)
                    output.remove(max)
                else:
                    print("remove lesser number: ", end="")
                    min = output[0]
                    for n in range(len(output)):
                        if min > output[n]:
                            min = output[n]
                    print(min)
                    output.remove(min)
        print("final element: ", output[0])

except ValueError:
    print("Kindly provide a Valid input")



"""Q8. Given an array of N distinct elements, the task is to find all elements in array except two greatest
elements in sorted order.
Example 1:
Input :
a[] = {2, 8, 7, 1, 5}
Output :
1 2 5
Explanation :
The output three elements have two or
more greater elements.
Example 2:
Input :
a[] = {7, -2, 3, 4, 9, -1}
Output :
-2 -1 3 4"""

try:
    elements = list(map(int, input("Enter the elements of the array, seperated by space: ").split(",")))
    final = []
    temp = elements
    min = elements[0]
    for n in range(len(elements)):
        min = temp[0]
        for i in range(len(temp)):
            if min > temp[i]:
                min = temp[i]
        temp.remove(min)
        final.append(min)
    
    print(final)
    final.pop()
    final.pop()
    print(final)
    
except ValueError:
    print("Kindly provide a Valid input")
        
        
    
        


"""Q9. Write a program to find the sum of the given series 1+2+3+ . . . . . .(N terms)
Example 1:
Input:
N = 1
Output: 1
Explanation: For n = 1, sum will be 1.
Example 2:
Input:
N = 5
Output: 15
Explanation: For n = 5, sum will be 1
+ 2 + 3 + 4 + 5 = 15."""

try:
    count = int(input("Enter the number: "))
    output = 0
    for n in range(count):
         output += n+1
    print(output)
            
except ValueError:
    print("Kindly provide a Valid input")



"""Q10. Given a number N. Your task is to check whether it is fascinating or not.
Fascinating Number: When a number(should contain 3 digits or more) is multiplied by 2 and 3 ,and
when both these products are concatenated with the original number, then it results in all digits from 1
to 9 present exactly once.
Example 1:
Input:
N = 192
Output: Fascinating
Explanation: After multiplication with 2
and 3, and concatenating with original
number, number will become 192384576
which contains all digits from 1 to 9.
Example 2:
Input:
N = 853
Output: Not Fascinating
Explanation: It's not a fascinating
number."""

try:
    count = int(input("Enter the number: "))
    if len(str(count)) >= 3:
        multwo = count * 2
        multhree = count * 3
        total = str(count)+str(multwo)+str(multhree)
        if len(list(total)) == len(set(total)):
            print("FASCINATING")
        else:
            print("NOT FASCINATING")      
            
except ValueError:
    print("Kindly provide a Valid input")



"""Bonus Question
Given an array of even size N, task is to find minimum value that can be added to an element so that
array become balanced. An array is balanced if the sum of the left half of the array elements is equal
to the sum of right half.
Example 1:
Input:
N = 4
arr[] = {1, 5, 3, 2}
Output: 1
Explanation:
Sum of first 2 elements is 1 + 5  = 6,
Sum of last 2 elements is 3 + 2  = 5,
To make the array balanced you can add 1.
Example 2:
Input:
N = 6
arr[] = { 1, 2, 1, 2, 1, 3 }
Output: 2
Explanation:
Sum of first 3 elements is 1 + 2 + 1 = 4,
Sum of last three elements is 2 + 1 + 3 = 6,
To make the array balanced you can add 2."""

try:
    count = int(input("Enter the array size: "))
    data = list(map(int, input("Enter the values of the array: ").split(",")))
    if count%2 == 0:
        mid = count // 2
        firstvalue = 0
        secondvalue = 0
        for n in range(0, mid, 1):
            firstvalue = firstvalue + data[n]
        for n in range(count-1, mid-1, -1):
            secondvalue = secondvalue + data[n]
        print("Output: ", abs(secondvalue - firstvalue))
    else:
        print("The array size is not even")
    
except ValueError:
    print("Give the Valid number")



        