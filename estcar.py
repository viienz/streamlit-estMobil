import pickle
import streamlit as st

model = pickle.load(open('estimasi_mobil.sav', 'rb'))

st.title('Estimasi Harga Mobil')

year = st.number_input('Input Tahun Mobil')
mileage = st.number_input('Input Km Mobil')
tax = st.number_input('Input Pajak')
mpg = st.number_input('Input Konsumsi BBM')
engineSize = st.number_input('Input Ukuran Mesin')

prediction = ''

if st.button('Estimasi Harga'):
    prediction = model.predict(
        [[year, mileage, tax, mpg, engineSize]])

    st.write('Estimasi Harga Mobil dalam ponds: ', prediction)
    st.write('Estimasi Harga Mobil dalam Rupiah: ', prediction*19000)
    