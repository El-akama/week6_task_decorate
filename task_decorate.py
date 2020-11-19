import datetime
import sched, time

# task1
# def times(func):
#     def wrapper():
#         t = time.localtime()[3]
#         if t >= 9 and t < 21:
#             func()
#         else:
#             print('not time')
#     return wrapper
         
# @times
# def say_whee():
#     print("wheee")

# say_whee()

# task2
# def timer(f):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         res = f(*args, **kwargs)
#         end = time.time()
#         print(f'Время выполнения: {end-start} секунд.')
#         return res
#     return wrapper

# @timer
# def func(x, y):
#     return x + y

# func(1, 2)


# task3

# def repeat(func):
#     def wrapper():
#         num = 4
#         func()
#         return num * name
#     return wrapper

# @repeat
# def function(name):
#     print(f"{name}")

# function("Python")

# task3
# def repeat(num):
#     def newrepeat(func):
#         def wraper(*args, **kwargs):
#             for a in range(num):
#                 func(*args, *kwargs)
#         return wraper
#     return newrepeat

# @repeat(num=4)
# def function(name):
#     print(name)

# function('Python')


# task4
# users = {'name1': 1234, 'name2': 3456, 'name3': 5678, 'name4': 7890}
# def decorate(func):
#     def wrapper(username='username', password = 'password'):
#         if username in users.keys():
#             if password == users[username]:
#                 func(username, password)
#             else:
#                 print('Password is wrong')
#         else: 
#             print('Username not defind')
#     return wrapper

# @decorate
# def login(username, password ):
#     print(f'Wellcome, {username}')

# login(username='name5', password=12345)


# task5
# def myDecorator(func):
#     def wrapper(a, b=1, *args, **kwargs):
#         print("Calling testFunc (", args, kwargs, ")")
#         print("argument a: ", a)
#         print("argument b: ", b)
#         print("argument args: ", args)
#         print("argument kwargs: ", kwargs)
#         print('Finished testFunc', func(a, b, *args, **kwargs))
#     return wrapper

# @myDecorator
# def testFunc(a, b=1, *args, **kwargs):
#     return a + b
# testFunc(2, 3, 4, 5, c=6, d=7)
# print()
# testFunc(2, c=5, d=6)
# print()
# testFunc(10)
