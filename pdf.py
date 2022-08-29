import PyPDF2
import sys 
import glob
import os


path =r'C:\Users\DELL\Documents\Python Scripts\pdf'
rawdfs = glob.glob(path + "/*.pdf")
inputs=[]
for rawdf in rawdfs:
    newfile=os.path.basename(rawdf)
    inputs.append(newfile)

# inputs=sys.argv[1:]

merger=PyPDF2.PdfFileMerger()

for file in inputs:
    merger.append(file)
merger.write('tender_document.pdf')