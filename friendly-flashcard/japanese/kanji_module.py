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
height_layer = 5
width_layer = 2
height_layer_size = A4_height / height_layer
width_layer_size = A4_width / width_layer
def module (data_file) :
	data_images = os.listdir(path_image)
	data_frames = pd.read_csv(data_file, header=None)
	number_row = data_frames.shape[0]
	number_col = data_frames.shape[1]
	can = canvas.Canvas(output_file_name, pagesize=A4)
	s12_words(can, data_frames, number_row, number_col, data_images)
	can.save()
def s12_words (can, data_frames, number_row, number_col, data_images):
	for count_row in range (height_layer) :
		kanji1 = data_frames[0][count_row]
		img_before_1 = data_frames[9][count_row]
		can.setFillColorRGB(255, 255, 255)
		can.rect(0,count_row*height_layer_size,width_layer_size, height_layer_size,fill=1)
		can.rect(0, count_row*height_layer_size, width_layer_size, height_layer_size, stroke=1, fill=0)
		if pd.notna(img_before_1) :
			img_before_1 =  image(data_images,img_before_1,path_image)
			can.drawImage(img_before_1, 40, count_row*height_layer_size + height_layer_size*0.155, width=130, height=110)
		can.roundRect(40, count_row*height_layer_size + height_layer_size*0.155, 130, 110, 2, fill=0)
		kanji5 = data_frames[0][count_row + height_layer]
		img_before_5 = data_frames[9][count_row + height_layer]
		can.rect(width_layer_size,count_row*height_layer_size,width_layer_size, height_layer_size,fill=1)
		can.rect(width_layer_size, count_row*height_layer_size, width_layer_size, height_layer_size, stroke=1, fill=0)
		if pd.notna(img_before_5) :
			img_before_5 =  image(data_images,img_before_5,path_image)
			can.drawImage(img_before_5, 338, count_row*height_layer_size + height_layer_size*0.155, width=130, height=110)
		can.roundRect(338, count_row*height_layer_size + height_layer_size*0.155, 130, 110, 2, fill=0)
		display_frames_before(can, kanji1, kanji5, count_row)
	can.showPage()
	for count_row in range (height_layer) :
		onyomi1 = data_frames[1][count_row]
		kunyomi1 = data_frames[2][count_row]
		Han_Viet1 = data_frames[3][count_row]
		meaning1_1 = data_frames[4][count_row]
		meaning1_2 = data_frames[5][count_row]
		meaning1_3 = data_frames[6][count_row]
		meaning1_4 = data_frames[7][count_row]
		exception1 = data_frames[8][count_row]
		img_after_1 = data_frames[10][count_row]
		can.setFillColorRGB(255, 255, 255)
		can.rect(0,count_row*height_layer_size,width_layer_size, height_layer_size,fill=1)
		can.rect(0, count_row*height_layer_size, width_layer_size, height_layer_size, stroke=1, fill=0)
		if pd.notna(img_after_1) :
			img_after_1 =  image(data_images,img_after_1,path_image)
			can.drawImage(img_after_1, 0, count_row*height_layer_size, width=width_layer_size, height=height_layer_size)
		onyomi5 = data_frames[1][count_row + height_layer]
		kunyomi5 = data_frames[2][count_row + height_layer]
		Han_Viet5 = data_frames[3][count_row + height_layer]
		meaning5_1 = data_frames[4][count_row + height_layer]
		meaning5_2 = data_frames[5][count_row + height_layer]
		meaning5_3 = data_frames[6][count_row + height_layer]
		meaning5_4 = data_frames[7][count_row + height_layer]
		exception5 = data_frames[8][count_row + height_layer]
		img_after_5 = data_frames[10][count_row + height_layer]
		can.rect(width_layer_size, count_row*height_layer_size,width_layer_size, height_layer_size,fill=1)
		can.rect(width_layer_size, count_row*height_layer_size, width_layer_size, height_layer_size, stroke=1, fill=0)
		if pd.notna(img_after_5) :
			img_after_5 =  image(data_images,img_after_5,path_image)
			can.drawImage(img_after_5, width_layer_size, count_row*height_layer_size, width=width_layer_size, height=height_layer_size)
		display_frames_after(can, onyomi1, kunyomi1, exception1, Han_Viet1,  meaning1_1, meaning1_2, meaning1_3, meaning1_4, onyomi5, kunyomi5, exception5, Han_Viet5, meaning5_1, meaning5_2, meaning5_3, meaning5_4, count_row)

