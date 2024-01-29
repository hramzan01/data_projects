import streamlit as st 
import subprocess
from streamlit_option_menu import option_menu

# Set page configuration to wide mode
st.set_page_config(layout="wide")

# 1. Set Home Nav Bar
selected = option_menu(
    
    # Configuration
    menu_title='', # req
    options=['About Me','Projects','Contact'], # req
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
if selected == 'Home':
    st.title(f'Project Zero')

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
    # Set Project Zero
    if project == 'City Plan':
        st.title('You selected City Plan')
        'some text about seleting project zero, a project '

    if project == 'Market':
        st.title('You selected Marktet')


    