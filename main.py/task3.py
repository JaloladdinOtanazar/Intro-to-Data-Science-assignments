import time
def decorator_1(function):
    def wrapper(*args, **kwargs):
        time_started = time.time() 
        time_resulted = function(*args, **kwargs)  
        time_ended = time.time()
        print("Running time of", function.__name__,"is", round(time_ended - time_started, 6), "seconds")
        return time_resulted 
    return wrapper 



import random
from task3 import decorator_1

@decorator_1
def func():
    result = 0
    n =  random.randint(10,751)
    for i in range(n):
        result += (i**2)
        
@decorator_1
def func():
    max_val = float('-inf')
    n =  random.randint(10,751)
    res = [pow(i,2) for i in range(n)]
    for i in res:
        if i > max_val: 
            max_val = i
    
if __name__ == "__main__": 
    func()
    func()
    func()
    func()
    func()
