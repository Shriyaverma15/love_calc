import streamlit as st
import time

#import kra hai bss!

def love_calculator1(): #function banaya
    st.set_page_config(page_title="LOVE CALCULATOR", page_icon="💖", layout="centered")
    st.title("💖 Love Calculator 💖")
    st.header("💖 Love Calculator 💖"
              "✨ Unlock Your Love Story!✨"
              "🌟 Are You Meant to Be? 🌟"
              "💫 Let the Stars Reveal Your Fate! 💫"
              "🔮 Enter Your Names & Feel the Magic! 🔮"
              "💌 True Love is Just a Click Away! 💌"
              "❤️ Destiny Awaits You Both! ❤️")

#quick layouts and kind of eye catchy layouts daale!

    column1, column2 = st.columns(2) #do alag alag columns banaye!

    with column1:
        st.header("First Name")
        name1 = st.text_input("Enter:", key="name1") #coulmn1 ke upar like as a header ek Text input kiya and then user ko naam enter krne ke liye space create krke type krne ki freedom diiiii

    with column2:
        st.header("Second Name")
        name2 = st.text_input("Enter:", key="name2")

    if name1 and name2:
#name1 ki calculations process hogi
        name1 = name1.replace(" ", "").upper()  #spaces ko hatayega and small characters ko upper char mein lekr jaayega taaki processing simple and easy ho ske
        sum_of_the_digit = sum(ord(a) - ord('A') + 1 for a in name1 if 'A' <= a <= 'Z')
        while sum_of_the_digit >= 10: #agr sum 10 se upr hai ya phir 2 digit ya 3 + digit ka hai then yeh statement further implement hogi ya phir esa smjho ki yeh code implement hoga..
            sum_of_the_digit = sum(int(digit) for digit in str(sum_of_the_digit))

#name2 ki calculations process hogi
        name2 = name2.replace(" ", "").upper()
        sum_of_the_digitt = sum(ord(a) - ord('A') + 1 for a in name2 if 'A' <= a <= 'Z')
        while sum_of_the_digitt >= 10:
            sum_of_the_digitt = sum(int(digit) for digit in str(sum_of_the_digitt))

        combined_result = str(sum_of_the_digit) + str(sum_of_the_digitt) #dono digits ko concatenate kra , means joda sath mein rather than add kra..

        #spinner laane se ek rotatory spinner humare pass aajayega to like make the website more responsive acc to me...
        with st.spinner('Calculating your love percentage...'):
            time.sleep(10) #spinner rotation ko proper time diya 10 secs

        st.success(f"💖 Your Love Percentage is: {combined_result}% 💖") #yahan pr calculate hokr aayega


        if int(combined_result) > 80:
            st.balloons()  #extra kiya hai bs taaki if result according to condition aaye then balloons appear honge
            st.markdown("**You two are a match made in heaven! 💕**")
        elif int(combined_result) < 50: #warning means red mark ke andr text likhkr aayega
            st.warning("**Don't worry, it's just for fun! ❤️**")
        else:
            st.success("**Great!!! You have good amount of chances too ❤️**")
            #success means green mark ke andr text likhkr ayega




#isse yeh code streamlit app pr run krega
if __name__ == "__main__":
    love_calculator1() #function ko call kra
