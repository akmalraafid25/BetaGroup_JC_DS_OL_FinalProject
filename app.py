import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import numpy as np

# === Load Dataset ===
@st.cache_data
def load_data():
    df = pd.read_csv("bank-additional-full.csv", sep=";")
    return df

# === Load Model ===
@st.cache_resource
def load_model():
    with open("model.sav", "rb") as f:
        model = pickle.load(f)
    return model

df = load_data()
model = load_model()

st.title("📊 Analisis & Prediksi Telemarketing Deposito Berjangka")

# === Sidebar Filter Data ===
st.sidebar.header("🎛️ Filter & Input")

st.sidebar.subheader("Filter Data")
job_filter = st.sidebar.multiselect("Pekerjaan:", df["job"].unique(), default=df["job"].unique())
edu_filter = st.sidebar.multiselect("Pendidikan:", df["education"].unique(), default=df["education"].unique())

filtered_df = df[(df["job"].isin(job_filter)) & (df["education"].isin(edu_filter))]

# === Sidebar Input Prediksi ===
st.sidebar.subheader("Prediksi Probabilitas")
input_data = {}
for col in df.columns[:-1]:
    if df[col].dtype == object:
        input_data[col] = st.sidebar.selectbox(f"{col}", sorted(df[col].unique()))
    else:
        input_data[col] = st.sidebar.number_input(f"{col}", float(df[col].min()), float(df[col].max()), float(df[col].mean()))

input_df = pd.DataFrame([input_data])

# === Main Area ===
st.header("1️⃣ Eksplorasi Dataset")
if st.checkbox("Tampilkan Data Mentah"):
    st.dataframe(df)

st.markdown(f"Jumlah baris: **{filtered_df.shape[0]}**, Kolom: **{filtered_df.shape[1]}**")

st.subheader("Statistik Deskriptif")
st.write(filtered_df.describe())

st.subheader("Distribusi Target")
fig1, ax1 = plt.subplots()
sns.countplot(data=filtered_df, x="y", ax=ax1)
st.pyplot(fig1)

st.subheader("Heatmap Korelasi")
numeric_cols = filtered_df.select_dtypes(include=["int64", "float64"]).columns
if len(numeric_cols) >= 2:
    fig2, ax2 = plt.subplots()
    sns.heatmap(filtered_df[numeric_cols].corr(), annot=True, cmap="coolwarm", ax=ax2)
    st.pyplot(fig2)

# === Prediksi ===
st.header("2️⃣ Prediksi Probabilitas Nasabah Berlangganan")

# Gabungkan dan encode input
combined = pd.concat([df.drop(columns='y'), input_df], axis=0)
combined_encoded = pd.get_dummies(combined)
input_encoded = combined_encoded.tail(1)

# Lengkapi kolom model jika ada yang hilang
model_features = model.feature_names_in_
missing_cols = set(model_features) - set(input_encoded.columns)
for col in missing_cols:
    input_encoded[col] = 0
input_encoded = input_encoded[model_features]

# Prediksi
proba = model.predict_proba(input_encoded)[0][1]

st.metric("Probabilitas Berlangganan", f"{proba*100:.2f}%")
