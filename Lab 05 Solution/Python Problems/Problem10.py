import time

def AppendandTrackTime():
    numbers = []
    for i in range(1, 101,1):
        start_time = time.time() 
        numbers.append(i)
        end_time = time.time()
        runtime=end_time-start_time
        print(f"Numbers list after adding {i} elements: {numbers}")
        print(f"Runtime after Adding {i} elements is: {runtime}")

# Driver
AppendandTrackTime()

#No Apparent change in time of appending the element as the size of list increases
