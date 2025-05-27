# phishing_gui.py
import tkinter as tk
from tkinter import messagebox
import pickle
import numpy as np

# Load model and vectorizer
try:
    with open("phishing_model.pkl", "rb") as f:
        model = pickle.load(f)
    with open("vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)
except Exception as e:
    print("❌ Error loading model or vectorizer:", e)
    exit()

def check_email():
    email_text = email_entry.get("1.0", tk.END).strip()

    if not email_text:
        messagebox.showwarning("Input Error", "Please enter an email body.")
        return

    vec = vectorizer.transform([email_text])
    prediction = model.predict(vec)[0]
    probabilities = model.predict_proba(vec)[0]
    confidence = round(np.max(probabilities) * 100, 2)

    if prediction == 1:
        result = f"⚠️ Phishing Detected!\nConfidence: {confidence}%"
        result_label.config(text=result, fg="red")
    else:
        result = f"✅ Email is Safe.\nConfidence: {confidence}%"
        result_label.config(text=result, fg="lightgreen")

# GUI setup
root = tk.Tk()
root.title("PhishShield - Email Phishing Detector")
root.geometry("600x400")
root.configure(bg="#2e2e2e")

tk.Label(root, text="Enter Email Body Below:", font=("Helvetica", 14), bg="#2e2e2e", fg="white").pack(pady=10)

email_entry = tk.Text(root, height=10, width=70, bg="#3e3e3e", fg="white", insertbackground="white", wrap="word")
email_entry.pack(padx=10)

tk.Button(root, text="Check Email", font=("Helvetica", 12, "bold"), bg="#444", fg="white", command=check_email).pack(pady=15)

result_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"), bg="#2e2e2e")
result_label.pack(pady=20)

root.mainloop()
