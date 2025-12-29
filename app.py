import streamlit as st
from tkinter import Tk, filedialog
from ui_components import sort_items

def select_folder():
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    folder_path = filedialog.askdirectory()
    root.destroy()
    return folder_path

st.set_page_config(page_title="Clothing Inventory Sorting App", layout="centered")

# Intro section
st.markdown(
    "<h1 style='text-align: center;'>Clothing Inventory Sorting App</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center;'>We sort and summarize saving time and energy...</p>",
    unsafe_allow_html=True
)


# Input field
st.header("Enter path or Select a Folder")

col1, col2 = st.columns([4,1])

with col1:
    path = st.text_input(
        "Enter folder directory path: ", 
        placeholder="e.g. C:/users/YourName/Documents/data"
        )
    
with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    submit = st.button("Submit")

selectFolder = st.button("Select Folder")

output_placeholder = st.empty()

if submit:
    folder = path
    sort_items(
        output_placeholder=output_placeholder,
        folder_path=folder
    )

if selectFolder:
    folder = select_folder()
    sort_items(
        output_placeholder=output_placeholder,
        folder_path=folder
    )


# --- Footer ---
st.markdown("---")
st.caption("Streamlit Visualization Setup")