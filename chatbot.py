import json
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

# Read the .env file and load environment variables
load_dotenv()

MEMORY_FILE = "memory.json"

# Temperature = 0.7 => natural and conversational responses
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7
)


def load_memory():
    """Load conversation history from memory.json."""
    if os.path.exists(MEMORY_FILE):
        try:
            with open(MEMORY_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError) as e:
            print(f"Warning: Could not load memory: {e}")
            return []

    return []


def save_memory(memory):
    """Save conversation history to memory.json."""
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=2, ensure_ascii=False)


def format_memory(memory: list) -> str:
    """Convert conversation history into a readable transcript."""
    lines = []

    for msg in memory:
        speaker = msg["role"].capitalize()
        text = msg["text"]
        lines.append(f"{speaker}: {text}")

    return "\n".join(lines)


def generate_response(user_input: str, memory: list) -> str:
    """Generate a response using the previous conversation history."""

    # Format existing conversation history.
    history = format_memory(memory)

    # Create a prompt with two variables: history and user_input.
    prompt = PromptTemplate.from_template(
        """You are a helpful assistant. Use the conversation history
to stay consistent and remember details the user told you earlier.

Conversation so far:
{history}

User: {user_input}
Assistant:"""
    )

    # LCEL: fill the template and send it to the model.
    chain = prompt | llm

    result = chain.invoke({
        "history": history,
        "user_input": user_input
    })

    # Return the response as plain text.
    return result.content


def main():
    memory = load_memory()

    print("Simple chat. Type 'exit' to quit.")

    while True:
        user = input("You: ")

        if user.strip().lower() in ("exit", "quit"):
            print("Chat ended.")
            break

        if not user.strip():
            continue

        try:
            # Generate the response using previous conversation history.
            reply = generate_response(user, memory)

            print("Bot:", reply)

            # Append both messages after the response is generated.
            memory.append({"role": "user", "text": user})
            memory.append({"role": "assistant", "text": reply})

            # Persist the conversation.
            save_memory(memory)

        except Exception as e:
            print(f"Error generating response: {e}")
            print("Please try again.")

if __name__ == "__main__":
    main()