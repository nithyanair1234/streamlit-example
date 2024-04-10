import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# YumSum!!!



In the meantime, below is an example of what you can do with just a few lines of code:
"""

cuisine = st.text_input('Cuisine')
location = st.text_input('Location')
numberOfResults = st.number_input('Results', min_value = 1, max_value = 5, value = 1)

done = st.button("Done", use_container_width= True)
reset = st.button("Reset", use_container_width=True) 

if(done):
    st.write("You want ", numberOfResults)
    st.write(location)
    st.write(cuisine)



