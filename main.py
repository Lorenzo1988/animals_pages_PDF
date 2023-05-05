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
    print(i)
    nome_file = Path(filepath).stem
    print(nome_file)