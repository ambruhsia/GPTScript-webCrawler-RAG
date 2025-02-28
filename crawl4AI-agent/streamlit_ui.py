from __future__ import annotations
from typing import Literal, TypedDict
import asyncio
import os

import streamlit as st
import json
import logfire
from supabase import Client
from openai import AsyncOpenAI

# Import all the message part classes
from pydantic_ai.messages import (
    ModelMessage,
    ModelRequest,
    ModelResponse,
    SystemPromptPart,
    UserPromptPart,
    TextPart,
    ToolCallPart,
    ToolReturnPart,
    RetryPromptPart,
    ModelMessagesTypeAdapter
)
from pydantic_ai_expert import pydantic_ai_expert, PydanticAIDeps

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

openai_client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
supabase: Client = Client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_SERVICE_KEY")
)

# Configure logfire to suppress warnings (optional)
logfire.configure(send_to_logfire='never')

# Streamlit Page Config with Custom Theme
st.set_page_config(
    page_title="GPTScript Doc Crawler & RAG",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styles
st.markdown(
    """
    <style>
        body {
            background-color: #1e1e2e;
            color: #ffffff;
        }
        .stApp {
            background-color: #1e1e2e;
        }
        .stButton>button {
            background-color: #7D0FBE;
            color: white;
            border-radius: 10px;
            font-size: 16px;
        }
        .stChatMessage {
            border-radius: 10px;
            padding: 10px;
        }
        .stChatMessage.user {
            background-color: #D7263D;
            color: white;
        }
        .stChatMessage.assistant {
            background-color: #5A189A;
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)

class ChatMessage(TypedDict):
    """Format of messages sent to the browser/API."""
    role: Literal['user', 'model']
    timestamp: str
    content: str

def display_message_part(part):
    """
    Display a single part of a message in the Streamlit UI.
    """
    if part.part_kind == 'system-prompt':
        with st.chat_message("system"):
            st.markdown(f"**System**: {part.content}")
    elif part.part_kind == 'user-prompt':
        with st.chat_message("user"):
            st.markdown(part.content)
    elif part.part_kind == 'text':
        with st.chat_message("assistant"):
            st.markdown(part.content)          

async def run_agent_with_streaming(user_input: str):
    """
    Run the agent with streaming text for the user_input prompt.
    """
    deps = PydanticAIDeps(
        supabase=supabase,
        openai_client=openai_client
    )

    async with pydantic_ai_expert.run_stream(
        user_input,
        deps=deps,
        message_history=st.session_state.messages[:-1],
    ) as result:
        partial_text = ""
        message_placeholder = st.empty()

        async for chunk in result.stream_text(delta=True):
            partial_text += chunk
            message_placeholder.markdown(partial_text)

        filtered_messages = [msg for msg in result.new_messages() 
                             if not (hasattr(msg, 'parts') and 
                                     any(part.part_kind == 'user-prompt' for part in msg.parts))]
        st.session_state.messages.extend(filtered_messages)
        
        st.session_state.messages.append(
            ModelResponse(parts=[TextPart(content=partial_text)])
        )

async def main():
    st.title("📄 GPTScript Documentation Crawler & RAG Agent")
    st.write("Explore and query documentation with AI-powered retrieval and intelligent answers.")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        if isinstance(msg, ModelRequest) or isinstance(msg, ModelResponse):
            for part in msg.parts:
                display_message_part(part)

    user_input = st.chat_input("Ask a question about GPTScript documentation...")

    if user_input:
        st.session_state.messages.append(
            ModelRequest(parts=[UserPromptPart(content=user_input)])
        )
        
        with st.chat_message("user"):
            st.markdown(user_input)

        with st.chat_message("assistant"):
            await run_agent_with_streaming(user_input)

if __name__ == "__main__":
    asyncio.run(main())
