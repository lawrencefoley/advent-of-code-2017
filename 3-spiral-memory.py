# distance = |p1 - q1| + |p2 - q2|
# distance = (p1.x - q1.x, p1.y - q1.y)

import math
from pprint import pprint

numIn = 25
# Generate the memory

gridSize = math.ceil(math.sqrt(25))
mem = []
for i in range(gridSize):
	currentRow = []
	for j in range(gridSize):
		currentRow.append(0)
	mem.append(currentRow)

mid = math.floor(gridSize / 2)
mem[mid][mid] = 1
mem[mid][mid + 1] = 2
sequence = []
for i in range(numIn):
	sequence.append(i)

currentPos = [mid, mid]
for i in range(1, 5):
	if i % 2 == 0:
		multiplier = -1
	else:
		multiplier = 1
	for j in range(2):
		if j != 0:
			# TODO Add i * multiplier to x
			currentPos[0] += i * multiplier * -1
			print("y", i * multiplier)
			
		else:
			# TODO Add i * multiplier to y
			currentPos[1] += i * multiplier
			print("x", i * multiplier)
		# pprint(currentPos)
		# mem[]
			
		




