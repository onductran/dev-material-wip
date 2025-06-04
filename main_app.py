import streamlit as st

st.set_page_config(
    page_title="Auth0 Streamlit App",
    layout="centered",
    initial_sidebar_state="auto"
)

def show_authenticated_content():
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
    st.write("This content is only visible to logged-in users.")

    st.sidebar.button("Logout", on_click=st.logout)

# Main app logic
st.sidebar.title("Authentication")

# Check if the user is already logged in
if st.session_state.get("user") and st.session_state["user"].is_logged_in:
    show_authenticated_content()
else:
    st.info("Please log in to access the application.")
    # Show login button, explicitly specifying the provider name from secrets.toml
    if not st.user.is_logged_in:
        st.button("Login with Auth0", on_click=st.login, args=["auth0"])
        st.stop()
    st.title("Welcome to the Public App!")
    st.write("This content is visible to everyone (post-login).")
    st.button("Log out", on_click=st.logout)
st.markdown("---")
st.write("This content is visible to everyone (pre-login).")