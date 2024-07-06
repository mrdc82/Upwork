from tkinter import Tk
from tkinter.filedialog import askdirectory as ad
import os
import read_doc
import read_docx
import read_pdf
import read_txt

srcdir = ad(title='Select Source Folder') # shows dialog box and return the path
print(srcdir)
destdir = ad(title='Select Destination Folder') # shows dialog box and return the path
print(destdir)


if __name__ == '__main__':
    # Iterate over files in directory
    for name in os.listdir(srcdir):
        if name.endswith('.doc'):
            read_doc.docfile()
        elif name.endswith('.docx'):
            read_docx.docxfile()
        elif name.endswith('.pdf'):
            read_pdf.pdffile()
        elif name.endswith('.txt'):
            read_txt.txtfile()
        else:
            print(f"{name} Not a valid file")

    #(pd.DataFrame.from_dict(data=pdfdict, orient='index').to_csv('dict_file.csv', header=False))
    #print(pdfdict)
