from fpdf import FPDF
import glob
from pathlib import Path
#PATH
path_input = "input_files/"
path_output="output_files/"

filepaths = glob.glob("input_files/*.txt")
print(filepaths)

#CREO PDF
pdf = FPDF(orientation="P", format="A4", unit="mm")

for i, filepath in enumerate(filepaths):
    pdf.add_page()
    nome_file = Path(filepath).stem
    pdf.set_font(family="Times",size=16,style="B")
    pdf.cell(w=50,h=8,txt= f"{str(nome_file).title()}")

pdf.output(path_output+"animals_pages_PDF.pdf")