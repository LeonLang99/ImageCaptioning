
import streamlit as st
import pandas as pd
import numpy as np
#from datasets import load_dataset
#dataset = load_dataset("//huggingface.co/datasets/laion/laion2B-multi")

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


#copied text from https://app.gitbook.com/o/-MIdja2NhrQfKSnOsaVz/s/rdKhridiL1e82zkcHWLY/data-sets/laion-dataset#example-download
import urllib3
import pandas as pd
from PIL import Image
import io
import json


routes = {}
df = pd.read_csv('index_file.csv')


# iterate over the rows and download the images
for index, row in df.iterrows():
    # get the image from the url
    http = urllib3.PoolManager()
    r = http.request('GET', row['url'])
    img_data = r.data
    
    # save data to image file and row['TEXT'] to json file
    filename = "filename"
    image = Image.open(io.BytesIO(img_data))
    image.save(filename + '.png')
    text = row['TEXT']
    
    # save to routes for later use
    routes[filename] = text

json.dump(routes, open("routes.json", "w"))
