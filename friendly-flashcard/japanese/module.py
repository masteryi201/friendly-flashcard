# -*- coding: utf-8 -*-
from sys import argv
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.platypus import Image
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.lib.colors import pink, black, red, blue, green
from reportlab.lib.units import inch
import pandas as pd

script, csv_file, name_pdf = argv
data_file = csv_file
pdfmetrics.registerFont(TTFont('simsun', './font/simsun.ttc'))
pdfmetrics.registerFont(TTFont('hgrge', './font/hgrge.ttc'))
pdfmetrics.registerFont(TTFont('hgrskp', './font/hgrskp.ttf'))
pdfmetrics.registerFont(TTFont('times-new-roman', './font/times-new-roman.ttf'))
output_file_name = "./temp/" + name_pdf + ".pdf"
A4_width = 595
A4_height = 842
def module (data_file) :
	data_frames = pd.read_csv(data_file, header=None)
	number_row = data_frames.shape[0]
	number_col = data_frames.shape[1]
	can = canvas.Canvas(output_file_name, pagesize=A4)
	s12_words(can, data_frames, number_row, number_col)
	can.save()
def s12_words (can, data_frames, number_row, number_col):
	for count_row in range (6) :
		kanji1 = data_frames[0][count_row]
		img_before_1 = data_frames[7][count_row]
		can.rect(0, count_row*140, 298, 140, stroke=1, fill=0)
		if pd.notna(img_before_1) :
			img_before_1 =  './images/' + img_before_1
			can.drawImage(img_before_1, 0, count_row*140, width=200, height=140)
		kanji7 = data_frames[0][count_row + 6]
		img_before_7 = data_frames[7][count_row + 6]
		can.rect(298, count_row*140, 298, 140, stroke=1, fill=0)
		if pd.notna(img_before_7) :
			img_before_7 =  './images/' + img_before_7
			can.drawImage(img_before_7, 298, count_row*140, width=200, height=140)
		display_frames_before(can, kanji1, kanji7, count_row)
	can.showPage()
	for count_row in range (6) :
		onyomi1 = data_frames[1][count_row]
		kunyomi1 = data_frames[2][count_row]
		remember1 = data_frames[3][count_row]
		Han_Viet1 = data_frames[4][count_row]
		meaning1_1 = data_frames[5][count_row]
		meaning1_2 = data_frames[6][count_row]
		img_after_1 = data_frames[8][count_row]
		can.rect(0, count_row*140, 298, 140, stroke=1, fill=0)
		if pd.notna(img_after_1) :
			img_after_1 =  './images/' + img_after_1
			can.drawImage(img_after_1, 0, count_row*140, width=298, height=140)
		onyomi7 = data_frames[1][count_row + 6]
		kunyomi7 = data_frames[2][count_row + 6]
		remember7 = data_frames[3][count_row + 6]
		Han_Viet7 = data_frames[4][count_row + 6]
		meaning7_1 = data_frames[5][count_row + 6]
		meaning7_2 = data_frames[6][count_row + 6]
		img_after_7 = data_frames[8][count_row + 6]
		can.rect(298, count_row*140, 298, 140, stroke=1, fill=0)
		if pd.notna(img_after_7) :
			img_after_7 =  './images/' + img_after_7
			can.drawImage(img_after_7, 298, count_row*140, width=298, height=140)
		display_frames_after(can, onyomi1, kunyomi1, remember1, Han_Viet1,  meaning1_1, meaning1_2, onyomi7, kunyomi7, remember7, Han_Viet7, meaning7_1, meaning7_2, count_row)

def display_frames_before (can, kanji1, kanji7, count_row) :	
	can.setFont('hgrskp', 30, leading=None)
	can.drawString(225, count_row*140 + 70,kanji1)
	can.setFont('hgrskp', 30, leading=None)
	can.drawString(520, count_row*140 + 70, kanji7)
def display_frames_after (can, onyomi1, kunyomi1, remember1, Han_Viet1,  meaning1_1, meaning1_2, onyomi7, kunyomi7, remember7, Han_Viet7, meaning7_1, meaning7_2, count_row) :
	can.setFillColor(blue)
	can.setFont('times-new-roman', 15, leading=None)
	can.drawString(130, count_row*140 + 115,Han_Viet1)
	can.setFont('simsun', 12, leading=None)
	can.drawString(30, count_row*140 + 100,"onyomi :" + onyomi1)
	can.setFont('simsun', 12, leading=None)
	can.drawString(30, count_row*140 + 80,"kunyomi :" + kunyomi1)
	can.setFont('times-new-roman', 10, leading=None)
	can.drawString(30, count_row*140 + 60,remember1)
	can.setFont('simsun', 13, leading=None)
	can.drawString(30, count_row*140 + 40,meaning1_1)
	can.drawString(30, count_row*140 + 20,meaning1_2)

	can.setFont('times-new-roman', 15, leading=None)
	can.drawString(428, count_row*140 + 115,Han_Viet7)
	can.setFont('simsun', 12, leading=None)
	can.drawString(328, count_row*140 + 100,"onyomi :" + onyomi7)
	can.setFont('simsun', 12, leading=None)
	can.drawString(328, count_row*140 + 80,"kunyomi :" + kunyomi7)
	can.setFont('times-new-roman', 10, leading=None)
	can.drawString(328, count_row*140 + 60,remember7)
	can.setFont('simsun', 12, leading=None)
	can.drawString(328, count_row*140 + 40,meaning7_1)
	can.drawString(328, count_row*140 + 20,meaning7_2)
module(data_file)
