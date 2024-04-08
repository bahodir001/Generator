def CloneRange(start=2):
    while True:
        yield start
        start *= 2

# Calling the CloneRange generator
clone_range = CloneRange()

# Calling values multiple times
for _ in range(10):
    print(next(clone_range))


""" EXPLANATION OF YIELD
        The yield keyword is important to the generator function. On each iteration, it returns a value via yield and stores the state inside the function.
    On the next iteration, the function repeats with the last saved state, continuing where it left off on its right. 
    This is the same as the suspended function with yield.
 """