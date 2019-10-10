from sys import argv
import os
import pandas as pd
import math
from PyPDF2 import PdfFileMerger
script, csv_file, path_image = argv
data_file = csv_file
results_file = './temp/results.csv'
def main (data_file) :
	list_file = []
	cp_data = pd.read_csv(data_file, header=0)
	number_row = cp_data.shape[0]
	num_page = math.ceil(float(number_row) / 8.0)
	missing = num_page * 8 - number_row
	cp_data.to_csv(results_file, index=False, header=False)
	data_frames = pd.read_csv(results_file, header=None)
	if missing != 0.0 :
		for i in range (int(missing)):
			add_row(data_frames, [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '', ''])
	print(data_frames)
	for i in range(int(num_page)) :
		list_file.append('file_' + str(i) + '.pdf')
		mycmd = 'python kanji_module.py ' + results_file + ' file_' + str(i) + " " + path_image
		os.system(mycmd)
		data_frames = data_frames.iloc[8:]
		data_frames.to_csv(results_file, index=False, header=False)
	pooled(list_file)
	remove()
def add_row(df, row):
    df.loc[-1] = row
    df.index = df.index + 1  
    return df.sort_index()

def pooled(list_file):
	path = './temp/'
	pdf_files = list_file
	merger =  PdfFileMerger()
	for files in pdf_files:
		merger.append(path+files)
	merger.write('../output/output.pdf')
	merger.close()
def remove():
	remove_code = 'rm ./temp/*'
	os.system(remove_code)
main (data_file)
