import pickle
import streamlit as st

# Load the trained model
model = pickle.load(open("Insurance.pkl", "rb"))

def depModel():
    st.title("Insurance Prediction Web App")

    # Input field for age
    age = st.number_input("Enter Age:", min_value=0, max_value=120, step=1)

    # Prediction button
    if st.button("Predict Insurance Status"):
        # Predict (assuming your model expects one feature: age)
        result = model.predict([[age]])[0]

        # Show result clearly
        if result == 1:
            st.success("Person is likely to take insurance (YES)")
        else:
            st.warning("Person is not likely to take insurance (NO)")

#  Make sure to actually call the function
if __name__ == "__main__":
    depModel()
