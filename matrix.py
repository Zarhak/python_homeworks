import random

def generate_random_matrix(rows, cols):
    return [[random.randint(1, 100) for _ in range(cols)] for _ in range(rows)]

def get_column_sum(matrix, column_index):
    return sum(row[column_index] for row in matrix)

def get_row_average(matrix, row_index):
    row_values = matrix[row_index]
    return sum(row_values) / len(row_values)

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix = generate_random_matrix(rows, cols)
print("Generated Matrix:")
for row in matrix:
    print(row)

column_index = int(input("Enter the column index to calculate sum: "))
column_sum = get_column_sum(matrix, column_index)
print(f"\nSum of Column {column_index + 1}: {column_sum}")

row_index = int(input("Enter the row index to calculate average: "))
row_average = get_row_average(matrix, row_index)
print(f"Average of Row {row_index + 1}: {row_average}")
