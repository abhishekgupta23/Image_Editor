import streamlit as st
from PIL import Image, ImageFilter,ImageFont,ImageDraw
import base64
import pandas as pd
st.title('IMAGE EDITOR')
def image():
    a=st.file_uploader('upload images')
    return a
def crop_image():
    b=image()
    if b:
        img=Image.open(b)
        x1=st.slider('x1',0,img.width)
        y1=st.slider('y1',0,img.height)
        x2=st.slider('x2',img.width,0)
        y2=st.slider('y2',img.height,0)
        final=img.crop((x1,y1,x2,y2))
        st.title("FINAL IMAGE")
        st.image(final)
        btn=st.button("Done")
        if btn:
            final.save('final image.png','PNG')
def show():
    b=image()
    if b:
        st.image(b)
        img=Image.open(b)
        c=img.format
        st.write("Format of uploaded image is :-")
        st.write(c)
        a=img.size
        st.write("size of uploaded image is :-")
        st.write(a)
        d=img.mode
        st.write("Mode of uploaded image is :-")
        st.write(d)
def resize():
    b=image()
    if b:
        img=Image.open(b)
        x1=int(st.text_input("length",10))
        y1=int(st.text_input('breath',10))
        final=img.resize((x1,y1))
        st.title("FINAL IMAGE")
        st.image(final)
        btn=st.button("Done")
        if btn:
            final.save('final image.png','PNG')
def filt_():
    f=image()
    if f:
        img=Image.open(f)
        x=st.text_input("enter the the value")
        st.write("CONTOUR()")
        st.write("EDGE_ENHANCE()")
        st.write("EMBOSS()")
        st.write("Split RGB Colors")
        if x=='CONTOUR()':
            final=img.filter(ImageFilter.CONTOUR())
        elif x=='EDGE_ENHANCE()':
            final=img.filter(ImageFilter.EDGE_ENHANCE())
        elif x=='EMBOSS()':
            final=img.filter(ImageFilter.EMBOSS())
        else:
            final=img
        st.title("FINAL IMAGE")
        st.image(final)
        btn=st.button("Done")
        if btn:
            final.save('final image.png','PNG')
def addfont():
    b=image()
    if b:
        img=Image.open(b)
        x=st.text_input("enter the the value")
        f=st.slider('Font Size',0,100)
        x1=st.slider('Height',0,img.width)
        y1=st.slider('Width',0,img.height)
        font=ImageFont.truetype('RobotoMono-VariableFont_wght.ttf',f)
        writer=ImageDraw.Draw(img)
        writer.text((x1,y1),x,font=font,fill=(225,0,0))
        final=img
        st.title("FINAL IMAGE")
        st.image(final)
        btn=st.button("Done")
        if btn:
            final.save('final image.png','PNG')
def conv_():
    b=image()
    if b:
        img=Image.open(b)
        x1=st.text_input("enter the the value","")
        st.write("please input python function above that support convert")
        final=img.convert((x1))
        st.title("FINAL IMAGE")
        st.image(final)
        btn=st.button("Done")
        if btn:
            final.save('final image.png','PNG')
def rotat():
    b=image()
    if b:
        img=Image.open(b)
        x1=int(st.text_input("degree",0))
        final=img.rotate((x1))
        st.title("FINAL IMAGE")
        st.image(final)
        btn=st.button("Done")
        if btn:
            final.save('final image.png','PNG')
def mask():
    st.title("COMING SOON")
def flip():
    b=image()
    if b:
        img=Image.open(b)
        x=st.text_input("degree","")
        st.write("values you can enter :-")
        st.write("FLIP_LEFT_RIGHT")
        st.write("FLIP_TOP_BOTTOM")
        if x=='FLIP_LEFT_RIGHT':
            final=img.transpose(Image.FLIP_LEFT_RIGHT)
        elif x=='FLIP_TOP_BOTTOM':
            final=img.transpose(Image.FLIP_TOP_BOTTOM)
        else:
            final=img
        st.title("FINAL IMAGE")
        st.image(final)
        def get_table_download_link(df):
            """Generates a link allowing the data in a given panda dataframe to be downloaded
            in:  dataframe
            out: href string
            """
            csv = df.to_png(index=False)
            b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
            href = f'<a href="data:file/png;base64,{b64}" download = "Crypto Data.png">Download png file</a>'
            return href
        btn=st.button("Done")
        if btn:
            st.markdown(get_table_download_link(final),unsafe_allow_html=True)
def main():
    selected_box = st.sidebar.selectbox(
        'Choose one of the following',
        ('crop image','show image details','resize','rotate image','convert image','add mask','flip the image','filter image','add font on image')
        )
    if selected_box == 'crop image':
        crop_image() 
    if selected_box == 'show image details':
        show()
    if selected_box == 'resize':
        resize()
    if selected_box == 'rotate image':
        rotat()
    if selected_box == 'convert image':
        conv_()
    if selected_box == 'add mask':
        mask()
    if selected_box == 'flip the image':
        flip()
    if selected_box == 'filter image':
        filt_()
    if selected_box == 'add font on image':
        addfont()


main()
