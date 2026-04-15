# S = " We test coders. Give us a try? Why not!"
S = "Forget  CVs..Save your damn time . x x x x x"
print(S)

# for i in S:
#     new = S.split(".")

sentences = []

for i in S.split("."):
    for j in i.split("?"):
        for k in j.split("!"):
            sentences.append(k)
            print(sentences)
            # print(len(sentences))
max_count = -1
for se in sentences:
    if max_count < len(se.split()):
        max_count = len(se.split())
        le_sent = len(se.split())
        print(le_sent)
print(max_count)
