#coding=utf-8

def a_new_decorator(func):
    def wrapTheFunction():
        print("I'm doing some boring work before func")
        func()
        print("I'm doing some boring work after func")
    return wrapTheFunction

@a_new_decorator
def a_function_require_decorator():
    print("I'm the function doing something interestinig")

a_function_require_decorator()
