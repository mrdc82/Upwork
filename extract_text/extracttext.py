# importing required classes 
from pypdf import PdfReader
import re

def pdfreader(pdfile):
    total = 0
    mydict = {}
    # creating a pdf reader object 
    reader = PdfReader(pdfile) 

    # printing number of pages in pdf file 
    numpages = (len(reader.pages)) 
    #print(numpages)

    # creating a page object 
    for i in range(numpages):
        page = reader.pages[i]

    # extracting text from page 
        extract = (page.extract_text())
        extract = extract.lower()
        extract = re.sub('[()/!:#$,0123456789-]', '', extract)
        paragraph = extract.split(None)

        for i in paragraph:
            if i not in mydict:
                mydict[i] = 0
                mydict[i] += 1
            else:
                mydict[i] += 1    
    print(mydict)

pdfreader('example.pdf')