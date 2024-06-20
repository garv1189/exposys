import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import altair as alt
from sklearn.linear_model import LinearRegression


df=pd.read_csv("50_Startups.csv")

x = np.array(df['R&D Spend']).reshape(-1,1)
lr = LinearRegression()
lr.fit(x,np.array(df['Profit']))

st.title("Profit Prediction for StartUps")
nav=st.sidebar.radio("Navigation",["Home","Prediction","Contribute"])

if nav=="Home":
    st.image("image.jpg",width=600)
    if st.checkbox("Show Table"):
        st.table(df)
    
    graph=st.selectbox("Which Graph",["Non Interactive","None"])

    if graph=="Non Interactive":
        st.altair_chart(df,use_container_width =True)
        plot = sns.pairplot(df)
        st.pyplot(plot.figure)

        st.line_chart(df)
        st.area_chart(df)
        st.bar_chart(df)
    if graph=="None":
        st.write("Select Non Interactive to view graph")
    

if nav=="Prediction":
    st.write("Prediction")
    st.image("image.jpg",width=600)
    st.header("Know the Profit")

    val = st.number_input("Enter your R&D Spend",0,200000,step = 100)
    val = np.array(val).reshape(1,-1)
    pred =lr.predict(val)[0]

    if st.button("Predict"):
        st.success(f"Your Profit is {round(pred)}")


if nav=="Contribute":
    st.write("Contribute")
    st.image("image.jpg",width=600)
    st.header("Contribute to our dataset")

    rd = st.number_input("Enter your R&D Spend",0,200000)
    sal = st.number_input("Enter your Profit",0,250000,step = 1000)
    adm = st.number_input("Enter your Administration",0,250000,step = 1000)
    mkt = st.number_input("Enter your Marketing",0,250000,step = 1000)
    if st.button("submit"):
        to_add = {"R&D Spend":[rd],"Marketing Spend":[mkt],"Administration":[adm],"Profit":[sal]}
        to_add = pd.DataFrame(to_add)
        to_add.to_csv("50_Startups.csv",mode='a',header = False,index= False)
        st.success("Submitted")