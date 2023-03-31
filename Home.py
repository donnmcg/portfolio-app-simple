import streamlit as st
import pandas

st.set_page_config(layout="wide")  # set the layout to wide so that the "invisible container" takes up the screen width.

col1, col2 = st.columns(2)  # create two column object instances

with col1:  # add something to a column with "with"
    st.image("images/photo.png")

with col2:
    st.title("Donnacha McGrath")
    content = """
    Hi, I'm Donnacha! I am taking a course that teaching me to do different things with python.
    """
    st.info(content)  # write content to col2. could use st.write() too.

content2 = """
Below you can find some the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])  # create 3 cols. List details ratio. Empty is a spacer.

df = pandas.read_csv("data.csv", sep=";")  # import the data into a pandas data frame. Separator = ;

with col3:
    for index, row in df[0:10].iterrows():  # use pandas to put the first ten items in col 3
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():  # use pandas to put the items after the 10th row in col 4
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")