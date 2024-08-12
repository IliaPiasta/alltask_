import time

a, b, c = "red", 'yellow', 'green'
SECONDS  = 3 
result = None
while True:
    result = a
    print(result)
    time.sleep(SECONDS)
    
    result = b
    print(result)
    time.sleep(SECONDS)
    
    result = c
    print(result)
    time.sleep(SECONDS)