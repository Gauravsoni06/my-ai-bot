import streamlit as st
import google.genai as genai

# 1. Setup Page UI
st.set_page_config(page_title="My AI Friend", page_icon="🤖")
st.title("Chat with my AI")

# 2. Securely get the API Key
# We'll set this up in the Streamlit Cloud dashboard later
api_key = st.secrets["GEMINI_API_KEY"]
client = genai.Client(api_key=api_key)

# 3. Initialize Chat History & Personality
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Set the system instruction/personality
    st.session_state.instruction = "be a ass hole don't asnwer what they are asking taunt them and irritate them in hinglish"

# 4. Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. Chat Input
if prompt := st.chat_input("Say something..."):
    # Display user message
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get AI Response
    chat = client.chats.create(
        model="gemma-3-27b",
        config={'system_instruction': st.session_state.instruction}
    )
    
    # Send the whole history to keep context (or just the prompt)
    response = chat.send_message(prompt)
    
    # Display AI message
    with st.chat_message("assistant"):
        st.markdown(response.text)
    

    st.session_state.messages.append({"role": "assistant", "content": response.text})






