import streamlit as st
import pandas as pd
import numpy as np
import time
import altair as alt

from urllib.error import URLError

from code.shared_functions import skip_echo

def display():
    c1, c2 = st.columns([9,1])
    c1.title("Ejemplo - gráfico en altair")
    show_code = c2.checkbox("Código")

    
