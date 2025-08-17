# 🍎🍌 Fruit Classifier – FastAI + Gradio

This project is my **Day 2 project from the FastAI Deep Learning course**.  
It trains a deep learning model to classify **healthy vs rotten fruits**, exports the model, and deploys it as a live web app using **Gradio** and **Hugging Face Spaces**.

---


## ⚙️ How it Works
1. **Dataset**: Images of healthy and rotten fruits collected using DuckDuckGo search.  
2. **Training**: FastAI was used to train a model.  
3. **Export**: Model was exported as `model.pkl`.  
4. **Deployment**: A Gradio app (`app.py`) loads the model and allows users to upload fruit images for classification.  

---

## 🛠️ Installation & Usage
Clone the repo:
```bash
git clone https://github.com/uswakk/Rotten-VS-Healthy-Fruit-Classifier.git
cd Rotten-VS-Healthy-Fruit-Classifier
