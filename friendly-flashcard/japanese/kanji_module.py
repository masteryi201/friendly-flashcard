# -*- coding: utf-8 -*-
import os
from sys import argv
import numpy as np
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.platypus import Image
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.lib.colors import Color, pink, black, red, blue, green
from reportlab.lib.units import inch
import pandas as pd
script, csv_file, name_pdf, path_image = argv
data_file = csv_file
pdfmetrics.registerFont(TTFont('simsun', './font/simsun.ttc'))
pdfmetrics.registerFont(TTFont('hgrge', './font/hgrge.ttc'))
pdfmetrics.registerFont(TTFont('hgrskp', './font/hgrskp.ttf'))
pdfmetrics.registerFont(TTFont('times-new-roman', './font/times-new-roman.ttf'))
output_file_name = "./temp/" + name_pdf + ".pdf"
A4_width = 595
A4_height = 842
def module (data_file) :
	data_images = os.listdir(path_image)
	data_frames = pd.read_csv(data_file, header=None)
	number_row = data_frames.shape[0]
	number_col = data_frames.shape[1]
	can = canvas.Canvas(output_file_name, pagesize=A4)
	s12_words(can, data_frames, number_row, number_col, data_images)
	can.save()
def s12_words (can, data_frames, number_row, number_col, data_images):
	for count_row in range (4) :
		kanji1 = data_frames[0][count_row]
		img_before_1 = data_frames[9][count_row]
		can.setFillColorRGB(255, 255, 255)
		can.rect(0,count_row*210.5,298, 210.5,fill=1)
		can.rect(0, count_row*210.5, 298, 210.5, stroke=1, fill=0)
		if pd.notna(img_before_1) :
			img_before_1 =  image(data_images,img_before_1,path_image)
			can.drawImage(img_before_1, 40, count_row*210.5 + 40, width=150, height=130)
		can.roundRect(40, count_row*210.5 + 40, 150, 130, 2, fill=0)
		kanji5 = data_frames[0][count_row + 4]
		img_before_5 = data_frames[9][count_row + 4]
		can.rect(298,count_row*210.5,298, 210.5,fill=1)
		can.rect(298, count_row*210.5, 298, 210.5, stroke=1, fill=0)
		if pd.notna(img_before_5) :
			img_before_5 =  image(data_images,img_before_5,path_image)
			can.drawImage(img_before_5, 338, count_row*210.5 + 40, width=150, height=130)
		can.roundRect(338, count_row*210.5 + 40, 150, 130, 2, fill=0)
		display_frames_before(can, kanji1, kanji5, count_row)
	can.showPage()
	for count_row in range (4) :
		onyomi1 = data_frames[1][count_row]
		kunyomi1 = data_frames[2][count_row]
		remember1 = data_frames[3][count_row]
		Han_Viet1 = data_frames[4][count_row]
		meaning1_1 = data_frames[5][count_row]
		meaning1_2 = data_frames[6][count_row]
		meaning1_3 = data_frames[7][count_row]
		meaning1_4 = data_frames[8][count_row]
		img_after_1 = data_frames[10][count_row]
		can.setFillColorRGB(255, 255, 255)
		can.rect(0,count_row*210.5,298, 210.5,fill=1)
		can.rect(0, count_row*210.5, 298, 210.5, stroke=1, fill=0)
		if pd.notna(img_after_1) :
			img_after_1 =  image(data_images,img_after_1,path_image)
			can.drawImage(img_after_1, 0, count_row*210.5, width=298, height=210.5)
		onyomi5 = data_frames[1][count_row + 4]
		kunyomi5 = data_frames[2][count_row + 4]
		remember5 = data_frames[3][count_row + 4]
		Han_Viet5 = data_frames[4][count_row + 4]
		meaning5_1 = data_frames[5][count_row + 4]
		meaning5_2 = data_frames[6][count_row + 4]
		meaning5_3 = data_frames[7][count_row + 4]
		meaning5_4 = data_frames[8][count_row + 4]
		img_after_5 = data_frames[10][count_row + 4]
		can.rect(298, count_row*210.5,298, 210.5,fill=1)
		can.rect(298, count_row*210.5, 298, 210.5, stroke=1, fill=0)
		if pd.notna(img_after_5) :
			img_after_5 =  image(data_images,img_after_5,path_image)
			can.drawImage(img_after_5, 298, count_row*210.5, width=298, height=210.5)
		display_frames_after(can, onyomi1, kunyomi1, remember1, Han_Viet1,  meaning1_1, meaning1_2, meaning1_3, meaning1_4, onyomi5, kunyomi5, remember5, Han_Viet5, meaning5_1, meaning5_2, meaning5_3, meaning5_4, count_row)

def display_frames_before (can, kanji1, kanji7, count_row) :
	can.setFillColor(black)	
	can.setFont('hgrskp', 70, leading=None)
	can.drawString(205, count_row*210.5 + 80,kanji1)
	can.setFont('hgrskp', 70, leading=None)
	can.drawString(500, count_row*210.5 + 80, kanji7)
