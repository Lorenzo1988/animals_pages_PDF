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

    ###RECUPERO TESTO DEI FILES
    with open(filepath, "r") as file:
        testo = file.readline()

    # CREO PDF
    pdf.add_page()
    nome_file = Path(filepath).stem
    pdf.set_font(family="Times",size=16,style="B")
    #TITOLO PAGINA
    pdf.cell(w=50,h=8,txt= f"{str(nome_file).title()}",ln=1)

    # TESTO PAGINA
    pdf.set_font(family="Times",size=10)
    pdf.multi_cell(w=0,h=6,txt= testo)

pdf.output(path_output+"animals_pages_PDF.pdf")