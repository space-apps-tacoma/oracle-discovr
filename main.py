import numpy as np
import pandas as pd
import streamlit as st

import plasmag_data_labels as pdl  # custom for project

st.title('Shockwave Surfers - NASA Space Apps Challenge 2023 - Tacoma Location')

# example usage of pdl
# print(pdl.data_labels)

spectra_df = pd.read_csv("./data/dsc_fc_summed_spectra_2023_v01.csv")
spectra_df.columns = pdl.data_labels
st.subheader("dsc fc summed spectra 2023 v01")
st.dataframe(spectra_df.head(2))

st.subheader("CASSIOPE_Sub Data Set")
cassiope_df = pd.read_csv("./data/CASSIOPE_Sub_Data_Set.csv")
st.dataframe(cassiope_df.head(10))

st.subheader("kP-index-data")
kp_index_df = pd.read_csv("./data/kP-index-data.csv")
st.dataframe(kp_index_df.head(10))
