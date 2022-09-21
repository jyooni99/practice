def average(data):
    result = sum(data) / len(data)
    return result

def deviation(data):
    avr = average(data)
    result = []

    for i in data:
        sub = i - avr
        sub = round(sub, 1)
        result.append(sub)
    
    return result


def variance(data):
    dev = deviation(data)
    square = []

    for i in dev:
        squ = i ** 2
        square.append(squ)
    
    result = sum(square) / len(square)
    result = round(result, 2)
    return result


result = variance([10,20,30])
print(result)