import PyPDF2

file = open('dictionary.txt','r')
lst = list(file.readlines())
pdfReader = PyPDF2.PdfFileReader(open('abc1_encrypted.pdf','rb'))
for x in lst:
    y = list(x)
    if '\n' in y:
        y.pop(-1)
    stry = ''.join(map(str,y))
    if pdfReader.decrypt(stry) == 1:
        print("The password for the encrypted PDF file is: " + stry)
        break