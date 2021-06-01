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
        x1=st.number_input("degree",0)
        final=img.rotate(int(x1))
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
        option2=st.selectbox("",('FLIP_LEFT_RIGHT','FLIP_TOP_BOTTOM','ROTATE_90'))
    if option2 == 'FLIP_LEFT_RIGHT':
        final=img.transpose(Image.FLIP_LEFT_RIGHT)
    elif option2=='FLIP_TOP_BOTTOM':
        final=img.transpose(Image.FLIP_TOP_BOTTOM)
    elif option2=='ROTATE_90':
        final=img.transpose(Image.ROTATE_90)
        st.title("FINAL IMAGE")
        st.image(final)
        btn=st.button("Done")
        if btn:
            a = final
            final.save('final image.png','PNG')
        
if selected_box == 'filter image':
     if a:
        img=Image.open(a)
        option=st.selectbox("...",('SHARPEN','SMOOTH','EMBOSS','CONTOUR','BLUR','BOX BLUR','EDGE ENHANCE'))
    if option=='SHARPEN':
        final=img.filter(ImageFilter.SHARPEN())
    elif option=='SMOOTH':
        final=img.filter(ImageFilter.SMOOTH())
    elif option=='EMBOSS':
        final=img.filter(ImageFilter.EMBOSS())
    elif option=='CONTOUR':
        final=img.filter(ImageFilter.CONTOUR())
    elif option=='BLUR':
        final=img.filter(ImageFilter.BLUR())
    elif option=="BOX BLUR":
        final=img.filter(ImageFilter.BoxBlur(),radius=1)
    elif option=="EDGE ENHANCE":
        final=img.filter(ImageFilter.EDGE_ENHANCE())
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
        c=st.color_picker(label="choose color of text")
        f=st.slider('Font Size',0,100)
        x1=st.slider('Height',0,img.width)
        y1=st.slider('Width',0,img.height)
        font=ImageFont.truetype('RobotoMono-VariableFont_wght.ttf',f)
        writer=ImageDraw.Draw(img)
        writer.text((x1,y1),x,font=font,fill=c)
        final=img
        st.title("FINAL IMAGE")
        st.image(final)
        btn=st.button("Done")
        if btn:
            a=final
            final.save('final image.png','PNG')
def mask():
    st.title("COMING SOON")
