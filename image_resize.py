import streamlit as st
from PIL import Image, ImageFilter,ImageFont,ImageDraw
import base64
from streamlit import color_picker
from io import BytesIO
def app():
    
    st.markdown(
        """
        <style>
        .reportview-container {
            background: url("https://images.unsplash.com/photo-1558244402-286dd748c593?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=675&q=80")no-repeat center fixed;
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.title('IMAGE EDITOR')
    a=st.file_uploader('upload images')
    selected_box = st.sidebar.selectbox(
            'Choose one of the following',
            ('Select Option from dropdown','show image details','crop image','resize','rotate image','convert image','flip the image','filter image','add font on image','Add Image Over Image')
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
                buffered = BytesIO()
                final.save(buffered, format="JPEG")
                img_str = base64.b64encode(buffered.getvalue()).decode()
                href = f'<a href="data:file/jpg;base64,{img_str}" download="final image.jpg"><h1>Download final image</h1></a>'
                st.markdown(href, unsafe_allow_html=True)
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
                buffered = BytesIO()
                final.save(buffered, format="JPEG")
                img_str = base64.b64encode(buffered.getvalue()).decode()
                href = f'<a href="data:file/jpg;base64,{img_str}" download="final image.jpg"><h1>Download final image</h1></a>'
                st.markdown(href, unsafe_allow_html=True)

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
                buffered = BytesIO()
                final.save(buffered, format="JPEG")
                img_str = base64.b64encode(buffered.getvalue()).decode()
                href = f'<a href="data:file/jpg;base64,{img_str}" download="final image.jpg"><h1>Download final image</h1></a>'
                st.markdown(href, unsafe_allow_html=True)
    if selected_box == 'convert image':
        if a:
            img=Image.open(a)
            option2=st.selectbox("",('Select option from dropdown','Black and white with blur','Black and white'))
            if option2=='Select option from dropdown':
                    final=img
            if option2 == 'Black and white with blur':
                    final=img.convert(('1'))
            elif option2=='Black and white':
                    final=img.convert(('L'))
            st.title("FINAL IMAGE")
            st.image(final)
            btn=st.button("Done")
            if btn:
                a=final
                buffered = BytesIO()
                final.save(buffered, format="JPEG")
                img_str = base64.b64encode(buffered.getvalue()).decode()
                href = f'<a href="data:file/jpg;base64,{img_str}" download="final image.jpg"><h1>Download final image</h1></a>'
                st.markdown(href, unsafe_allow_html=True)
    if selected_box == 'flip the image':
        if a:
            img=Image.open(a)
            option2=st.selectbox("",('Select option from dropdown','FLIP_LEFT_RIGHT','FLIP_TOP_BOTTOM','ROTATE_90'))
            if option2=='Select option from dropdown':
                    final=img
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
                buffered = BytesIO()
                final.save(buffered, format="JPEG")
                img_str = base64.b64encode(buffered.getvalue()).decode()
                href = f'<a href="data:file/jpg;base64,{img_str}" download="final image.jpg"><h1>Download final image</h1></a>'
                st.markdown(href, unsafe_allow_html=True)

    if selected_box == 'filter image':
         if a:
            img=Image.open(a)
            option=st.selectbox("...",('Select option from dropdown','SHARPEN','SMOOTH','EMBOSS','CONTOUR','BLUR','BOX BLUR','EDGE ENHANCE'))
            if option==' ':
                    final=img
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
                buffered = BytesIO()
                final.save(buffered, format="JPEG")
                img_str = base64.b64encode(buffered.getvalue()).decode()
                href = f'<a href="data:file/jpg;base64,{img_str}" download="final image.jpg"><h1>Download final image</h1></a>'
                st.markdown(href, unsafe_allow_html=True)
    if selected_box == 'add font on image':
        if a:
            img=Image.open(a)
            x=st.text_input("enter the the value")
            choice=st.selectbox("choose font",("OdibeeSans-Regular","RobotoMono-VariableFont_wght","ZCOOLKuaiLe-Regular","IndieFlower-Regular","ShadowsIntoLight-Regular","Pacifico-Regular"))
            f=st.number_input("enter font size")
            if choice=="RobotoMono-VariableFont_wght":
                font=ImageFont.truetype('RobotoMono-VariableFont_wght.ttf',int(f))
            elif choice=="OdibeeSans-Regular":
                font=ImageFont.truetype('OdibeeSans-Regular.ttf',int(f))
            elif choice=="ZCOOLKuaiLe-Regular":
                font=ImageFont.truetype('ZCOOLKuaiLe-Regular.ttf',int(f))
            elif choice=="IndieFlower-Regular":
                font=ImageFont.truetype('IndieFlower-Regular.ttf',int(f))
            elif choice=="ShadowsIntoLight-Regular":
                font=ImageFont.truetype('ShadowsIntoLight-Regular.ttf',int(f))
            elif choice=="Pacifico-Regular":
                font=ImageFont.truetype('Pacifico-Regular.ttf',int(f))
            writer=ImageDraw.Draw(img)
            x1=st.slider('x1',0,img.width)
            y1=st.slider('y1',0,img.height)
            writer.text((x1,y1),x,font=font,fill=(255,0,255))
            st.title("FINAL IMAGE")
            st.image(img)
            btn=st.button("Done")
            if btn:
                buffered = BytesIO()
                img.save(buffered, format="JPEG")
                img_str = base64.b64encode(buffered.getvalue()).decode()
                href = f'<a href="data:file/jpg;base64,{img_str}" download="final image.jpg"><h1>Download final image</h1></a>'
                st.markdown(href, unsafe_allow_html=True)
    if selected_box == 'Add Image Over Image':
        if a:
            img=Image.open(a)
            p=st.file_uploader("")
            if p:
                width=st.slider("enter x1",0,img.width)
                height=st.slider("enter x2",0,img.height)
                p=Image.open(p)
                st.write("to change the size of pasted image")
                x1=st.slider('enter width',10,p.width)
                y1=st.slider('enter height',10,p.height)
                final=p.resize((x1,y1))
                img.paste(final,(int(width),int(height)))
                st.image(img)
                btn=st.button("Done")
                if btn:
                    buffered = BytesIO()
                    img.save(buffered, format="JPEG")
                    img_str = base64.b64encode(buffered.getvalue()).decode()
                    href = f'<a href="data:file/jpg;base64,{img_str}" download="final image.jpg"><h1>Download final image</h1></a>'
                    st.markdown(href, unsafe_allow_html=True)
