import masking
import image_resize
import border
import streamlit as st
PAGES = {
    "Editing": image_resize,
    "Masking": masking,
    "Add boder to image": border
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
