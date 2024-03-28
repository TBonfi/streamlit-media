import streamlit as st
import pandas as pd
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin",
  database="protein_db"
)

query = "SELECT * FROM demo"
df = pd.read_sql(query, con=mydb)

from PIL import Image
from io import BytesIO

# Function to read image from binary data
def read_image(image_data):
    return Image.open(BytesIO(image_data))

# Apply the function to read images from the DataFrame
df['Image_demo'] = df['Image_demo'].apply(read_image)



# Título del app
st.title('Search and Display Images App')

# Buscador en la barra (en realidad es para tener un input con el cual filtrar)
search_term = st.sidebar.text_input("Search by Name", "")

# Ahora utilizamos la variable search_term para filtrar, es para una prueba de concepto
filtered_df = df[df['Name'].str.contains(search_term, case=False)]

# Display search results
if not filtered_df.empty:
    # selectbox es la "caja" de búsqueda que se puede desplegar, tendrá los resultados filtrados según la query anterior
    selected_item = st.selectbox('Select an item:', filtered_df['Name'])


    selected_row = filtered_df[filtered_df['Name'] == selected_item].iloc[0]

    st.write('**Name:**', selected_row['Name'])
    st.write('**Description:**', selected_row['Description'])
    st.image(selected_row['Image_demo'], caption='Selected Image', use_column_width=True)

else:
    st.warning('No results found.')


st.subheader('Entire DataFrame')
st.write(df)
