def test_line(parts, retesting):
    difflist = []
    for i in range(len(parts)-1):
        diff = (int(parts[i+1]) - int(parts[i]))
        difflist.append(diff)
    if all(x < 0 and x >=-3 for x in difflist) or all(x > 0 and x <=3 for x in difflist):
        return True 
    else:
        #only retest if you haven't yet
        if retesting == False:
            if retest_line(parts):
                return True

def retest_line(parts):
    for i in range(len(parts)):
        check = parts[:i] + parts[i+1:]
        if test_line(check, True):
            return True

def main():
    safe_amount = 0
    with open("2/data.txt") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(" ")
            if test_line(parts, False):
                safe_amount += 1

    print(safe_amount)

main()
