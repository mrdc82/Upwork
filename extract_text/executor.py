from tkinter import Tk
from tkinter.filedialog import askdirectory as ad
import os
import read_doc
import read_docx
import read_pdf
import read_txt
import csv

srcdir = ad(title='Select Source Folder') # shows dialog box and return the path
print(srcdir)
destdir = ad(title='Select Destination Folder') # shows dialog box and return the path
print(destdir)


if __name__ == '__main__':
    # Iterate over files in directory
    for fname in os.listdir(srcdir):
        if fname.endswith('.doc'):
            read_doc.docfile()
        elif fname.endswith('.docx'):
            read_docx.docxfile()
        elif fname.endswith('.pdf'):
            read_pdf.pdffile()
        elif fname.endswith('.txt'):
            read_txt.txtfile()
        else:
            print(f"{fname} is invalid")