def display_frames_before (can, kanji1, kanji7, count_row) :
	can.setFillColor(black)
	can.setFont('hgrskp', 65, leading=None)
	can.drawString(195, count_row*height_layer_size + height_layer_size*0.38,kanji1)
	can.setFont('hgrskp', 65, leading=None)
	can.drawString(490, count_row*height_layer_size + height_layer_size*0.38, kanji7)
def display_frames_after (can, onyomi1, kunyomi1, exception1, Han_Viet1,  meaning1_1, meaning1_2, meaning1_3, meaning1_4, onyomi5, kunyomi5, exception5, Han_Viet5, meaning5_1, meaning5_2, meaning5_3, meaning5_4, count_row) :
	can.setFillColor(black)
	can.setFont('times-new-roman', 20, leading=None)
	can.drawCentredString(448, count_row*height_layer_size + height_layer_size/1.238,Han_Viet1)
	can.setFont('simsun', 14, leading=None)
	can.drawString(323, count_row*height_layer_size + height_layer_size/1.403,"★訓 :" + onyomi1)
	can.setFont('simsun', 14, leading=None)
	can.drawString(323, count_row*height_layer_size + height_layer_size/1.619,"★音 :" + kunyomi1)
	can.setFont('times-new-roman', 12, leading=None)
	can.drawString(323, count_row*height_layer_size + height_layer_size/1.914,"Ví dụ :")
	can.setFont('simsun', 14, leading=None)
	if meaning1_1 != "_" :
		meaning_ja = ja(meaning1_1)
		meaning_vi = vi(meaning1_1,len(meaning_ja),len(meaning1_1))
		can.setFont('simsun', 13, leading=None)
		meaning_ja = correction(meaning_ja)
		can.drawString(323, count_row*height_layer_size + height_layer_size/2.339,"- "+meaning_ja)
		can.setFont('times-new-roman', 12, leading=None)
		can.drawString(323+len(meaning_ja)*5, count_row*height_layer_size + height_layer_size/2.339,meaning_vi)	
	if meaning1_2 != "_" :
		meaning_ja = ja(meaning1_2)
		meaning_vi = vi(meaning1_2,len(meaning_ja),len(meaning1_2))
		can.setFont('simsun', 13, leading=None)
		meaning_ja = correction(meaning_ja)
		can.drawString(323, count_row*height_layer_size + height_layer_size/3.007,"- "+meaning_ja)
		can.setFont('times-new-roman', 12, leading=None)
		can.drawString(323+len(meaning_ja)*5, count_row*height_layer_size + height_layer_size/3.007,meaning_vi)	
	if meaning1_3 != "_" :
		meaning_ja = ja(meaning1_3)
		meaning_vi = vi(meaning1_3,len(meaning_ja),len(meaning1_3))
		can.setFont('simsun', 13, leading=None)
		meaning_ja = correction(meaning_ja)
		can.drawString(323, count_row*height_layer_size + height_layer_size/4.21,"- "+meaning_ja)
		can.setFont('times-new-roman', 12, leading=None)
		can.drawString(323+len(meaning_ja)*5, count_row*height_layer_size + height_layer_size/4.21,meaning_vi)
	if meaning1_4 != "_" :
		meaning_ja = ja(meaning1_4)
		meaning_vi = vi(meaning1_4,len(meaning_ja),len(meaning1_4))
		can.setFont('simsun', 13, leading=None)
		meaning_ja = correction(meaning_ja)
		can.drawString(323, count_row*height_layer_size + height_layer_size/7.012,"- "+meaning_ja)
		can.setFont('times-new-roman', 12, leading=None)
		can.drawString(323+len(meaning_ja)*5, count_row*height_layer_size + height_layer_size/7.012,meaning_vi)
	if exception1 != "_" :
		can.setFillColor(red)
		meaning_ja = ja(exception1)
		meaning_vi = vi(exception1,len(meaning_ja),len(exception1))
		can.setFont('simsun', 11, leading=None)
		meaning_ja = exception_correction(meaning_ja)
		can.drawString(323, count_row*height_layer_size + height_layer_size/13.5,"* "+meaning_ja)
		can.setFont('times-new-roman', 10, leading=None)
		can.drawString(323+len(meaning_ja)*5, count_row*height_layer_size + height_layer_size/13.5,meaning_vi)
		can.setFillColor(black)

	can.setFont('times-new-roman', 20, leading=None)
	can.drawCentredString(150, count_row*height_layer_size + height_layer_size/1.238,Han_Viet5)
	can.setFont('simsun', 14, leading=None)
	can.drawString(25, count_row*height_layer_size + height_layer_size/1.403,"★訓 :" + onyomi5)
	can.setFont('simsun', 14, leading=None)
	can.drawString(25, count_row*height_layer_size + height_layer_size/1.619,"★音 :" + kunyomi5)
	can.setFont('times-new-roman', 12, leading=None)
	can.drawString(25, count_row*height_layer_size + height_layer_size/1.914,"Ví dụ :")
	can.setFont('simsun', 14, leading=None)
	if meaning5_1 != "_" :
		meaning_ja = ja(meaning5_1)
		meaning_vi = vi(meaning5_1,len(meaning_ja),len(meaning5_1))
		can.setFont('simsun', 13, leading=None)
		meaning_ja = correction(meaning_ja)
		can.drawString(25, count_row*height_layer_size + height_layer_size/2.339,"- "+meaning_ja)
		can.setFont('times-new-roman', 12, leading=None)
		can.drawString(25+len(meaning_ja)*5, count_row*height_layer_size + height_layer_size/2.339,meaning_vi)	
	if meaning5_2 != "_" :
		meaning_ja = ja(meaning5_2)
		meaning_vi = vi(meaning5_2,len(meaning_ja),len(meaning5_2))
		can.setFont('simsun', 13, leading=None)
		meaning_ja = correction(meaning_ja)
		can.drawString(25, count_row*height_layer_size + height_layer_size/3.007,"- "+meaning_ja)
		can.setFont('times-new-roman', 12, leading=None)
		can.drawString(25+len(meaning_ja)*5, count_row*height_layer_size + height_layer_size/3.007,meaning_vi)	
	if meaning5_3 != "_" :
		meaning_ja = ja(meaning5_3)
		meaning_vi = vi(meaning5_3,len(meaning_ja),len(meaning5_3))
		can.setFont('simsun', 13, leading=None)
		meaning_ja = correction(meaning_ja)
		can.drawString(25, count_row*height_layer_size + height_layer_size/4.21,"- "+meaning_ja)
		can.setFont('times-new-roman', 12, leading=None)
		can.drawString(25+len(meaning_ja)*5, count_row*height_layer_size + height_layer_size/4.21,meaning_vi)
	if meaning5_4 != "_" :
		meaning_ja = ja(meaning5_4)
		meaning_vi = vi(meaning5_4,len(meaning_ja),len(meaning5_4))
		can.setFont('simsun', 13, leading=None)
		meaning_ja = correction(meaning_ja)
		can.drawString(25, count_row*height_layer_size + height_layer_size/7.012,"- "+meaning_ja)
		can.setFont('times-new-roman', 12, leading=None)
		can.drawString(25+len(meaning_ja)*5, count_row*height_layer_size + height_layer_size/7.012,meaning_vi)
	if exception5 != "_" :
		can.setFillColor(red)
		meaning_ja = ja(exception5)
		meaning_vi = vi(exception5,len(meaning_ja),len(exception5))
		can.setFont('simsun', 11, leading=None)
		meaning_ja = exception_correction(meaning_ja)
		can.drawString(323, count_row*height_layer_size + height_layer_size/13.5,"* "+meaning_ja)
		can.setFont('times-new-roman', 10, leading=None)
		can.drawString(323+len(meaning_ja)*5, count_row*height_layer_size + height_layer_size/13.5,meaning_vi)
		can.setFillColor(black)

def ja(value):
	meaning_len = len(value)
	japanese = ""
	for i in range (meaning_len):
		char1 = value[i]
		if char1 != "/" :
			japanese += char1
		else:
			break
	japanese_len = len(japanese)
	ja_result=""
	for j in range (japanese_len):
		char2 = japanese[j]
		if char2 == ",":
			ja_result += "/"
		else :
			ja_result += char2
			
	return ja_result
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
		pass
	for i in range(3):
		file_name = img + extension[i-1]
		if file_name in data_images:
			return path_image + file_name
def correction(string):
	if len(string) <= 10:
		return  string + "   "
	elif len(string) <= 20:
		return string + "  "
	elif len(string) <= 30:
		return string + " "
	else:
		return string
def exception_correction(string):
	if len(string) <= 10:
		return  string + " "
	else:
		return string	
module(data_file)
