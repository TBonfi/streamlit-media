import streamlit as st
import pandas as pd

'''
Para ejecutar la aplicación-> abrir una CMD y ejecutar: streamlit run app.py
Para encontrar donde está el config.toml -> streamlit config show (E.G.: "C:\Users\bonfi\.streamlit\config.toml")
Para cortar la ejecución -> ctrl+c
'''

# datos sample
data = {
    'Name': ['patas', 'proteina', 'orejas'],
    'Image_Path': ['patas.jpg',
                   'protein.jpg',
                   'orejas.jpg'],
    'Description': ['Description1', 'Description2', 'Description3'],
    'Image': [True, False, True]
}

df = pd.DataFrame(data)

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
    st.image(selected_row['Image_Path'], caption='Selected Image', use_column_width=True)

else:
    st.warning('No results found.')


st.subheader('Entire DataFrame')
st.write(df)
