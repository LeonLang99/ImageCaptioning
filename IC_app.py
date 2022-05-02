import streamlit as st
import random as rdm
import pandas as pd
import numpy as np




  
  
st.title('Image Captioning Group 13')

with st.expander("The Team"):
  st.write("Hello, we are Leon Lang, Jean Louis Fichtner and Loredana Bratu and we create this app as a part of our business informatics course ")
with st.expander("The Mission"):
  st.write("The purpose of our app is to automatically describe an image with one or more natural language sentences. To generate textual descriptions of images we will use Machine Learning and Deep Learning Techniques.")
with st.expander("The Dataset"):
  st.write("Here you can see some examples from our Dataset")
  col1, col2, col3 = st.columns(3)

with col1:
    st.header("Chrysler Logo")
    st.image("https://img1.d2cmedia.ca/cb5bf24a74832ba/1471/7214770/C/Chrysler-200-2016.jpg")

with col2:
    st.header("NIKE Shoe")
    st.image("https://img.alicdn.com/imgextra/i3/817462628/O1CN01eLHBGX1VHfUMBA1du_!!817462628.jpg")

with col3:
    st.header("Girl in a white dress")
    st.image("https://static2.yan.vn/YanNews/2167221/202004/co-luc-na-trat-duoc-khen-nuc-no-vi-qua-de-thuong-nho-tang-can-93c37ecb.jpeg")

with st.expander("Random Picture"):
  st.write("Please press the following Button to get a random picture from our dataset.")
  
  
  
  @st.cache
  def load_data_csv():
    data = pd.read_csv("https://github.com/LeonLang99/ImageCaptioning/blob/main/Mappe1.csv")
    return data
  
  data=load_data_csv()

  def get_rdm_image():
    row = rdm.randint(0,67)
    url = data.iloc[row]["URL"]
    st.image(url)
    st.write(data.iloc[row]["TEXT"])
  
  if st.button("Get Random Image"):
    get_rdm_image()
  

