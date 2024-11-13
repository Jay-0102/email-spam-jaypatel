import streamlit as st
import pickle

model=pickle.load(open('spam.pkl','rb'))
cv=pickle.load(open('vectorizer.pkl','rb'))

st.title("Email Spam Classification Application")
st.write("This is machine Learining application to classify emalis as spam or ham")
user_input=st.text_area("Enter Email Data:",height=200)

if st.button("Classify"):
    if user_input:
        data=[user_input]
        vect=cv.transform(data).toarray()
        pred=model.predict(vect)
        if pred[0]==0:
            st.success("This email is not spam")
        else:
            st.error("This is spam email")
    else:
        print("Pleasr type email")