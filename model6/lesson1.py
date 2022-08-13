# Addition in lambda
# add_two = lambda my_number: my_number + 2
# print(add_two(10))

# # you can still it this way
# print((lambda my_number: my_number + 2)(10))


# #Generate a list using lambda


# # lambda using conditional logic
# Check_for_A_grade = lambda grade : 'Got an A!' if grade >= 90 else 'Did not get an A!'
# print(Check_for_A_grade(90))
# print(Check_for_A_grade(50))
# print(Check_for_A_grade(20))

# # using lambda function as an argument in a higher order function
# def myfunc(n):
#   return lambda a : a ** n

# square = myfunc(2)

# cube= myfunc(3)

# print(square(11))

# print(cube(11))

# #using lambda without defining a function
# #Lets square a number
# square = lambda a,n: a**n
# print(square(3,2))


# list = [(lambda x : x + 2, range(1, 101))]
# print(list)

# lists = list(map(lambda x=x: x * 10 for x in range(1, 11))) 

# for list in lists:
#     print(lists())
