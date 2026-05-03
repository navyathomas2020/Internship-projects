# CNN Image Classification - Cats vs Dogs

## Project Overview

This project implements a **Convolutional Neural Network (CNN)** to classify images of cats and dogs.
The model is trained using an augmented dataset and deployed using a **Streamlit web application**.

---

## CNN Architecture

The CNN model consists of the following layers:

* **Convolutional Layers** → Extract features like edges and shapes
* **ReLU Activation** → Adds non-linearity
* **MaxPooling Layers** → Reduces image size and keeps important features
* **Flatten Layer** → Converts 2D feature maps into 1D
* **Dense Layers** → Perform classification
* **Output Layer (Sigmoid)** → Binary classification (Cat / Dog)

---

## Technologies Used

* Python
* TensorFlow / Keras
* Streamlit
* NumPy
* PIL (Image Processing)

---

## Dataset

* Dataset: *Cats vs Dogs Augmented Dataset (Kaggle)*
* Contains images of cats and dogs
* Images are preprocessed and augmented for better accuracy

---

## How to Run the Project

### Step 1: Install dependencies

```bash
pip install -r requirements.txt
```

---

### Step 2: Train the Model

Open and run:

```
Deep_Learning/cnn_model.ipynb
```

👉 This will generate:

```
cnn_model.h5
```

---

### Step 3: Run Streamlit App

Go to Streamlit folder:

```bash
cd Streamlit_Apps/cnn_file
streamlit run streamlit_app.py
```

---

## 📸 Output

* Upload an image (cat or dog)
* The model predicts the class
* Displays result in the web app

(Screenshot included in repository)

---

## Important Note

The trained model file `cnn_model.h5` is **not uploaded** due to GitHub file size limitations.

👉 To use the app:

1. Run the notebook (`cnn_model.ipynb`)
2. It will generate `cnn_model.h5`
3. Place it inside the Streamlit folder
4. Then run the app

---



## Results

* The model successfully classifies images of cats and dogs
* Accuracy depends on training but performs well on test images

---

## Conclusion

This project demonstrates:

* Image classification using CNN
* Model training using TensorFlow/Keras
* Deployment using Streamlit

---

## Author

Navya Thomas
