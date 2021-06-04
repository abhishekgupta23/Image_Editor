import streamlit as st
from PIL import Image, ImageOps
import base64 
from io import BytesIO
def app():
    st.markdown(
        """
        <style>
        .reportview-container {
            background: url("https://images.unsplash.com/photo-1558244402-286dd748c593?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=675&q=80") no-repeat center fixed;
            background-size: cover;
        }
    .sidebar .sidebar-content {
            background: url("url_goes_here")
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.title("Add Border To Image")
    im1=st.file_uploader(label="UPLOAD IMAGE")
    if im1:
        # open the image
        img = Image.open(im1)
        a=st.slider("border width",1,100)
        # add border to the image
        img2 = ImageOps.expand(img, border=int(a), fill='blue')
        # display image
        st.image(img2)
        btn = st.button("Save")
        if btn:
            buffered = BytesIO()
            img2.save(buffered, format="JPEG")
            img_str = base64.b64encode(buffered.getvalue()).decode()
            href = f'<a href="data:file/jpg;base64,{img_str}" download="final image.jpg"><h1>Download final image</h1></a>'
            st.markdown(href, unsafe_allow_html=True)
