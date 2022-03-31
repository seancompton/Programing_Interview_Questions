#!/bin/python3

def plusMinus(arr):
    # Write your code here
    above_zero = 0
    above_zero_ratio = 0.0

    below_zero = 0
    below_zero_ratio = 0.0

    equal_to_zero = 0
    equal_to_zero_ratio = 0.0
    
    for i in arr:
        if(i > 0):
            above_zero = above_zero + 1
        elif(i<0):
            below_zero = below_zero + 1
        elif(i == 0):
            equal_to_zero = equal_to_zero + 1
        else:
            print(f"Sorry {i} is not a number we can work with")

    list_length = len(arr)
    print(below_zero)

    below_zero_ratio = below_zero / list_length
    above_zero_ratio = above_zero / list_length
    equal_to_zero_ratio = equal_to_zero / list_length
    a_fraction = 1/3
    
    print(f"{below_zero_ratio:.6f}")
    print(f"{above_zero_ratio:.6f}")
    print(f"{equal_to_zero_ratio:.6f}")

def main():
    array = [3, -4, 5, -90, 3, 0, 3, 5, 6, -9]
    plusMinus(array)




main()

