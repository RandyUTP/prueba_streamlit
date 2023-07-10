import streamlit as st
import pandas as pd
import numpy as np

from code.shared_functions import skip_echo

def display():
    c1, c2 = st.columns([9,1])
    c1.title("¿Cómo y dónde aprender?")
    show_code = c2.checkbox("Código")
    with st.echo("above") if show_code else skip_echo():
        c1, c2 = st.columns([2,3])
        c1.image("images/link.png")
        c2.markdown("##### Enlaces:")
        c2.markdown("* https://streamlit.io/\n* https://docs.streamlit.io/")
        c2.markdown("##### Comunidades:")
        c2.markdown("* Foro Oficial: https://discuss.streamlit.io/\n* Discord: https://discord.com/invite/bTz5EDYh9Z")
        c2.markdown("##### Material:")
        c2.markdown("* :book: [Getting Started with Streamlit for Data Science](https://www.amazon.com/Getting-Started-Streamlit-Data-Science/dp/180056550X), de Tyler Richards")
        c2.markdown("##### Twitter:")
        c2.markdown("* Streamlit: @streamlit\n* Fanilo Andrianasolo\n@andfanilo\n* Charlie Wargnier: @DataChaz\n* JM Napoles: @napoles3D")