import PyPDF2, sys, os
cpath = os.getcwd()
password = sys.argv[1]
file_name_list = []
for x,y,z in os.walk(cpath):
    for a in z:
        if a[-3:] == 'pdf':
            file_name_list.append(a)
for a in file_name_list:
    file_path = x + '/' + a
    pdfFile = open(file_path,'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    pdfWriter = PyPDF2.PdfFileWriter()
    for pageNum in range(pdfReader.numPages):
        pdfWriter.addPage(pdfReader.getPage(pageNum))
    pdfWriter.encrypt(password)
    resultPdf = open(file_path[0:-4] + '_encrypted.pdf', 'wb')
    pdfWriter.write(resultPdf)
    resultPdf.close()

file_name_list2 = []
for x,y,z in os.walk(cpath):
    for a in z:
        if a[-14:] == '_encrypted.pdf':
            file_name_list2.append(a)
for a in file_name_list2:
    pdfReader = PyPDF2.PdfFileReader(open(x + '/' + a, 'rb'))
    if pdfReader.isEncrypted == True:
        os.remove(a[:-14] + '.pdf')
print("Done, ser!")