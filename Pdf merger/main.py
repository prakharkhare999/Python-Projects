import PyPDF2

pdfiles=["sample1.pdf",'sample2.pdf']
merger = PyPDF2.PdfMerger()
for filename in pdfiles:
    pdfFile = open(filename,'rb')
    pdfReader=PyPDF2.PdfReader(pdfFile)
    merger.append(pdfReader)
pdfFile.close()
merger.write('merger.pdf')