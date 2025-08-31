import streamlit as st 
import requests 

st.set_page_config(page_title='codebase qa assistant',layout='wide')

st.title('code base qa Assistant') 
st.markdown("Ask questions about your codebase and get intelligent answers using langchain FAISS and ollama")

question = st.text_input('Enter your question: ',placeholder='e.g. Where is the database connection initialized?')

if st.button("Ask"):
    if question.strip():
        with st.spinner('Thinking....'):
            response = requests.post('http://backend:8000/chat',json={'question':question})
            answer = response.json().get('answer','no answer returned')
            st.markdown('Answer ')
            st.write(answer['content'])
    else:
        st.warning('Please enter a question.')