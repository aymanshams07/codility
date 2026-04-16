# function for even or odd

def even_or_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"


print(even_or_odd(4))


## one possible soln
filters = [1,2,3,4]
for i in filters:
    addition = filters[0]+ filters[1] + filters[2] + filters[3]

print(addition)

## soln 2


def sum_numbers(numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum
        #print(sum)

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(sum_numbers(numbers))

