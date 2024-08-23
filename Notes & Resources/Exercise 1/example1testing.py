data = """1,2,3
4,5,6
"""

handle = open("data.csv", "w")
print(type(handle))
handle.write(data)
handle.close()

handle = open("data.csv")

matrix = []
# while line := handle.readline():
#     matrix.append(line.rstrip())
line = handle.readline()
print(type(line))
cell1 = line[:1]
print(cell1)
print(type(cell1))
cell1 = int(cell1)
print(type(cell1))
print(cell1)