# from dotenv import load_dotenv
# load_dotenv()

from langchain.chat_models import ChatOpenAI
chat_model = ChatOpenAI()

import streamlit as st

st.title('인공지능 시인')
content = st.text_input('시 제목을 입력해주세요!')

if st.button('시 한수 써 줄래?'):
    with st.spinner('시를 짓고 있습니다!  시간이 조금 걸릴 수 있습니다!  잠시만 기다려주세요...'):
        # time.sleep(5)
        result = chat_model.predict(content + "에 대한 시를 써 줘!")
        # st.write('시 제목: ', content)
        # st.write('인공지능이 자작한 시: ')
        st.write(result)

