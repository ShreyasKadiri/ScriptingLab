string1=["I am going not coming today", "well done", "Strings editing", "Give it"]
print(string1)

for i in range(len(string1)):
	if i%2==0:
		print("At index", i ,string1[i])

for i in range(len(string1)):
	if i%3==0:
		string1[i]=string1[i].upper()
print(string1)

for i in range(len(string1)):
	string1[i]=" ".join(reversed(string1[i].split()))
print("On reversal",string1)

num=[]
for i in range(len(string1)):
	for s in string1[i].split():
		 if s.isdigit():
		 	num.append(s)
		 	
print(num)
