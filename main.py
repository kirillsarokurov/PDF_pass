from PyPDF2 import PdfWriter,PdfReader
import getpass

pdfwriter = PdfWriter()


pdf = PdfReader('DIC Swatch ReadMe.pdf')

for page in range(len(pdf.pages)):
    pdfwriter.add_page(pdf.pages[page])
admin_psw = 'admin'
psw = getpass.getpass(prompt='Password: ')
if psw == admin_psw:
    pdfwriter.encrypt(admin_psw)
else:
    print('You are not allowed to')


with open('protected.pdf', 'wb') as file:
    pdfwriter.write(file)


