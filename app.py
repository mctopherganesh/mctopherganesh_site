import streamlit as st
import streamlit as st
from streamlit_lottie import st_lottie
import requests
import json
from PIL import Image

st.set_page_config(page_title="mctopherganesh.io", page_icon=":grin:", layout="wide")


# load assets


def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottie_url("https://assets3.lottiefiles.com/packages/lf20_1cazwtnc.json")
img_prof_pic = Image.open("images/prof_pic.jpeg")


# header section
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Hello I'm Christopher")
        st.title("Data Programmer")
        st.write("I am passionate about using data to improve internal processes, decrease waste, and refine production.")
    with right_column:
        st.image(img_prof_pic)

        

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
        """
        By day, I am a software analyst, managing clients, internal resources from multiple different
        departments and countries, working to resolve bugs and configuration errors. My work ethos are 
         explicit and open communication, the elimination of waste in production workflow,
        and laying foundation for continued improvement. I have professional experience in constructing 
        automated testing frameworks, data mining, and a decade of combined client experience in sales, support
        and consulting.

        By night, I am a self-learning-data-sleuthing-python-programming-technodork who blogs. My journey
        is captured in written shenanigans. Presently I am studying through courses in Machine Learning and 
        building bots, and working towards my Google Analytics and Greenbelt Six Sigma certifications. 

        When I'm not doing any of that I am on bike ride or reading or at my favorite coffee shop writing. 
        """
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        # insert image
        pass
    with text_column:
        st.subheader("Discord Blood Sugar Bot")
        st.write(
            """
        insert text here
        
        
        """
        )

with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/mctopherganesh.com" method="POST">
     <input type="hidden" name="_captacha" value="false">   
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here:" required></textarea>
     <button type="submit">Send</button>
</form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()




