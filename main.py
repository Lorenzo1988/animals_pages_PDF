from fpdf import FPDF
import glob

#PATH
path_input = "input_files/"
path_output="output_files/"

filepaths = glob.glob("input_files")
print(filepaths)

#SELEZIONE_FILES