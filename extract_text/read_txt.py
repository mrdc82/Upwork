txtdict = {}

with open("example.txt","r") as file:
    x = file.read()
    x = x.split(None)

    for word in x:
        if word not in txtdict:
            txtdict[word] = 0
            txtdict[word] += 1
        else:
            txtdict[word] += 1  

print(txtdict)