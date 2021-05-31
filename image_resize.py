import streamlit as st
from PIL import Image, ImageFilter,ImageFont,ImageDraw
import base64
import pandas as pd
st.title('IMAGE EDITOR')
a=st.file_uploader('upload images')
selected_box = st.sidebar.selectbox(
        'Choose one of the following',
        ('show image details','crop image','resize','rotate image','convert image','add mask','flip the image','filter image','add font on image')
        )
if selected_box == 'show image details':
    if a:
        st.image(a)
        img=Image.open(a)
        c=img.format
        st.write("Format of uploaded image is :-")
        st.write(c)
        b=img.size
        st.write("size of uploaded image is :-")
        st.write(b)
        d=img.mode
        st.write("Mode of uploaded image is :-")
        st.write(d) 
if selected_box == 'crop image' :
    if a:
        img=Image.open(a)
        x1=st.slider('x1',0,img.width)
        y1=st.slider('y1',0,img.height)
        x2=st.slider('x2',img.width,0)
        y2=st.slider('y2',img.height,0)
        final=img.crop((x1,y1,x2,y2))
        st.title("FINAL IMAGE")
        st.image(final)
        btn=st.button("Done")
        if btn:
            a = final
            final.save('final image.png','PNG')
if selected_box == 'resize':
    if a:
        img=Image.open(a)
        x1=int(st.text_input("length",10))
        y1=int(st.text_input('breath',10))
        final=img.resize((x1,y1))
        st.title("FINAL IMAGE")
        st.image(final)
        btn=st.button("Done")
        if btn:
            a = final
            final.save('final image.png','PNG')
            
if selected_box == 'rotate image':
    if a:
        img=Image.open(a)
        x1=int(st.text_input("degree",0))
        final=img.rotate((x1))
        st.title("FINAL IMAGE")
        st.image(final)
        btn=st.button("Done")
        if btn:
            a=final
            final.save('final image.png','PNG')
if selected_box == 'convert image':
    if a:
        img=Image.open(a)
        x1=st.text_input("enter the the value","")
        st.write("please input python function above that support convert")
        final=img.convert((x1))
        st.title("FINAL IMAGE")
        st.image(final)
        btn=st.button("Done")
        if btn:
            a=final
            final.save('final image.png','PNG')
if selected_box == 'add mask':
    mask()
if selected_box == 'flip the image':
    if a:
        img=Image.open(a)
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
            a = final
            final.save('final image.png','PNG')
        
if selected_box == 'filter image':
     if a:
        img=Image.open(a)
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
            a = final
            final.save('final image.png','PNG')
if selected_box == 'add font on image':
    if a:
        img=Image.open(a)
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
            a=final
            final.save('final image.png','PNG')
def mask():
    st.title("COMING SOON")
