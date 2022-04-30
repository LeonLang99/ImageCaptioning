import streamlit as st
import pandas as pd
import numpy as np
from datasets import load_dataset
dataset = load_dataset("laion/laion2B-multi")

y=1


st.write("""
# Image Captioning Group 13

Hello, we are Leon Lang, Jean Luis Fichtner and Loredana Bratu and we are the creators 
of the app ,,Image captioning“. Our app’s aim is to automatically describe an image with 
one or more natural language sentences. To generate textual description of images we will 
be using Neural Network and Deep Learning Techniques.


""")

#Different function based on box

BoxOptions= st.selectbox("Choose", ("load sample table", "view rdm item", "redirect"))

def selectDataset(boxOptions):
  if BoxOptions=="load sample table":
    b=y*100
    return b
# squad_dataset = load_dataset("squad")
  elif BoxOptions=="view rdm item":
    a=y*5
  return a
#  elif BoxOptions=="redirect":
#  "Ready to roll": ![alt](www.google.de)
  else:
    y=y+1
    return y
    
