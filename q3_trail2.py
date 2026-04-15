def solution(file_object):
    lines = file_object.read().split("\n")  # split text read by filereader line by line

    for line in lines:

        if len(line.strip().split()) == 1:  # filter line only which has only one value
            try:
                c = int(line.strip())  # convert str to integer if format is invalid, it throw exceptiont, so we can ignore wrong format.
            except:
                continue

            if - 10 ** 9 <= c <= 10 ** 9:  # check range is in available [-1000000000, 1000000000]
                yield c
                # yield iterator

            else:
                continue
        else:
            continue


file_object = "object.txt"
