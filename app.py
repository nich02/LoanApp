import streamlit as st

#file processing packages
from PIL import Image
import pandas as pd
import docx2txt
#from PyPDF2 import PdfFileReader
import pdfplumber
#import textract

import os
import base64
#loading images
@st.cache #making image load faster
def load_image(image_file):
	img=Image.open(image_file)
	return img

#def read_pdf(file):
	#pdfReader=PdfFileReader(file)
	#count=pdfReader.numPages
	#all_page_text=""
	#for i in range(count):
		#page=pdfReader.getPage(i)
		#all_page_text +=page.extractText()
	#return all_page_text
#DOWNOAD FUNCTION
def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
    return href


def main():
	st.title("File Upload Tutorial")

	menu=["Home","Dataset","DocumentFiles","About"]
	choice=st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("Home")
		image_file=st.file_uploader("Upload Images",
			type=["png","jpg","jpeg"])
		if image_file is not None:


			#To see details
			   st.write(type(image_file))
			   #methods/attributes
			   #st.write(dir(image_file))
			   file_details={"filename":image_file.name,"filetype":image_file.type,"filesize":image_file.size}
			   st.write(file_details)

			   st.image(load_image(image_file),width=650,height=650)
	elif choice == "Dataset":
		st.subheader("Dataset")
		data_file=st.file_uploader("Upload CSV",type=["csv"])
		if data_file is not None:
			st.write(type(data_file))
			file_details={"filename":data_file.name,"filetype":data_file.type,"filesize":data_file.size}
			st.write(file_details)
			df=pd.read_csv(data_file)
			st.dataframe(df)
	elif choice == "DocumentFiles":
		st.subheader("DocumentFiles")
		docx_file=st.file_uploader("Upload Document",type=["pdf","docx","txt"])
		if st.button("Process"):
			if docx_file is not None:
				file_details={"filename":docx_file.name,"filetype":docx_file.type,"filesize":docx_file.size}
			st.write(file_details)
			if docx_file.type =="text/plain":
				#read as bytes
				#raw_text = docx_file.read()
				#st.write(raw_text)#works but in bytes

				#st.text(raw_text)#does work as expected

				#read as string (decode bytes to string)
				raw_text=str(docx_file.read(),"utf-8")
				#st.write(raw_text)#works
				st.text(raw_text)#works also
			elif docx_file=="application/pdf":
				try:
				   with pdfplumber.open(docx_file,'wb') as pdf:
				       pages=pdf.pages[0]
				       st.write(pages.extract_text())
				except:
				       st.write("None")
				#using PyPDF
				#raw_text=read_pdf(docx_file)
				#st.write(raw_text)
			else:   

				raw_text=docx2txt.process(docx_file)
				st.write(raw_text)
				#st.text(raw_text)
	else:
		st.subheader("About")
		st.markdown(get_binary_file_downloader_html('photo.jpg', 'Picture'), unsafe_allow_html=True)
st.markdown(get_binary_file_downloader_html('data.csv', 'My Data'), unsafe_allow_html=True)
st.markdown(get_binary_file_downloader_html('2g1c.mp4', 'Video'), unsafe_allow_html=True)

if __name__ == '__main__':
	main() 