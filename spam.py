import streamlit as st
import pickle

mode1 = pickle.load(open('spam.pk1','rb'))
cv = pickle.load(open('vec.pk1','rb'))
 
def main():
    st.title("Email Spam Classification Application")
    st.write("This is a Machine Learning application to classify emails as spam or ham.")
    st.subheader("Classification")
    user_input=st.text_area("Enter an email to classify", height=150)
    if st.button("Classify"):
        if user_input:
            data=[user_input]
            print(data)
            vec=cv.transform(data).toarray()
            result=mode1.predict(vec)
            if result[0]==0:
                st.success("this is not a spam mail")
            else:
                st.error("This is a Spam mail")
        else:
            st.write("please enter an email to classify.")
main()