from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import streamlit as st
from pathlib import Path
import numpy as np
import os

# Setting up category lists
dress = []
shoes = []
pants = []
shirts = []
unidentified = []
fileNames = []

# Defining the categories
categories = ['Dress', 'Pant', 'Shirt', 'Shoe'] 

# Loading the saved model
model = load_model('models/clothing_cnn_model_v2.h5')

# Function for image prediction
def predict_category(image_path):
    # Load and preprocess the image
    img = image.load_img(image_path, target_size=(64, 64))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)/255.0
    
    # Predict the class probabilities
    prediction = model.predict(img_array)
    predicted_class = np.argmax(prediction)
    category = categories[predicted_class]

    return category

# Sorting function
def sort_items(output_placeholder, folder_path):
    if not folder_path:
        output_placeholder.error("Please enter a folder path.")
    elif not os.path.isdir(folder_path):
        output_placeholder.error("Invalid folder path. Folder does not exist.")
    else:
        # Example processing: list files and count them
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        num_files = len(files)

        folder = Path(folder_path)

        fileNames = [file.name for file in folder.iterdir() if file.is_file()]

        for i in fileNames:
            file_path = f'{folder_path}/{i}'
            prediction = predict_category(file_path)
            if prediction == 'Dress':
                dress.append(i)
            elif prediction == 'Shoe':
                shoes.append(i)
            elif prediction == 'Pant':
                pants.append(i)
            elif prediction == 'Shirt':
                shirts.append(i)
            else:
                unidentified.append(i)

        # Display results in a separate field
        with output_placeholder.container():
            # --- Output section ---
            st.subheader("Results")
            st.success("Folder processed successfully!")
            st.write(f"**Folder Path:** {folder_path}")
            st.write(f"**Number of files:** {num_files}")

            st.subheader(f"Inventory Summary:")
            st.write(f"**Dresses:** {len(dress)}")
            st.write(f"**Pants:** {len(pants)}")
            st.write(f"**Shirts:** {len(shirts)}")
            st.write(f"**Shoes:** {len(shoes)}")
            st.write(f"**Unidentified:** {len(unidentified)}")

            st.subheader("Item Categores And List Of File Names")
            if len(dress) > 0:
                st.write("**Dresses:**")
                st.dataframe(dress)
            else:
                st.info("No dress found in this folder.")

            if len(pants) > 0:
                st.write("**Pants:**")
                st.dataframe(pants)
            else:
                st.info("No pants found in this folder.")
            
            if len(shirts) > 0:
                st.write("**Shirts:**")
                st.dataframe(shirts)
            else:
                st.info("No shirts found in this folder.")
            
            if len(shoes) > 0:
                st.write("**Shoes:**")
                st.dataframe(shoes)
            else:
                st.info("No shoes found in this folder.")

            if len(unidentified) > 0:
                st.write(f"**Unidentified:** {unidentified}")
                st.dataframe(unidentified)
            else:
                st.info("No unidentifed item found in this folder.")