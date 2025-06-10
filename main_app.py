import streamlit as st
from data_editor import load_data, display_data

st.set_page_config(
    page_title="Auth0 Streamlit App",
    layout="centered",
    initial_sidebar_state="auto"
)

# # --- Functions to display different sections of the app ---

def show_authenticated_content():
    """Displays content visible only to logged-in users."""
    st.title("Welcome to the Authenticated App!")
    # st.write(f"Hello, **{st.user.name}**!") # Access user's name from Auth0
    # st.write(f"Your email: `{st.user.email}`") # Access user's email

    st.markdown("---")
    st.header("Data Editor")
    data = load_data("./1. APP PLACEMENTS - TEXTILE.xlsx")  # Load sample data
    edited_data = display_data(data)  # Display the data editor
    st.dataframe(edited_data, use_container_width=True)  # Show the edited data
    st.markdown("---")

#     # Logout button for authenticated users
#     st.sidebar.button("Logout", on_click=st.logout)

# def show_public_content():
#     """Displays content visible to all users (before login)."""
#     st.title("Welcome to the Public App!")
#     st.info("Please log in to access the full application features.")

#     # Login button for unauthenticated users
#     # When this button is clicked, st.login() is called, which initiates the redirect.
#     # st.stop() is crucial here to prevent the rest of the script from running
#     # until the user returns from the Auth0 login page.
#     if st.button("Login with Auth0"):
#         st.login("auth0") # "auth0" matches the provider name in your secrets.toml
#         st.stop() # Stop script execution and redirect

#     st.markdown("---")
#     st.write("This content is visible to everyone.")


# # --- Main Application Logic ---

# st.sidebar.title("Authentication Status")

# # Check if the user is currently logged in
# # st.session_state["user"] is populated by Streamlit's OIDC mechanism
# # st.user.is_logged_in is the primary way to check the login status
# if st.user.is_logged_in:
#     # If authenticated, show the content for logged-in users
#     show_authenticated_content()
# else:
#     # If not authenticated, show the public content and login prompt
#     show_public_content()

show_authenticated_content()