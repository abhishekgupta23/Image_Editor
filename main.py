import masking
import image_resize
import streamlit as st
PAGES = {
    "editing": image_resize,
    "masking": masking
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
