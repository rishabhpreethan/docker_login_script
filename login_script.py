import docker
import streamlit as st
from docker.errors import DockerException

def docker_login(username, password):
    try:
        auth_config = {
            'username': username,
            'password': password,
        }

        client = docker.from_env()
        client.login(**auth_config)
        if client.ping():
            return "Logged in"
            # print("Logged in as", username, "to Docker Hub")
        else:
            return "Login failed"
            # print("Login failed")
    except DockerException as e:
        return "An error occured: ",e
        # print(f"An error occurred: {e}")
    except Exception as e:
        return "An unexpected error occured: ", e
        # print(f"An unexpected error occurred: {e}")
        
        
def main():
    st.title("Docker Login")
    st.write("Enter your Docker Hub credentials:")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username and password:
            result = docker_login(username, password)
            st.write(result)
        else:
            st.write("Please enter both username and password.")

if __name__ == "__main__":
    main()