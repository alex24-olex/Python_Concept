import PyPDF2

pdf_file = open('/Users/kbhatnagar/Desktop/rahul/python/Enrollment_Form_filled.pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()
print(number_of_pages)
page = read_pdf.getPage(0)
page_content = page.extractText()
print(page_content)
