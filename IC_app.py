import streamlit as st
import pandas as pd
import numpy as np
from datasets import load_dataset
dataset = load_dataset("laion/laion2B-multi")

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
# squad_dataset = load_dataset("squad")
  elif BoxOptions=="view rdm item"
  return 1
  elif BoxOptions=="redirect"
  "Ready to roll": ![alt](www.google.de)
    else 
    return 0
    
