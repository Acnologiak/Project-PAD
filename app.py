import streamlit as st
import pickle

model = pickle.load(open("model.sv",'rb'))

# Diabetes_binary: min - 0.0, max - 1.0 i
# HighBP: min - 0.0, max - 1.0 i
# HighChol: min - 0.0, max - 1.0 i
# CholCheck: min - 0.0, max - 1.0 i
# BMI: min - 12.0, max - 98.0 i
# Smoker: min - 0.0, max - 1.0 i
# Stroke: min - 0.0, max - 1.0 i
# HeartDiseaseorAttack: min - 0.0, max - 1.0 i
# PhysActivity: min - 0.0, max - 1.0 i
# Fruits: min - 0.0, max - 1.0 i
# Veggies: min - 0.0, max - 1.0 i
# HvyAlcoholConsump: min - 0.0, max - 1.0 i
# AnyHealthcare: min - 0.0, max - 1.0 i
# NoDocbcCost: min - 0.0, max - 1.0 i
# GenHlth: min - 1.0, max - 5.0 i
# MentHlth: min - 0.0, max - 30.0 i
# PhysHlth: min - 0.0, max - 30.0 i
# DiffWalk: min - 0.0, max - 1.0 i
# Sex: min - 0.0, max - 1.0 w
# Age: min - 1.0, max - 13.0 i
# Education: min - 1.0, max - 6.0 i
# Income: min - 1.0, max - 8.0 i

def main():

	st.set_page_config(page_title="Heart Disease")
	overview = st.container()
	left, right = st.columns(2)
	prediction = st.container()

	st.image("https://health.clevelandclinic.org/wp-content/uploads/sites/3/2020/01/mildHeartAttack-866257238-770x553.jpg")

	with overview:
		st.title("Heart Disease")


if __name__ == "__main__":
    main()
