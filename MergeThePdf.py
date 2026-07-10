from pypdf import PdfWriter
# import os

merger = PdfWriter()
for pdf in["resume.pdf", "Aditya resume.pdf"   ]:

    merger.append(pdf)
    
merger.write("merged-pdf.pdf")
merger.close()    