def display_frames_after (can, onyomi1, kunyomi1, remember1, Han_Viet1,  meaning1_1, meaning1_2, meaning1_3, meaning1_4, onyomi5, kunyomi5, remember5, Han_Viet5, meaning5_1, meaning5_2, meaning5_3, meaning5_4, count_row) :
	can.setFillColor(black)	
	can.setFont('times-new-roman', 20, leading=None)
	can.drawCentredString(150, count_row*210.5 + 170,Han_Viet1)
	can.setFont('simsun', 14, leading=None)
	can.drawString(25, count_row*210.5 + 150,"★訓 :" + onyomi1)
	can.setFont('simsun', 14, leading=None)
	can.drawString(25, count_row*210.5 + 130,"★音 :" + kunyomi1)
	can.setFont('times-new-roman', 12, leading=None)
	can.drawString(25, count_row*210.5 + 110,remember1)
	can.setFont('simsun', 14, leading=None)
	if meaning1_1 != "_" :
		meaning_ja = ja(meaning1_1)
		meaning_vi = vi(meaning1_1,len(meaning_ja),len(meaning1_1))
		can.setFont('simsun', 14, leading=None)
		can.drawString(25, count_row*210.5 + 90,meaning_ja)
		can.setFont('times-new-roman', 13, leading=None)
		can.drawString(25+len(meaning_ja)*5, count_row*210.5 + 90,meaning_vi)	
	if meaning1_2 != "_" :
		meaning_ja = ja(meaning1_2)
		meaning_vi = vi(meaning1_2,len(meaning_ja),len(meaning1_2))
		can.setFont('simsun', 14, leading=None)
		can.drawString(25, count_row*210.5 + 70,meaning_ja)
		can.setFont('times-new-roman', 13, leading=None)
		can.drawString(25+len(meaning_ja)*5, count_row*210.5 + 70,meaning_vi)	
	if meaning1_3 != "_" :
		meaning_ja = ja(meaning1_3)
		meaning_vi = vi(meaning1_3,len(meaning_ja),len(meaning1_3))
		can.setFont('simsun', 14, leading=None)
		can.drawString(25, count_row*210.5 + 50,meaning_ja)
		can.setFont('times-new-roman', 13, leading=None)
		can.drawString(25+len(meaning_ja)*5, count_row*210.5 + 50,meaning_vi)
	if meaning1_4 != "_" :
		meaning_ja = ja(meaning1_4)
		meaning_vi = vi(meaning1_4,len(meaning_ja),len(meaning1_4))
		can.setFont('simsun', 14, leading=None)
		can.drawString(25, count_row*210.5 + 30,meaning_ja)
		can.setFont('times-new-roman', 13, leading=None)
		can.drawString(25+len(meaning_ja)*5, count_row*210.5 + 30,meaning_vi)

	can.setFont('times-new-roman', 15, leading=None)
	can.drawCentredString(448, count_row*210.5 + 170,Han_Viet5)
	can.setFont('simsun', 12, leading=None)
	can.drawString(323, count_row*210.5 + 150,"★訓 :" + onyomi5)
	can.setFont('simsun', 12, leading=None)
	can.drawString(323, count_row*210.5 + 130,"★音 :" + kunyomi5)
	can.setFont('times-new-roman', 12, leading=None)
	can.drawString(323, count_row*210.5 + 110,remember5)
	can.setFont('simsun', 14, leading=None)
	if meaning5_1 != "_" :
		meaning_ja = ja(meaning5_1)
		meaning_vi = vi(meaning5_1,len(meaning_ja),len(meaning5_1))
		can.setFont('simsun', 14, leading=None)
		can.drawString(323, count_row*210.5 + 90,meaning_ja)
		can.setFont('times-new-roman', 13, leading=None)
		can.drawString(323+len(meaning_ja)*5, count_row*210.5 + 90,meaning_vi)	
	if meaning5_2 != "_" :
		meaning_ja = ja(meaning5_2)
		meaning_vi = vi(meaning5_2,len(meaning_ja),len(meaning5_2))
		can.setFont('simsun', 14, leading=None)
		can.drawString(323, count_row*210.5 + 70,meaning_ja)
		can.setFont('times-new-roman', 13, leading=None)
		can.drawString(323+len(meaning_ja)*5, count_row*210.5 + 70,meaning_vi)	
	if meaning5_3 != "_" :
		meaning_ja = ja(meaning5_3)
		meaning_vi = vi(meaning5_3,len(meaning_ja),len(meaning5_3))
		can.setFont('simsun', 14, leading=None)
		can.drawString(323, count_row*210.5 + 50,meaning_ja)
		can.setFont('times-new-roman', 13, leading=None)
		can.drawString(323+len(meaning_ja)*5, count_row*210.5 + 50,meaning_vi)
	if meaning5_4 != "_" :
		meaning_ja = ja(meaning5_4)
		meaning_vi = vi(meaning5_4,len(meaning_ja),len(meaning5_4))
		can.setFont('simsun', 14, leading=None)
		can.drawString(323, count_row*210.5 + 30,meaning_ja)
		can.setFont('times-new-roman', 13, leading=None)
		can.drawString(323+len(meaning_ja)*5, count_row*210.5 + 30,meaning_vi)
def ja(value):
	meaning_len = len(value)
	japanese = ""
	for i in range (meaning_len):
		char1 = value[i]
		if char1 != "/" :
			japanese += char1
		else:
			break
	return japanese
def vi(value,len_ja,len_all):
	vietnamese = ""
	VI_len_start = len_ja + 1
	while VI_len_start <= len_all:
		char2 = value[VI_len_start-1]
		vietnamese += char2
		VI_len_start += 1
	return vietnamese
def image(data_images,img,path_image):
	extension=['.png','.jpeg','.jpg']
	if type(img) is np.int64 :
		img = img.astype(str)
	elif type(img) is np.int32 :
		img = img.astype(str)
	elif type(img) is np.float64 :
		img = img.astype(int)
		img = img.astype(str)
	elif type(img) is np.float32 :
		img = img.astype(int)
		img = img.astype(str)
	else :
		print(type(img))
	print(img)
	print(type(img))
	for i in range(3):
		file_name = img + extension[i-1]
		if file_name in data_images:
			print(file_name)
			return path_image + file_name
module(data_file)
