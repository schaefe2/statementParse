import PyPDF2

pdfFileObj = open('pdfs/statement1.pdf', 'rb')

pdfReader = PyPDF2.PdfReader(pdfFileObj)

print(len(pdfReader.pages))

for page in pdfReader.pages:
    lines = page.extract_text().split('\n')
    inTrans = 0
    for line in lines:
        if line[0].isnumeric() and inTrans:
            #transaction line
            print(line)
        elif line == "Purchases and Adjustments":
            inTrans = 1
        else:
            inTrans = 0



pdfFileObj.close()