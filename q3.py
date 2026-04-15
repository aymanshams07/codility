f = open("object.txt")
print("this is file f",f)

# for i in f:
#     print(i)

# split - split txt line by line or else every char goes in each line, strip- revomes white spaces
line = f.read().split("\n")
for j in line:
    print("this is j", j)
    print("this is line ", line)
    if len(j) == 1:
        c = int(j.strip())
        print(c)
        try:
            converter = int(line.strip())
            print("this is converter", converter)
        except:
            continue
        if -10**9 <= converter <= 10**9:
            print("this is an ex")
        else:
            continue
    else:
        continue
        print("this is current_converter", line)
