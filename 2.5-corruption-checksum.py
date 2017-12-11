# Read file into 2D list
data = []
with open("2-input.txt") as f:
	for line in f:
		items = line.split("\t")
		if(items[0].strip() == ""):
			continue
		currentLine = []
		for item in items:
			currentLine.append(int(item.strip()))
		if len(currentLine) > 0:
			data.append(currentLine)

sum = 0
for row in data:
	rowMin = row[0]
	for item in row:
		for x in row:
			if item % x == 0 and item != x:
				sum += item / x
	rowMax = 0
	rowMin = 0
print(sum)