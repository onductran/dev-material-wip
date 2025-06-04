import streamlit as st

st.set_page_config(
    page_title="Auth0 Streamlit App",
    layout="centered",
    initial_sidebar_state="auto"
)

# --- Functions to display different sections of the app ---

def show_authenticated_content():
    """Displays content visible only to logged-in users."""
    st.title("Welcome to the Authenticated App!")
    st.write(f"Hello, **{st.user.name}**!") # Access user's name from Auth0
    st.write(f"Your email: `{st.user.email}`") # Access user's email

    # You can access other claims from the OIDC token if configured in Auth0
    # For example, if you add custom claims or roles to your Auth0 tokens,
    # you can often access them like:
    # st.write(f"Your role: {st.user.get('https://your-namespace/role', 'N/A')}")
    # Note: Custom claims require configuration in Auth0 Rules/Actions to be included in the ID token.

    st.subheader("Raw User Info:")
    st.json(st.user) # Displays all available user information from Auth0

    st.markdown("---")
    st.write("This is the main content of your application, only visible to logged-in users.")

    # Logout button for authenticated users
    st.sidebar.button("Logout", on_click=st.logout)

def show_public_content():
    """Displays content visible to all users (before login)."""
    st.title("Welcome to the Public App!")
    st.info("Please log in to access the full application features.")

    # Login button for unauthenticated users
    # When this button is clicked, st.login() is called, which initiates the redirect.
    # st.stop() is crucial here to prevent the rest of the script from running
    # until the user returns from the Auth0 login page.
    if st.button("Login with Auth0"):
        st.login("auth0") # "auth0" matches the provider name in your secrets.toml
        st.stop() # Stop script execution and redirect

    st.markdown("---")
    st.write("This content is visible to everyone.")


# --- Main Application Logic ---

st.sidebar.title("Authentication Status")

# Check if the user is currently logged in
# st.session_state["user"] is populated by Streamlit's OIDC mechanism
# st.user.is_logged_in is the primary way to check the login status
if st.user.is_logged_in:
    # If authenticated, show the content for logged-in users
    show_authenticated_content()
else:
    # If not authenticated, show the public content and login prompt
    show_public_content()