# Python basics 3.1-3.3

# pg 60.
# def divide(num,den):
#     remainder = num % den
#     floor = num // den
#     print(num, 'divided by', den, 'equals', floor, 'with a remainder of', remainder)
#
# def main():
#     numerator = 5
#     denominator = 2
#     divide(numerator, denominator)
# main()


# # pg 61 one step arithmatic
# a = 5
# a+=2
# print(a) #returns 7
# a-=2
# print(a) #returns 5
# a*=2
# print(a) #returns 10
# print(type(a)) #returns <class 'float'>
# a/=2
# print(a) #returns 5.0
# print(type(a)) #returns <class 'float'.
# a%=2
# print(a) #returns 1.0
# a**=2
# print(a) #returns 1.0
# a//=2
# print(a) #returns 0.0


# # p 62. changing data types. Converting data types to integers.
# # Have them do the following for each one
# x = int(5.6)
# print(x)
# int(5) #object is an integer already. Returns 5
# int("5") #object is a string. Returns 5
# int(5.4) #object is a float. Returns 5
# int(5.9) #objectis a float. Returns 5
# int(-5.9) #object is a float. Returns 5
# # int("5.4") #object is a string. Returns ValueError: invalid literal


# # pg 63. abs value of x as an integer or a float.
# x=abs(-5)
# print(x)
# y=abs(5)
# print(y)
# t=abs(-5.5)
# print(t)
# d=abs(5.5)
# print(d)


# # pg 64. Returning the min and max value passed in
# num = min(2,1,3)
# print(num)
# num = min(3.14, -1.5, -300)
# print(num)
# num = max(2,1,3)
# print(num)
# num = max(3.14, -1.5, -300)
# print(num)


# # p 64 powers
# #pow(x,y[z])
# num = pow(4,2,3)
# print(num)
# newNum = pow(4,2)
# print (newNum)

# # p 65. rounding numbers
# num = round(3.14)
# print(num)
# numNew = round(1111, -2)
# print(numNew)
