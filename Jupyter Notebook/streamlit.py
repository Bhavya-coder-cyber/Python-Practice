import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv("Salary.csv")

x = data[['YearsExperience']]
y = data[['Salary']]

model = LinearRegression()
model.fit(x,y)

st.title("Salary Prediction App")
st.write("Enter your years of experience to predict your salary:")

experience = st.number_input("Years of Experience", min_value=0.0, max_value=50.0, step=0.1, key="experience")

if experience:
    print(f"{experience}")

# print(f"{model.predict([[experience]])}")
    predicted_salary = round(model.predict([[experience]])[0][0],2)
    st.success(f"Predicted Salary: ${predicted_salary}")
st.subheader("Salary vs Years of Experience")

fig, ax = plt.subplots()
ax.scatter(x,y,color="blue",label="Actual Data")
ax.plot(x,model.predict(x),color="red",label="Regression Line")
ax.set_xlabel("Years Of Experience")
ax.set_ylabel("Salary")
ax.set_title("Salary VS Experience")
ax.legend()
st.pyplot(fig)