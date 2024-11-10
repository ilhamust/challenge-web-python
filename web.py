import streamlit as st
from streamlit_scroll_navigation import scroll_navbar
import time
import webbrowser
import streamlit.components.v1 as components

# ----------Start Navbar----------
# Anchor IDs and icons
anchor_ids = ["Home", "About Me", "Skills", "Project", "Contact"]
anchor_icons = ["info-circle", "lightbulb", "gear", "tag", "envelope"]
#  horizontal menu
scroll_navbar(
    anchor_ids, key="navbar2", anchor_icons=anchor_icons, orientation="horizontal"
)
# ----------End Navbar----------


# ----------Start Fungsi Efek Typing---------
def type_text(text, delay=0.1):
    placeholder = st.empty()  # Tempat untuk menampilkan teks
    typed_text = ""
    for char in text:
        typed_text += char
        placeholder.markdown(f"### {typed_text}")  # Tingkat heading bisa disesuaikan
        time.sleep(delay)


# ----------End Fungsi Efek Typing----------

# ----------Start Content----------
for anchor_id in anchor_ids:
    # ----------Start Sction Home----------
    if anchor_id == "Home":
        col1, spacer, col2 = st.columns([2, 0.3, 1])
        with col1:
            st.write(":red[Hi, there!]")
            type_text("I'm Ilham Mustaqim.")
            st.write("Informatic Student and Tech Enthusiast")
            if st.button("Get CV !"):
                webbrowser.open_new_tab(
                    "https://drive.google.com/file/d/154KuuMA8w0mFLQIqsyvuIP-ZvyjnONzz/view?usp=sharing"
                )
        with col2:
            st.image(
                "./assets/poto-profil.png",
                width=200,
            )
        # ----------End Sction Home----------

        # ----------Start Sction About me----------
    elif anchor_id == "About Me":
        st.subheader(anchor_id, anchor=anchor_id)
        st.write(
            "My name is Ilham Mustaqim, a 20-year-old undergraduate student pursuing a degree in Informatics at the Faculty of Information Technology, Nahdlatul Ulama University of Yogyakarta. I have demonstrated strong academic performance by maintaining a GPA of 3.91/4.00 during my second semester. My professional experience includes an internship at CV. Karya Hidup Sentosa, and I have been actively involved in various organizational activities. I am particularly interested in and skilled at problem-solving strategies, administrative tasks, computer programming, and graphic design work."
        )
        # ----------End Sction About me----------

        # ----------Start Sction Skills----------
    elif anchor_id == "Skills":
        st.subheader(anchor_id, anchor=anchor_id)
        st.write("")
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.image("./assets/flutter.png")
            st.image("./assets/js.png")
        with col2:
            st.image("./assets/git.png")
            st.image("./assets/github.png")
        with col3:
            st.image("./assets/mysql.png")
            st.image("./assets/node.png")
        with col4:
            st.image("./assets/laravel.png")
            st.image("./assets/tailwind.png")
        with col5:
            st.image("./assets/node.png")
            st.image("./assets/php.png")
        # ----------End Sction Skills----------

        # ----------Start Sction Project----------
    elif anchor_id == "Project":
        st.subheader(anchor_id, anchor=anchor_id)
        st.write("Here are the best open source projects I've ever worked on:")
        tab1, tab2, tab3, tab4 = st.tabs(
            ["E-Company", "Bookself Apps", "Calculator Web", "Simple Web"]
        )
        with tab1:
            components.iframe(
                "https://alphaomegaid.github.io/",
                width=700,
                height=300,
                scrolling=True,
            )
            with st.expander("Show/Hide", expanded=True):
                st.subheader("SMM Website", divider="red")
                st.markdown(
                    """
                     SSM Website, offers professional social media management services tailored to small and medium businesses. It provides content development, performance analytics, editorial calendars, and targeted social media advertising, helping clients boost their online presence and audience engagement. The site is user-friendly, showcasing its services with a modern design and encouraging businesses to transform their digital strategy.
                    """
                )
                st.link_button(
                    "Go to Source Code",
                    "https://github.com/AlphaOmegaid/AlphaOmegaid.github.io",
                )
        with tab2:
            components.iframe(
                "https://bookself-apps-livid.vercel.app/",
                width=700,
                height=300,
                scrolling=True,
            )
            with st.expander("Show/Hide", expanded=True):
                st.subheader("Bookself Apss", divider="red")
                st.markdown(
                    """
                    The Bookshelf App is a web-based application designed for managing book collections. Users can add books, categorize them as "Read" or "Unread," and search for specific titles. It provides an intuitive interface for organizing reading progress and tracking books effectively. Built as a beginner-friendly project for learning front-end development, the app demonstrates skills in responsive design and user interaction.
                    """
                )
                st.link_button(
                    "Go to Source Code",
                    "https://github.com/ilhamust/bookself-apps",
                )
        with tab3:
            components.iframe(
                "https://web-calcolator.vercel.app/",
                width=700,
                height=300,
                scrolling=True,
            )
            with st.expander("Show/Hide", expanded=True):
                st.subheader("Calculator Web", divider="red")
                st.markdown(
                    """
                    The web calculator project is a user-friendly online tool designed to handle basic arithmetic operations, including addition, subtraction, multiplication, and division. Its straightforward interface enables users to perform calculations quickly and view their history of past calculations for reference.
                    """
                )
                st.link_button(
                    "Go to Source Code",
                    "https://github.com/ilhamust/WebCalcolator",
                )
        with tab4:
            components.iframe(
                "https://ilhamust-github-io-1.vercel.app/",
                width=700,
                height=300,
                scrolling=True,
            )
            with st.expander("Show/Hide", expanded=True):
                st.subheader("Informational Website", divider="red")
                st.markdown(
                    """
                     This project effectively presents the city’s charm and serves as a digital guide to Bandung’s rich culture and history.
                    """
                )
                st.link_button(
                    "Go to Source Code",
                    "https://github.com/ilhamust/ilhamust.github.io-1",
                )
            # ----------End Sction Project----------

    # ----------Start Sction Contact----------
    elif anchor_id == "Contact":
        st.subheader(anchor_id, anchor=anchor_id)
        st.write("Let's connect with me and collaborate :")
        st.link_button(
            "Github",
            "https://github.com/ilhamust",
        )
        st.link_button(
            "LinkedIn",
            "www.linkedin.com/in/ilham-must",
        )
        st.link_button(
            "Instagram",
            "https://instagram.com/_ilhamustaqim",
        )
# ---------End Sction Contact----------

# ----------End Content----------
