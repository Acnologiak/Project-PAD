import streamlit as st
import pickle

model = pickle.load(open("model.sv",'rb'))

yesNo = {0:"No", 1:"Yes"}
sex = {0:"Female", 1:"Male"}

def main():

	st.set_page_config(page_title="Diabetes")
	overview = st.container()
	left, right = st.columns(2)
	prediction = st.container()

	with overview:
		st.title("Diabetes")
		st.write("Here you can fill in the form and get information on whether you are at risk of getting diabetes.")

	with left:
		_highBP = st.radio("Do you have high blood pressure?", list(yesNo.keys()), format_func=lambda x: yesNo[x])
		_highChol = st.radio("Do you have high cholesterol?", list(yesNo.keys()), format_func=lambda x: yesNo[x])
		_cholCheck = st.radio("Have you checked for cholesterol in 5 years?", list(yesNo.keys()),
							  format_func=lambda x: yesNo[x])
		_BMI = st.slider("Your body mass index", value=22, min_value=10, max_value=100)
		_smoker = st.radio("Have you smoked at least 100 cigarettes in your entire life?", list(yesNo.keys()),
						   format_func=lambda x: yesNo[x])
		_stroke = st.radio("Did you have a stroke?", list(yesNo.keys()), format_func=lambda x: yesNo[x])
		_heartDiseaseorAttack = st.radio("Did you have a coronary heart disease or myocardial infarction?",
										 list(yesNo.keys()), format_func=lambda x: yesNo[x])
		_physActivity = st.radio("Have you had any physical activity in the last 30 days except work?",
								 list(yesNo.keys()), format_func=lambda x: yesNo[x])
		_fruits = st.radio("Do you eat fruit at least once a day?", list(yesNo.keys()), format_func=lambda x: yesNo[x])
		_vegetables = st.radio("Do you eat vegetables at least once a day?", list(yesNo.keys()),
							   format_func=lambda x: yesNo[x])
		_hvyAlcoholConsump = st.radio(
			"Do you heavy drinkers (adult men having more than 14 drinks per week and adult women having more than 7 drinks per week)?",
			list(yesNo.keys()), format_func=lambda x: yesNo[x])

	with right:
		_anyHealthcare = st.radio(
			"Do you have any kind of health care coverage, including health insurance, prepaid plans such as HMO?",
			list(yesNo.keys()), format_func=lambda x: yesNo[x])
		_noDocbcCost = st.radio(
			"Was there a time in the past 12 months when you needed to see a doctor but could not because of cost?",
			list(yesNo.keys()), format_func=lambda x: yesNo[x])
		_genHlth = st.slider(
			"Would you say that in general your health is: 1 = excellent, 2 = very good, 3 = good, 4 = fair, 5 = poor?",
			value=2, min_value=1, max_value=5)
		_mentHlth = st.slider(
			"Now thinking about your mental health, which includes stress, depression, and problems with emotions, for how",
			value=5, min_value=1, max_value=30)
		_physHlth = st.slider(
			"Now thinking about your physical health, which includes physical illness and injury, for how many days during the past 30",
			value=5, min_value=1, max_value=30)
		_diffWalk = st.radio("Do you have serious difficulty walking or climbing stairs?", list(yesNo.keys()),
							 format_func=lambda x: yesNo[x])
		_sex = st.radio("Sex", list(sex.keys()), format_func=lambda x: sex[x])
		_age = st.slider("Your age in the 13-level age category", value=2, min_value=1, max_value=13)
		_education = st.slider("Your level of education according to EDUCA", value=5, min_value=1, max_value=6)
		_income = st.slider("How do you feel about your income level: 1 - low, 8 - high?", value=4, min_value=1,
							max_value=8)

	data = [[_highBP, _highChol, _cholCheck, _BMI, _smoker, _stroke, _heartDiseaseorAttack, _physActivity, _fruits,
			 _vegetables, _hvyAlcoholConsump, _anyHealthcare, _noDocbcCost, _genHlth, _mentHlth, _physHlth, _diffWalk,
			 _sex, _age, _education, _income]]
	chances = model.predict(data)

	with prediction:
		st.subheader("Your result:")
		if (chances[0] == 0):
			st.write("You are not at risk, but you need to take care of yourself.")
		else:
			st.write("You are at risk and you need to change something in your life to prevent diabetes.")

if __name__ == "__main__":
    main()

