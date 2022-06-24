import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# PASSWORD PROTECTED
password = st.text_input("Enter the password:")
if password != st.secrets["password"]:
    st.stop()

# RESIZE THE PAGE WIDTH AND SET THE TITLE
# st.set_page_config(layout="wide")
st.title("Penguin App")
st.markdown('Use this Streamlit App to make your own scatterplot.')


# IMPORT DATA
penguin_df = pd.read_csv('penguins.csv')
# st.write(penguin_df.head())


# GET USER INPUT
# selected_species = st.selectbox('What species?',
#                                ['Adelie', 'Gentoo', 'Chinstrap'])

# penguin_df = penguin_df[penguin_df['species'] == selected_species]


x = st.selectbox('Select the X variable:',
                 ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm',
                  'body_mass_g'])

y = st.selectbox('Select the Y variable:',
                 ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm',
                  'body_mass_g'])



# SHOW THE PLOT
fig, ax = plt.subplots()
ax = sns.scatterplot(x=penguin_df[x], y=penguin_df[y], hue=penguin_df['species'])
# plt.title(f'{selected_species} Penguins')
plt.title('Penguins')
plt.xlabel(x)
plt.ylabel(y)
st.pyplot(fig)
