import streamlit as st
import pickle


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
