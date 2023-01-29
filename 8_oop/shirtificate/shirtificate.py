from fpdf import FPDF

name = input("What's your name? ")
class PDF(FPDF):
    def header(self):
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 38)
        # Moving cursor to the right:
        # Printing title:
        self.cell(w=0, txt="CS50 Shirtificate", align="C")
        # Performing a line break:
        self.ln(20)

    # def background(self):


    def footer(self):
        # Position cursor at 1.5 cm from bottom:
        self.set_y(30)
        # Setting font: helvetica italic 8
        self.set_font("helvetica", "B", 31)
        self.set_text_color(255,255,255)
        self.cell(w=0, h=210, txt=f"{name} took CS50", align="C")


# Instantiation of inherited class

pdf = PDF()
pdf.add_page()
pdf.set_font("Times", size=12)
pdf.image("shirtificate.png", h=pdf.eph, w=pdf.epw, y=50)
pdf.output("shirtificate.pdf")

