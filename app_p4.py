#Import the required Libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(layout="wide")


# Functions for each of the pages
def home(uploaded_file):
    if uploaded_file:
        st.header('Begin exploring the data using the menu on the left')
    else:
        st.header('To begin please upload a file')
        

def data_summary():
    st.header('Data Usage Summary')
    st.text('This data is from last 28 days of Copilot usage')
    st.write('Languages Used : Java')
  
    total = df['Lines_Accepted'].sum()
    st.write('Total Lines Accepted:', total)  

    st.write('Total Acceptance Percentage %:', total/df['Lines_Suggested'].sum() * 100)

    total = df['Lines_Suggested'].sum()
    st.write('Total Lines Suggested:', total)
    st.write('Average Lines Suggested:', df['Lines_Suggested'].mean())
    chart_data = df[['Lines_Accepted', 'Lines_Suggested',]]
    st.line_chart(chart_data)
 


def data_header():  
    st.header('Header of Dataframe')
    st.write(df.head())

def displayplot():
    st.header('Plot of Data')
    
    fig, ax = plt.subplots(1,1)
    ax.scatter(x=df['Lines_Suggested'], y=df['Lines_Accepted'])
    ax.set_xlabel('Lines)_Suggested')
    ax.set_ylabel('Lines_Accepted')
    
    st.pyplot(fig)



# Add a title and intro text
st.title('Copilot Data Usage Project')
st.text('This is an application to allow exploration of Copilot Data')


# Sidebar setup
st.sidebar.title('Sidebar')
upload_file = st.sidebar.file_uploader('Upload a file containing copilot usage data')
#Sidebar navigation
st.sidebar.title('Navigation')
options = st.sidebar.radio('Select what you want to display:', ['Home', 'Data Summary', 'Data Header', 'Scatter Plot'])


# Check if file has been uploaded
if upload_file is not None:
    df = pd.read_csv(upload_file)

# Navigation options
if options == 'Home':
    home(upload_file)
elif options == 'Data Summary':
    data_summary()
elif options == 'Data Header':
    data_header()
elif options == 'Scatter Plot':
    displayplot()

