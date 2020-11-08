import PyPDF2 as ppdf
import pyttsx3 as tts

# Reading text from pdf file
file_path = r'D:\Programming_Projects\PYTHON\PDF2Audio\f60_What every Body is saying.pdf'
pdf = open(file_path, 'rb')
file = ppdf.PdfFileReader(pdf)

txt = ''
num_of_pages = file.getNumPages()
for num in range(1,num_of_pages):
    page = file.getPage(num)
    txt += page.extractText()

# Audio Read file content
tts.speak(txt)
pdf.close()
