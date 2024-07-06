docdict = {}

with open("example.doc","r") as file:
    x = file.read()
    x = x.split(None)

    for word in x:
        if word not in docdict:
            docdict[word] = 0
            docdict[word] += 1
        else:
            docdict[word] += 1  

print(docdict)