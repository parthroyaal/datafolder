def generate_number_list(x1, x2, step=50):
    number_list = []
    current_number = x1

    while current_number <= x2:
        number_list.append(current_number)
        current_number += step

    return number_list

# Example usage:
x1 = 25200 #small
x2 = 25300 #large
result = generate_number_list(x1, x2)
print(result)