# 👕 Clothing Inventory Sorting App Using CNN

## 📌 Project Overview

This project implements a **Clothing Inventory Sorting Application** using a **Convolutional Neural Network (CNN)** to automatically identify and categorize clothing items from images. The system classifies clothing into predefined categories—**dress, pants, shirt, and shoes**—and generates a summarized inventory count based on the classified results.

The application is designed to reduce the time, effort, and errors associated with manual inventory sorting by leveraging **deep learning and computer vision techniques**.

---

## 🎯 Problem Statement

Manual clothing inventory sorting is often time-consuming, repetitive, and mentally demanding. It typically requires repeated verification to ensure accuracy, which can lead to fatigue and inefficiency. This project provides an automated solution that identifies clothing items from images and accurately categorizes them, producing a clear summary of available inventory.

---

## 🧠 Solution Approach

A **Convolutional Neural Network (CNN)** was chosen due to its effectiveness in image classification tasks. CNNs automatically learn spatial features such as edges, textures, and shapes, making them ideal for recognizing clothing items from images.

### Key Steps Involved:

* Data collection and labeling
* Image preprocessing (resizing, normalization)
* Data augmentation (rotation, flipping, zooming)
* CNN model design and compilation
* Model training and hyperparameter tuning
* Model evaluation and testing
* Local deployment using Streamlit

---

## 🏗️ Model Architecture

The CNN model consists of:

* **Convolutional layers** for feature extraction
* **MaxPooling layers** for dimensionality reduction
* **ReLU activation functions** for non-linearity
* **Fully connected (Dense) layers** for classification
* **Softmax output layer** for multi-class prediction

The model was trained to classify images into four categories:

* Dress
* Pants
* Shirt
* Shoes

---

## 📊 Results & Performance

* Initial training accuracy: **82%**
* Final optimized accuracy: **97%**

Model tuning and data augmentation significantly improved performance, resulting in accurate and reliable predictions across unseen image folders.
Link to the models: https://drive.google.com/drive/folders/1Gvnw6rDn4IwrHw9ckNtS5BsdCiUKGATj?usp=drive_link

---

## 🚀 Deployment

The trained model was deployed locally using **Streamlit**, providing an interactive interface where users can:

* Upload clothing images or folders
* View predicted categories
* Obtain a summarized inventory count per category

This deployment demonstrates how the model can be applied in real-world inventory management scenarios.

---

## 🛠️ Technologies Used

* Python
* TensorFlow / Keras
* Convolutional Neural Networks (CNN)
* NumPy
* Matplotlib
* Streamlit

---

## 📁 Project Use Cases

* Retail inventory management
* Automated stock counting
* Image-based product categorization
* AI-powered inventory systems

---

## 📌 Conclusion

This project showcases the practical application of **Convolutional Neural Networks in image classification** by solving a real-world inventory management problem. By combining deep learning, image processing, and web deployment, the system delivers an efficient, scalable, and user-friendly solution for automated clothing inventory sorting.

---

