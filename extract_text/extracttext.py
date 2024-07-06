# importing required classes 
from pypdf import PdfReader 

def pdfreader():
    total = 0
    # creating a pdf reader object 
    reader = PdfReader('example.pdf') 

    # printing number of pages in pdf file 
    numpages = (len(reader.pages)) 
    print(numpages)

    # creating a page object 
    for i in range(numpages):
        page = reader.pages[i]

    # extracting text from page 
        extract = (page.extract_text())
        extract = extract.lower()
        extract = extract.replace('\n','')
        paragraph = extract.split(' ')
        #paragraph = extract.strip('\n')

        mydict = {}

        for i in paragraph:
            #with open("words.txt", "a+") as words:
            #reading = words.read()
            if i not in mydict:
                mydict[i] = 0
                mydict[i] += 1
            else:
                mydict[i] += 1    
    print(mydict)

pdfreader()