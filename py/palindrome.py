# Python3 code to demonstrate
# checking a number is palindrome
# using math.log() + recursion + list comprehension
import math
   
# the recursive function to reverse
def rev(num):
    return int(num != 0) and ((num % 10) * \
             (10**int(math.log(num, 10))) + \
                          rev(num // 10))

# initializing number
number_1 = 9669669
number_2 = 1234


# using math.log() + recursion + list comprehension
# for checking a number is palindrome
res_1 = number_1 == rev(number_1)
res_2 = number_2 == rev(number_2)

# printing result
print(f"Is the number {number_1} palindrome ? : " + str(res_1))
print(f"Is the number {number_2} palindrome ? : " + str(res_2))
