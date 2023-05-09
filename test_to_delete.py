from fpdf import FPDF
import glob
from pathlib import Path
#PATH
path_input = "input_files/"
path_output="output_files/"

filepaths = glob.glob("input_files/*.txt")

for i, filepath in enumerate(filepaths):
    print(i)
    print(filepath)
    with open(filepath,"r") as file:
        testo = file.readline()
        print(testo)
    print("\n\n")