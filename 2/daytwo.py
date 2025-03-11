
safe_amount = 0

with open("2/data.txt") as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(" ")
        correct = True
        if int(parts[0]) < int(parts [1]):
            for i in range(len(parts)-1):
                diff = abs(int(parts[i+1]) - int(parts[i]))
                if int(parts[i+1]) < int(parts[i]) or (diff > 3 or diff == 0):
                    correct = False
            if correct:
                #print(f"correct asc: {line}")
                safe_amount += 1
        elif int(parts[0]) > int(parts[1])-1:
            for i in range(len(parts)-1):
                diff = abs(int(parts[i+1]) - int(parts[i]))
                if int(parts[i+1]) > int(parts[i]) or (diff > 3 or diff == 0):
                    correct = False
            if correct:
                safe_amount += 1
                #print(f"correct desc: {line}")

print(safe_amount)
                    





