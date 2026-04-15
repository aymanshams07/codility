def solution(f):
    # f = open("object.txt")
    # print(f)
    # for i in f
    #     print(i)
    # split - split txt line by line or else every char goes in each line, strip- removes white spaces
    line = f.read().split("\n")
    for j in line:
        print("this is j", j)
        print("this is line ", line)
        if len(j.strip().split()) == 1:
            # c = int(j.strip())
            # print(c)
            try:
                converter = int(j.strip())
            except:
                continue
            if -10 ** 9 <= converter <= 10 ** 9:
                yield converter
            else:
                continue
        else:
            continue
        print("this is final line", )


f = open("object.txt")
solution(open("object.txt"))
