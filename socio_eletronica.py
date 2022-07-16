import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import PyPDF2

pdf_file=open('F:\dumps\socios\ALARMES 10 A 12 2017 Razão.pdf')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
print(read_pdf)
