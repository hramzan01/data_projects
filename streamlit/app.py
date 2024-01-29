import streamlit as st
import subprocess
from streamlit_option_menu import option_menu

# Set page configuration to wide mode
st.set_page_config(layout="wide")

# 1. Set Home Nav Bar
selected = option_menu(

    # Configuration
    menu_title='', # req
    options=['About','Projects','Contact'], # req
    icons=['house','file-code-fill','chat-dots-fill'], #opt
    # menu_icon='cast', #opt
    default_index=0, #opt
    orientation='horizontal',

    #Styles
    styles={
                "container": {"padding": "0!important", "background-color": "transparent"},
                # "icon": {"color": "orange", "font-size": "25px"},
                "nav-link": {
                #     "font-size": "25px",
                #     "text-align": "left",
                #     "margin": "0px",
                      "--hover-color": "grey",
                },
                "nav-item":{
                    "--hover-color": "grey",
                },
                "nav-link-selected": {"background-color": "transparent"},
                "nav-link:hover": {
                    "color": "grey",  # Font color when hovering
                },
            },

    )

# 2. Set Home
if selected == 'About':
    st.markdown("""
    <div style="padding: 40px 180px;">
        <h1 style="padding-bottom: 20px;">About Me</h1>
        Architect and data specialist leveraging project data to deliver high quality, cost-effective, and sustainable design.
        From the decarbonisation of modern housing to monitoring the big data requirements of future cities across the world.
        - Deep understanding of both architectural and digital languages
        - Experienced in presenting complex ideas in a clear and understandable way
        - Highly organized professional with an ability to innovate, strategize and deliver excellence.
    </div>
    """, unsafe_allow_html=True)

# 3. Set Contact
if selected == 'Contact':
    contact = option_menu(

    menu_title='', # req
    options=['', '', ''], # req
    icons=['github' ,'linkedin', 'medium'], #opt
    orientation='horizontal', #opt
    styles={
                "container": {"padding": "0!important", "background-color": "transparent"},
                "nav-link-selected": {"background-color": "transparent"}
            },
)

# Set Projects
if selected == 'Projects':
    project = option_menu(

    menu_title='', # req
    options=[' ', 'City Plan','Market'], # req
    icons=[None ,'buildings','lightning'], #opt
    orientation='horizontal', #opt
    styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "nav-link-selected": {"background-color": "transparent"}

        },
    )

    # Custom padding for the "Projects" section

    # Set Project Zero
    if project == 'City Plan':
        st.markdown("""
        <div class="projects-container" style="padding: 40px 180px;">
            <h1 style="padding-bottom: 20px;">City Plan Project</h1>
            Here is a generic description about the project where the business
            problems are as follows. While working as an architect.
        </div>
        """, unsafe_allow_html=True)

    if project == 'Market':
        st.markdown("""
        <div class="projects-container" style="padding: 40px 180px;">
            <h1 style="padding-bottom: 20px;">Market Project</h1>
            Here is a a slightly different description about the project where the business
            problems are as follows. While working as an architect.
        </div>
        """, unsafe_allow_html=True)
