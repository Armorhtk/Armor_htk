#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   home.py
@Contact :   htkstudy@163.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/5/16 12:29   Armor(htk)     1.0         None
'''
import streamlit as st
import requests
import os
import pandas as pd
from streamlit_lottie import st_lottie
from PIL import Image

def load_lottic(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def load_css(css_file):
    css_file = os.path.join(os.getcwd(),css_file)
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

def load_img(img_file):
    img_file = os.path.join(os.getcwd(), img_file)
    return Image.open(img_file)


def app():
    load_css('style/style.css')
    lottie_coding = load_lottic('https://assets2.lottiefiles.com/packages/lf20_rtsrhxhg.json')
    img_any = load_img('images/imgany.jpg')

    st.header("Home Page")

    # ---- HEADER SECTION ----
    with st.container():
        left_column, right_column = st.columns(2)
        with right_column:
            st_lottie(lottie_coding, height=256, key="coding")
        with left_column:
            st.title("Welcome to my home page :sparkles:")
            st.subheader("About Me")
            st.write("\n\n")
            st.write(
                """
                
                ● :wave: Hi, I am Tingkai Hu , A Postgraduate student from CQUST
                
                ● 👨‍💻 I'm passionate on Natural Language Processing and Data Mining....
                
                ● 📊 I’m currently learning Data Mining in the emergency events and Fine-grained text classification.
                
                ● 📊 My research mainly focuses on text classification, such as Fine-grained text classification, Weakly supervised text classification and so on.
                
                ● 📧 How to reach me: htkstudy@163.com / [Github](https://github.com/Armorhtk)
                
                ● ✨ 成人不自在，自在不成人
                """
            )
        # st.audio("audio/靠近-咻咻满.mp3")

    # ---- WHAT I DO ----
    with st.container():
        st.write("---")
        left_column, right_column = st.columns([2,4])
        with right_column:
            st.subheader("What I do")
            st.write("##")
            st.write(
                """
                Follow my channel O(∩_∩)O.
                \n
                """
            )
            st.write("[Yuque Channel >](https://www.yuque.com/armor-novr7)")
        with left_column:
            st.image(img_any,width=300)

    # ---- CONTACT ----
    with st.container():
        st.write("---")
        st.subheader("Get In Touch With Me!")
        st.write("##")

        # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
        contact_form = """
        <form action="https://formsubmit.co/htkstudy@163.COM" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        left_column, right_column = st.columns([3,1])
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
        	st.empty()
