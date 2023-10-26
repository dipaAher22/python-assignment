
#method 1

def calculate_area(length, width):
    if length == width:
        return "This is a square!"
    return length * width

length = float(input("Enter length: "))
width = float(input("Enter width: "))

result = calculate_area(length, width)

print("The area of the rectangle is:", result)


#Method 2


def calculate_area(length, width):
    if length == width:
        return "This is a square!"
    else:
        return length * width

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

result = calculate_area(length, width)

print(result)
