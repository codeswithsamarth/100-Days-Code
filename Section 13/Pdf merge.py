from PyPDF2 import  PdfWriter

merger = PdfWriter()
pdfs = []
n = int(input("Enter The Number of Pdf Merge"))
for i in range(0,n):
    name = input(f"Enter The Name of pdf {i+1}")
    pdfs.append(name)

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged.pdf")
merger.close()
