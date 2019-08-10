numbers = list(range(100))
binary = [bin(num)[2:] for num in numbers]
new_numbers = [int(b, 2) for b in binary]

print(binary)

