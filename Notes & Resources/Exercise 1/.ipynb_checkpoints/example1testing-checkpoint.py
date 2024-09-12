data = """1,2,3
4,5,6
7,8,9
"""

handle = open("data.csv", "w")
handle.write(data)
handle.close()

handle = open("data.csv")

matrix = []
# while line := handle.readline():
#     matrix.append(line.rstrip())


for line in handle:
    row = line.split(',')
    row = [float(value) for value in row]
    matrix.append(row)

print(matrix)


def sum_columns(matrix):
    totals = []
    
    for cols in range (len(matrix[0])):
        result = 0
        for rows in range (len(matrix)):
            result += matrix[rows][cols]
            
        totals.append(result)
        
    return totals

def sum_rows(matrix):
    totals = []
    
    for rows in range(len(matrix)):
        result = 0
        for cols in range (len(matrix[0])):
            result += matrix[rows][cols]
            
        totals.append(result)
        
    return totals
        
test1 = sum_rows(matrix)
test2 = sum_columns(matrix)
print (test1)
print(test2)

test3 = "start"
print(test3[1])
    # for cols in range(len(matrix[0])):
    #     result = 0
    #     for rows in range(len(matrix)):
            










# line = handle.readline()
# print(type(line))
# print("Line: ", line)
# cell1 = line[:1]
# cell2 = line[2:3]
# cell3 = line[4:]
# print("Cell 1: ", cell1)
# print("Cell 2: ", cell2)
# print("Cell 3: ", cell3)
# print(type(cell1))
# cell1 = float(cell1)
# cell2 = float(cell2)
# cell3 = float(cell3)
# print(type(cell1))
# print(cell1)

# matrix.append([cell1, cell2, cell3])
# print(matrix)