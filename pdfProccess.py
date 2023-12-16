import PyPDF2

pdfFileObj = open('statementParse\pdfs\statement1.pdf', 'rb')

pdfReader = PyPDF2.PdfReader(pdfFileObj)

print(len(pdfReader.pages))

for page in pdfReader.pages:
    lines = page.extract_text().split('\n')
    inTrans = 0
    for line in lines:
        if line[0].isnumeric() and inTrans:
            txt = line.split(' ')
            transactionDate = line[:5]
            vendor = line[12:37].strip()
            price = txt[-1]
            print(f"{transactionDate} {vendor} {price}")
        elif line == "Purchases and Adjustments":
            inTrans = 1
        else:
            inTrans = 0



pdfFileObj.close()