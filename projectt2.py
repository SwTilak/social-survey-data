import pandas as pd
import streamlit as st
import PIL as Image
import plotly.express as px
import csv 
import plotly.graph_objects as go
st.title("Genral Social Survey data analytics web app")
gss_data=pd.read_csv("C:\\Users\\swati\\Downloads\\gss2016.csv")
gss_data_filtered=gss_data[['race','sex','age','degree','wrkstat','income','happy']]
gss_data_filtered.head()
st.write("")
st.write("")
st.write("")
st.write("")

st.header("GSS 2016 datset filtered on sex,Race,Age,Degree,Wrkstat,Income and Happiness")
st.dataframe(gss_data_filtered)

columns={'race','sex','age','degree','wrkstat','income','happy'}
st.write("")
st.write("")
st.write("")
st.write("")
st.header("dataset aggregated by count")
pick_columns=st.selectbox("Count by column:" , list(columns))
gss_data_filtered["Count"]=0
gss_data_filtered_count=gss_data_filtered.groupby(pick_columns).count()
gss_data_filtered_count=gss_data_filtered_count[["Count"]]
gss_data_filtered_count["percentage"]=(gss_data_filtered_count.Count/gss_data_filtered_count.Count.sum())*100
st.dataframe(gss_data_filtered_count)

st.write("")
st.write("")
st.write("")
st.write("")
st.header("dataset correlation between columns")

multi_select_column=st.multiselect("columns for correlation:",list(columns),default=["sex"])

multi_select_filtered=gss_data_filtered[multi_select_column]
st.dataframe(multi_select_filtered)

st.write("")
st.write("")
st.write("")
st.header("dataset correlation between columns multi select")


multiselectcolumn2=st.multiselect("multi select column group by:",list(columns),default=["sex"])
multiselectgroupby=gss_data_filtered[multiselectcolumn2].groupby(multiselectcolumn2).size().reset_index(name="Count")

multiselectgroupby["percentage"]=(multiselectgroupby.Count/multiselectgroupby.Count.sum())*100
st.dataframe(multiselectgroupby)

st.write("")
st.write("")
st.write("")
st.write("")
st.header("dataset aggregated by count pie chart")
pickcolumnsvisualized=st.selectbox("Visualize by column:",list(columns))
visual=gss_data_filtered.groupby(pickcolumnsvisualized).count()

visual["x-axis"]=visual.index
fig=go.Figure(data=[go.Pie(labels=visual["x-axis"],values=visual["Count"])])
st.plotly_chart(fig)
