import streamlit as st
import numpy as np
import cv2
import time
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import load_model
from streamlit_drawable_canvas import st_canvas

from code.shared_functions import skip_echo
from matplotlib import pyplot as plt

#from tensorflow.keras.utils import object_identity

#@st.cache(hash_funcs={object_identity.ObjectIdentityDictionarys: lambda _: None})¡
@st.cache(allow_output_mutation=True)
def load_digits_model():
    model = load_model('model.h5')
    return model

def display():
    predicted_value = 0
    c1, c2 = st.columns([9,1])
    c1.title("Ejemplo usando componentes y Machine Learning")
    show_code = c2.checkbox("Código")
    predict = c2.button("Predecir")

    st.caption("Reconocimiento dígitos - basado en https://github.com/rahulsrma26/streamlit-mnist-drawable")

    with st.echo("above") if show_code else skip_echo():
        # Cargar el modelo
        model = load_digits_model()
        # Streamlit, dame 2 columnas en relacion 1:2
        c1, c2 = st.columns([1,2])
        # En la primera columna, pone un canvas
        with c1:
            st.markdown("Dibuja un dígito")
            SIZE = 28*10
            canvas_result = st_canvas(
                fill_color='#000000',
                stroke_width=20,
                stroke_color='#FFFFFF',
                background_color='#000000',
                width=SIZE,
                height=SIZE,
                drawing_mode="freedraw", #if mode else "transform",
                display_toolbar=True,
                key='canvas')
        if predict:
            # Pequeño delay para inicialización del canvas
            time.sleep(0.5)
            # En la segunda columna, cuando se tenga un dibujo, ejecuta codigo
            if canvas_result is not None and canvas_result.image_data.sum().sum() != 255*SIZE*SIZE :     
                img = cv2.resize(canvas_result.image_data.astype('uint8'), (28, 28))
                x = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY).reshape(1, 28, 28)
                val = model.predict(x) # shape (1,10)
                predicted_value = np.argmax(val[0])
                c2.write(f'Predicción: **{predicted_value}**')
                c2.bar_chart(val[0])
        # Mostrar algunos de los dígitos
        with st.expander("¿Qué es esto?"):
            st.write("Se proporciona un canvas para dibujar y (tratar de) reconocer el dígito.")
            st.write("La imagen dibujada por el usuario se escala para tener 28x28 pixeles.")
            st.write("La imagen escalada se pasa a una red neural entrenada en ejemplos del MNIST dataset.")
            st.write("La red neuronal posee 3 capas con 300, 50 y 10 neuronas.")
            st.write("El MNIST dataset contiene 70,000 imágenes de 28x28 pixeles con dígitos.")
        # Mostrar algunos de los dígitos
        with st.expander("¿Cómo son los ejemplos del Datast MNIST?"):
            (x_train, y_train), (x_test, y_test) = mnist.load_data()
            c1, c2 = st.columns([3,9])
            digit = c1.number_input("Selecciona un dígito:", min_value=0, max_value=9, step=1, value=predicted_value)
            x_examples = x_train[y_train==digit,:,:]
            N = 20
            c = st.columns(N)
            for i in range(N):
                fig, ax = plt.subplots()
                plt.imshow(x_examples[i])
                c[i].pyplot(fig)

if __name__=="__main__":
    display()                