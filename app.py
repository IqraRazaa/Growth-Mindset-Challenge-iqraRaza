#streamlit
import streamlit as st

st.set_page_config(page_title="page_title=Growth Mind Set",page_icon="⭐")               
st.title("Growth Mindset:Web App With Streamlit 📖👩‍🎓")
st.header("💎 Welcome to your Growth Journey!")
st.write("Difficult challenges", "learn from mistake",
"This is Ai App power ","growth mindset leads to greater success", "and fulfillment in both personal and professional life.")
#quote section
st.header("🏆Today's Growth Mindset Quote")
st.write("Embrace challenges, learn from failures, and keep pushing forward!🚀✨")

st.header("💪What is your challenges today")
user_input= st.text_input("Describe a challenges you are facing;")

#condition use loop function
if user_input:
    st.success(f" you are facing: {user_input}.keep pushing forward achive your goal")
else:
    st.warning("Tell us about your challenges to get started!🎯")

#reflection
st.header("🧠Reflect on your Learning")
reflection = st.text_area("Write your reflection here")

#condition use loop function
if reflection:
    st.success(f"✨ Great insight your reflection !{reflection}")
else:
    st.info("Reflecting on past experience help grow! Share your difficulties & problems")

##condition use loop function
st.header("🏆🥉 Celebrate your Wins!")
achivements =st.text_input ("Share  something you have recently accomploshied; ")

#condition use loop function
if achivements:
    st.success(f"✨🎉 Amazing !You achived:  !{achivements}")
    st.button("→⇉ More motivation")
else:
    st.info("small or huge every achivement counts! Share one now🎊")

#footer
st.write("- - -")
st.write("🚀keep beliving in yours self ;Growth is a journey,not a destination🎈")







