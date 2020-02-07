def iq_test(numbers):
    evens = 0
    odds = 0
    numbers = map(int, numbers.split())
    for num in numbers:
        if num % 2 == 0:
            evens += 1
        else:
            odds += 1
    position = 0
    if evens == 1:
        for num in numbers:
            position += 1
            if num % 2 == 0:
                return position
    else:
        for num in numbers:
            position += 1
            if num % 2 == 1:
                return position
