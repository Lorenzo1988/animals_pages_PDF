from fpdf import FPDF
import glob
from pathlib import Path
#PATH
path_input = "input_files/"
path_output="output_files/"

filepaths = glob.glob("input_files/*.txt")
print(filepaths)

#SELEZIONE_FILES

for i, filepath in enumerate(filepaths):
    nome_file = Path(filepath).stem
    #PDF FILES
    pdf = FPDF(orientation="P",format="A4",unit="mm")
    pdf.add_page()
    pdf.set_font(family="Times",size=16,style="B")
    pdf.cell(w=50,h=8,txt= f"{str(nome_file).title()}")
    pdf.output(path_output+"pdf_"+str(nome_file)+".pdf")