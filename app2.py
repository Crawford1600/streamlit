import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

df=pd.read_csv("sample_pivot.csv")
st.set_page_config(layout="wide")
fh=df.drop(columns=["Region"]).columns
st.title("HIGH FASHION :green[Analysis]:👕👔🧥👟:")
st.markdown("This Analysis Dashboard that gives a Relationship Between Region And Other Various attributes used in production of Designer of **High Fashion**Wears,Based on Four Region Which Are(East,West,North,South")

st.sidebar.markdown("## The Piechart And Barchart: Ralationship Between Region And Sales.")
x_axis=st.sidebar.selectbox("X AXIS",fh)
y_axis=st.sidebar.selectbox("Y AXIS",fh)
color_encode=st.sidebar.checkbox(label="COLOR ENCODE BY Region")
container=st.container()
chart1,chart2=container.columns(2)

with chart1:
   if x_axis and y_axis: 
    fig=px.bar(df,x=x_axis,y=y_axis,color="Region" if color_encode else None,title="{} vs {} ".format(x_axis.upper(),y_axis.upper()))
    st.plotly_chart(fig,use_container_width=True)
with chart2:
   if x_axis and y_axis:
    st.markdown("SELECT X AXIS TO BE ONLY CATEGORY AND Y AXIS SHOULD BE NUMBER.") 
    fig2=px.pie(df,names=x_axis,values=y_axis,title="{} vs {}".format(x_axis.upper(),y_axis.upper()),template="seaborn",hole=0.5)
    pull_values=[0,0,0,0]
    fig2.update_traces(pull=pull_values,textposition="inside",textinfo="percent+label")
    st.plotly_chart(fig2,use_container_width=True)

show_df=st.checkbox("SHOW DATA FRAME")
if show_df:
  st.dataframe(df)

st.header("CHICKEN REPUBLIC🍟🍕🍖🥤🥗🍔🍗🥓")
st.markdown("This Analyzing the Relationship Between Customer And Other Attributes like(Total bill,Tips,Gender) with Each Day ")
df3=pd.read_csv("tips.csv")
fig6=px.sunburst(df3,path=["Day","Time","Sex","Smoker"],values="Total_bill")
st.plotly_chart(fig6,use_container_width=True)