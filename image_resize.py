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
def format_():
    b=image()
    img=Image.open(b)
    c=img.format
    st.write("Format of uploaded image is :-")
    st.write(c)
def mode_():
    b=image()
    if b:
        img=Image.open(b)
        c=img.mode
        st.write("Mode of uploaded image is :-")
        st.write(c)
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
def size_():
    b=image()
    if b:
        img=Image.open(b)
        a=img.size
        st.write("size of uploaded image is :-")
        st.write(a)
def filt_():
    f=image()
    if f:
        img=Image.open(f)
        x=st.text_input("enter the the value")
        st.write("CONTOUR()")
        st.write("EDGE_ENHANCE()")
        st.write("EMBOSS()")
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
        btn=st.button("Done")
        if btn:
            final.save('final image.png','PNG')
def main():
    selected_box = st.sidebar.selectbox(
        'Choose one of the following',
        ('crop image','show', 'format', 'mode','resize','size','rotate image','convert image','add mask','flip the image','filter image','add font on image')
        )
    if selected_box == 'crop image':
        crop_image() 
    if selected_box == 'show':
        show()
    if selected_box == 'format':
        format_()
    if selected_box == 'mode':
        mode_()
    if selected_box == 'resize':
        resize()
    if selected_box == 'size':
        size_()
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
