import streamlit as st 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
import plotly.express as px 
from PIL import Image

def run():
    ## membuat judul
    st.title('EDA untuk Dataset FER2013')

    ## membuat sub header
    st.subheader('Objective : Membuat Model ANN untuk prediksi Emosi Wajah untuk mengetahui Ekpresi peserta kelas Hacktiv8 untuk meningkatkan efektifitas pembelajaran.')

    ## tambahkan gambar
    image =  Image.open('dataset-cover.png')
    st.image(image, caption='FER2013')

    ## menambahkan deskripsi
    

    st.subheader('Distribusi Data Train')
    st.write('Data distribution for train: ')
    image2 =  Image.open('train.png')
    st.image(image2, caption='Distribusi Data Train')
    st.write('fear: 4103, surprise: 3205, happy: 7164, angry: 3993, disgust: 436, neutral: 4982, sad: 4938')

    st.subheader('Distribusi Data Val')
    st.write('Data distribution for validation: ')
    image3 =  Image.open('val.png')
    st.image(image3, caption='Distribusi Data Val')
    st.write('fear: 1018, surprise: 797, happy: 1825, angry: 960, disgust: 111, neutral: 1216, sad: 1139')

    st.subheader('Distribusi Data Test')
    st.write('Data distribution for test: ')
    image4 =  Image.open('test.png')
    st.image(image4, caption='Distribusi Data Test')
    st.write('fear: 528, surprise: 626, happy: 879, angry: 491, disgust: 55, neutral: 594, sad: 416')


    st.markdown('---')

    st.write('Page ini dibuat oleh Raymond Samuel')






if __name__ == '__main__':
    run()