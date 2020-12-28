import PyPDF2, sys, os
cpath = os.getcwd()
file_name_list = []
for x,y,z in os.walk(cpath):
    for a in z:
        if a[-3:] == 'pdf':
            file_name_list.append(a)
for a in file_name_list:
    pdfReader = PyPDF2.PdfFileReader(open(x + '/' + a, 'rb'))
    if pdfReader.isEncrypted == True:
        k = str(input("Please enter the password for the file: " + a))
        if pdfReader.decrypt(k) == 1:
            pdfReader.decrypt(k)
            print("The password {} is correct".format(k))
        else:
            print("The password {} is wrong.".format(k))
print("Done, ser!")