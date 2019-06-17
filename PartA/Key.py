input={120:"mi",166:"kkr",135:"dc",167:"csk",111:"rcb"}
print(input)

for key in input.keys():
	if key%2==0:
		print(key,input[key])
