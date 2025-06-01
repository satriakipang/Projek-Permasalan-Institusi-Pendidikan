import streamlit as st
import pandas as pd
import joblib
import pickle

# Load model dan fitur
model = joblib.load('model/model_selected_columns.pkl')
used_features = joblib.load('model/used_features.pkl')

# Mapping hasil prediksi
status_mapping = {0: 'Dropout', 1: 'Graduate'}

# Judul Aplikasi
st.markdown(
    "<h1 style='text-align: center; font-size: 60px;'>Jaya Jaya Institut</h1>",
    unsafe_allow_html=True
)
st.title("Aplikasi Prediksi Status Mahasiswa")
st.write("Masukkan data mahasiswa untuk memprediksi apakah akan Dropout atau Graduate.")

# Input pengguna
user_input = {}
user_input['Curricular_units_1st_sem_approved'] = st.number_input("1st Sem - Units Approved", min_value=0, step=1)
user_input['Curricular_units_1st_sem_grade'] = st.number_input("1st Sem - Grade", min_value=0.0, max_value=20.0, step=0.1)
user_input['Curricular_units_2nd_sem_approved'] = st.number_input("2nd Sem - Units Approved", min_value=0, step=1)
user_input['Curricular_units_2nd_sem_grade'] = st.number_input("2nd Sem - Grade", min_value=0.0, max_value=20.0, step=0.1)
user_input['Previous_qualification_grade'] = st.number_input("Previous Qualification Grade", min_value=0.0, max_value=200.0, step=0.1)
user_input['Admission_grade'] = st.number_input("Admission Grade", min_value=0.0, max_value=200.0, step=0.1)


# Tombol prediksi
if st.button("Prediksi Status"):
    # Buat DataFrame dan sesuaikan urutan kolom
    user_df = pd.DataFrame([user_input])
    user_df = user_df[used_features]

    # Prediksi
    prediction = model.predict(user_df)[0]

    # Tampilkan hasil
    st.subheader("Hasil Prediksi:")
    st.success(f"Status Mahasiswa diprediksi akan **{status_mapping[prediction]}**")
