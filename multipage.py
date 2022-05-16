#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   multipage.py    
@Contact :   htkstudy@163.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/5/16 12:22   Armor(htk)     1.0         None
'''

import streamlit as st

class MultiPage:
    def __init__(self)->None:
        self.page = []

    def add_page(self,title,func):
        self.page.append(
            {
                "title":title,
                "function":func,
            }
        )

    def run(self):
        page = st.sidebar.selectbox(
            "App navigation",
            self.page,
            format_func=lambda  page: page["title"],

        )
        page["function"]()