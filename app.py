#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   app.py    
@Contact :   htkstudy@163.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/5/16 11:21   Armor(htk)     1.0         None
'''
import streamlit as st
from multipage import MultiPage
from pages import home

st.set_page_config(page_icon=":ghost:",page_title="Home Page",layout="wide")

app = MultiPage()

# add application
app.add_page("Home", home.app)

if __name__=="__main__":
    app.run()

