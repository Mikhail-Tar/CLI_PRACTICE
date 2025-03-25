def model(x: float, k: float=2.0, b: float=0.0):
    return k * x + b

input_data = [1.0, 2, 3, 4, 5, 6, 7, 8, 9, 10]
output_data = [model(x) for x in input_data]

print(output_data)