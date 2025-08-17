#!/usr/bin/env python
# coding: utf-8

# In[7]:


get_ipython().system('pip install gradio')

from fastai.vision.all import *
import gradio as gr


# In[33]:


def is_healthy(x): return x[0].isupper()


# In[34]:


im = PILImage.create('rotten.jpeg')
im.thumbnail((192, 192))
im


# In[35]:


learn = load_learner('export.pkl')


# In[36]:


learn.predict(im)


# In[37]:


categories = ('Rotten', 'Healthy')

def classify_images(img):
    # load your model
    learn = load_learner("export.pkl")
    
    # make prediction
    pred, _, probs = learn.predict(img)
    
    return {pred: float(max(probs))}


# In[38]:


image = gr.Image()
label = gr.Label()
example = ["rotten.jpeg"]


# In[39]:


intf = gr.Interface(
    fn=classify_images,          # your prediction function
    inputs=image,
    outputs=label,
    examples=example
)

intf.launch()


# In[ ]:





# In[ ]:





# In[ ]:




