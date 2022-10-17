def solution(n):
    # string to integer conversion
    n = int(n)
    # initializing the number of conversions
    counter = 0
    while(n != 1):
        # indicating an exception for number 3 which results in two more conversions
        if(n == 3):
            counter += 2
            return counter
        # the shortest path is made by division. Unless it isn't divisble,
        # we try to add or subtract it to check whether the new result is divisible by 4
        # because 4 makes the path shorter than only 2
        if(n % 2 == 0):
            n //= 2
            counter += 1
        else:
            if((n + 1) % 4 == 0):
                n = ((n + 1) // 2)
            else:
                n = ((n - 1) // 2)
            counter += 2
    return counter
print(solution(str(10**309-1)))
