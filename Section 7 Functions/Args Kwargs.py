# Args Stands for argument and kwargs stands for keyword argument
# With single args we can pass multiple argument


def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total
print(add(1,2,3,4))

def find_max(*nums):
    return max(nums)

print(max(2,4))

def join_str(*args):
    for string in args:
        return "".join(string)

print(join_str("Samarth","Patil"))

def multiply_all(*nums):
    total = 1
    for num in nums:
        total*=num
        return total

print(multiply_all(11,22,33,44))

def count_even_odd(*args):
    even_count = 0
    odd_count = 0

    for arg in args:
        if arg % 2 == 0:
            even_count +=1
        if arg % 2 != 0:
            odd_count += 1

    return odd_count,even_count

print(count_even_odd(1,2,3))

def calculator(operator,*args):
    if operator == "+":
        return sum(args)
    elif operator == "/":
        result = 1
        for num in args:
            result *= num
        return result
    else:
        print("Unknown Operator")

print(calculator("+",12,13,14,15,22))

def print_address(**kwargs):
    for keys,value in kwargs.items():
        print(f"{keys}:{value}")

print_address(name = 'Samarth Patil',
              city = "Solapur",
              state = "Maharashtra",
              area  = "Mallikarjun Nagar")


def power(base ,exponent = 2):
    return base ** exponent

print(power(2,exponent=9))


