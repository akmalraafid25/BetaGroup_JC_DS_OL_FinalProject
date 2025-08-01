import streamlit as st
import pandas as pd
import pickle

# Load model
with open("model.sav", "rb") as f:
    model = pickle.load(f)

# Load dataset untuk ambil unique value
@st.cache_data
def load_data():
    df = pd.read_csv("bank-additional-full.csv", sep=";")
    return df

df = load_data()

st.title("🎯 Prediksi Term Deposit")

st.markdown("Masukkan karakteristik nasabah. Input diambil dari nilai unik dataset asli.")

# Ambil unique value dari dataset untuk tiap kolom
def get_unique(col):
    return sorted(df[col].dropna().unique().tolist())

# Slider age
age = st.slider("Umur", min_value=int(df["age"].min()), max_value=int(df["age"].max()), value=30)

job = st.selectbox("Pekerjaan", get_unique("job"))
marital = st.selectbox("Status Pernikahan", get_unique("marital"))
education = st.selectbox("Pendidikan", get_unique("education"))
default = st.selectbox("Kredit macet sebelumnya?", get_unique("default"))
housing = st.selectbox("Pinjaman rumah?", get_unique("housing"))
loan = st.selectbox("Pinjaman pribadi?", get_unique("loan"))
contact = st.selectbox("Jenis kontak", get_unique("contact"))
month = st.selectbox("Bulan terakhir dihubungi", get_unique("month"))
day_of_week = st.selectbox("Hari dalam minggu", get_unique("day_of_week"))
campaign = st.selectbox("Jumlah kontak selama kampanye ini", sorted(df["campaign"].unique()))
pdays = st.selectbox("Hari sejak terakhir dihubungi (-1 = belum pernah)", sorted(df["pdays"].unique()))
previous = st.selectbox("Jumlah kontak sebelumnya", sorted(df["previous"].unique()))
poutcome = st.selectbox("Hasil kampanye sebelumnya", get_unique("poutcome"))
emp_var_rate = st.selectbox("Variasi tingkat pekerjaan", sorted(df["emp.var.rate"].unique()))
cons_price_idx = st.selectbox("Indeks harga konsumen", sorted(df["cons.price.idx"].unique()))
cons_conf_idx = st.selectbox("Indeks kepercayaan konsumen", sorted(df["cons.conf.idx"].unique()))
euribor3m = st.selectbox("Suku bunga Euribor 3 bulan", sorted(df["euribor3m"].unique()))
nr_employed = st.selectbox("Jumlah pekerja", sorted(df["nr.employed"].unique()))

# Generate kolom tambahan pdays_grouped
def group_pdays(val):
    if val in [-1, 999]:
        return "never"
    elif val < 7:
        return "recent"
    else:
        return "late"

pdays_grouped = group_pdays(pdays)

# Buat dataframe input
input_data = pd.DataFrame([{
    'age': age,
    'job': job,
    'marital': marital,
    'education': education,
    'default': default,
    'housing': housing,
    'loan': loan,
    'contact': contact,
    'month': month,
    'day_of_week': day_of_week,
    'campaign': campaign,
    'pdays': pdays,
    'previous': previous,
    'poutcome': poutcome,
    'emp.var.rate': emp_var_rate,
    'cons.price.idx': cons_price_idx,
    'cons.conf.idx': cons_conf_idx,
    'euribor3m': euribor3m,
    'nr.employed': nr_employed,
    'pdays_grouped': pdays_grouped
}])

# Tampilkan input
with st.expander("📋 Lihat Input Data"):
    st.dataframe(input_data)

# Prediksi
if st.button("Prediksi"):
    try:
        pred = model.predict(input_data)[0]
        if pred == 1:
            st.success("✅ Nasabah diprediksi akan **BERLANGGANAN** term deposit.")
        else:
            st.warning("❌ Nasabah diprediksi **TIDAK** akan berlangganan.")

    except Exception as e:
        st.error(f"Terjadi error saat memproses prediksi: {e}")
