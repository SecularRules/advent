list1 = []
list2 = []

# added folder and put file in it, but it couldnt find it? it can now
with open("1/data.txt") as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split("   ")
        list1.append(int(parts[0]))
        list2.append(int(parts[1]))

list1.sort()
list2.sort()

totaldif = 0

for i in range(len(list1)):
    dif = abs(list1[i] - list2[i])
    totaldif += dif

print(totaldif)

# part 2

similarity_score = 0

for i in list1:
    amount = list2.count(i)
    score = i * amount
    similarity_score += score

print(similarity_score)
