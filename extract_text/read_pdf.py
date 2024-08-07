# importing required classes 
from pypdf import PdfReader
import re
import pandas as pd

def pdffile():

    pdfile = "example.pdf"
    total = 0
    pdfdict = {}
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
        extract = re.sub("[()/!:#$,0123456789-]", "", extract)
        paragraph = extract.split(None)

        for i in paragraph:
            if i not in pdfdict:
                pdfdict[i] = 0
                pdfdict[i] += 1
            else:
                pdfdict[i] += 1

    print(pdfdict)

    #write dictionary to csv file
    pd.DataFrame.from_dict(data=pdfdict, orient='index').to_csv('wordcount.csv', header=False)


if __name__ == '__main__':
    pdffile()
