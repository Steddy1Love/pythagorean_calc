side_a = int(input("Input side a: "))
side_b = int(input("Input side b: "))
print(f"The width of the triangle is: {side_a}")
print(f"The height of the triangle is: {side_b}")

side_c = (side_a ** 2 + pow(side_b, 2)) ** (1/2)

print(f"C equals: {side_c}")