# 💬 Chatbot With Conversational Memory

A Python-based conversational chatbot built using **LangChain, OpenAI GPT-4o-mini, and JSON-based persistent storage**.

Unlike a basic chatbot that processes each message independently, this project maintains conversation history and passes previous interactions to the language model to generate context-aware responses. Conversation history is saved to a JSON file, allowing the chatbot to retain context across application restarts.

## 🎯 Project Objectives

The primary objectives of this project are to:

* Build a conversational chatbot using an OpenAI language model.
* Understand how stateless LLM calls can support conversational memory.
* Implement conversation history management using Python.
* Use LangChain's `PromptTemplate` and LCEL pipeline.
* Persist conversation history in a JSON file.
* Understand how previous messages influence LLM responses.
* Practice modular Python programming and file handling.

## ✨ Features

* **Context-aware conversations:** Uses previous messages to generate relevant responses.
* **Conversation history:** Maintains user and assistant messages in a Python list.
* **Persistent memory:** Saves conversation history to `memory.json`.
* **Memory restoration:** Loads previously saved conversations when the application starts.
* **LangChain integration:** Uses `PromptTemplate` and LangChain Expression Language (LCEL).
* **Configurable LLM:** Uses OpenAI's `gpt-4o-mini` model.
* **Environment variable management:** Loads API credentials from a `.env` file.
* **Interactive CLI:** Allows users to chat directly through the terminal.
* **Graceful exit:** Supports `exit` and `quit` commands.

## 🛠️ Technology Stack

| Technology         | Purpose                                          |
| ------------------ | ------------------------------------------------ |
| Python             | Core programming language                        |
| OpenAI GPT-4o-mini | Generates conversational responses               |
| LangChain          | Connects prompts and the language model          |
| `langchain-openai` | Integrates OpenAI chat models with LangChain     |
| `langchain-core`   | Provides `PromptTemplate` and LCEL functionality |
| python-dotenv      | Loads environment variables from `.env`          |
| JSON               | Stores conversation history persistently         |

## 🏗️ Project Architecture

The application follows a simple, modular architecture.

```text
User Input
    |
    v
main()
    |
    v
Load Existing Conversation
(load_memory)
    |
    v
Format Conversation History
(format_memory)
    |
    v
Construct Prompt
(PromptTemplate)
    |
    v
LangChain LCEL Pipeline
(prompt | llm)
    |
    v
OpenAI GPT-4o-mini
    |
    v
Generate Context-Aware Response
(generate_response)
    |
    v
Display Response
    |
    v
Update Conversation History
    |
    v
Save to memory.json
(save_memory)
```

### Conversation Flow

Each interaction follows these steps:

1. The application loads existing conversation history from `memory.json`.
2. The user enters a new message.
3. The existing conversation history is formatted into readable text.
4. A `PromptTemplate` combines the history with the current user input.
5. The LCEL pipeline sends the prompt to the OpenAI model.
6. The model generates a response using the supplied context.
7. The user message and assistant response are appended to the conversation history.
8. The updated conversation history is saved to `memory.json`.

**Important:** The language model does not automatically remember previous API calls. The application provides conversational context by including the relevant history in each prompt.

## 📂 Project Structure

```text
Chatbot-With-Memory/
│
├── chatbot.py             # Main chatbot application
├── memory.json         # Persistent conversation history
├── .env                # OpenAI API key (not committed to Git)
├── .gitignore          # Files excluded from Git tracking
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

`memory.json` is created automatically when the first successful conversation is saved. The `.env` file must be created locally and should not be committed to the repository.

## ⚙️ Prerequisites

Before running the application, ensure you have:

* Python 3.10 or later.
* An OpenAI API key.
* An active internet connection.
* A code editor such as Visual Studio Code.
* Basic knowledge of Python and command-line execution.

You must also have API access to the selected OpenAI model. API usage may incur charges depending on your account and usage.

## 🚀 Installation and Setup

### Step 1: Clone the Repository

```bash
git clone <your-github-repository-url>
```

Navigate to the project directory:

```bash
cd Chatbot-With-Memory
```

Replace `<your-github-repository-url>` with your actual repository URL.

### Step 2: Create a Virtual Environment

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Alternatively, activate it using Command Prompt:

```cmd
.venv\Scripts\activate.bat
```

### Step 3: Install Dependencies

Install the required Python packages:

```bash
pip install langchain langchain-openai langchain-core python-dotenv
```

Alternatively, if you have a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### Step 4: Configure the OpenAI API Key

Create a `.env` file in the project root directory.

Add the following configuration:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

Replace the placeholder with your actual API key.

**Security reminder:** Never publish your API key, commit the `.env` file, or hardcode credentials in your Python source code.

### Step 5: Create the `.gitignore` File

Add the following entries to `.gitignore`:

```gitignore
# Environment variables and secrets
.env
.env.*

# Python virtual environment
.venv/
venv/

# Python cache
__pycache__/
*.py[cod]

# Jupyter Notebook checkpoints
.ipynb_checkpoints/

# Local conversation history
memory.json
```

Ignoring `memory.json` prevents personal conversation history from being committed to Git.

If you intentionally want to distribute a sample conversation file, use a separate sanitized example such as `memory.example.json`.

## ▶️ Running the Application

Run the application from the project directory:

```bash
python main.py
```

Expected startup message:

```text
Simple chat. Type 'exit' to quit.
You:
```

Enter a message to begin the conversation.

## 💬 Example Conversation

### First Interaction

```text
You: My name is Rajanna and my favorite sport is cricket.

Bot: Nice to meet you, Rajanna! Cricket is a great sport.
```

### Context-Aware Follow-Up

```text
You: What is my favorite sport?

Bot: Your favorite sport is cricket.
```

The chatbot can answer the follow-up because the previous conversation is included in the prompt.

### Exit the Application

```text
You: exit

Chat ended.
```

The conversation history remains stored in `memory.json`.

### Test Persistent Memory

1. Start the application.
2. Tell the chatbot your name and favorite sport.
3. Exit the application.
4. Run `python main.py` again.
5. Ask the chatbot to recall your name and favorite sport.

The chatbot should be able to answer because the application reloads the saved conversation history.

## 🧩 Core Functions Explained

### 1. `load_memory()`

**Purpose:** Loads the existing conversation history from `memory.json`.

* Checks whether the file exists.
* Reads and parses JSON data.
* Returns an empty list when no history file exists.
* Handles common file-reading and JSON-decoding errors.

### 2. `save_memory(memory)`

**Purpose:** Persists the conversation history.

* Accepts a list of conversation dictionaries.
* Serializes the list into JSON.
* Writes the updated history to `memory.json`.

Example memory structure:

```json
[
  {
    "role": "user",
    "text": "My favorite sport is cricket."
  },
  {
    "role": "assistant",
    "text": "That's great! Cricket is a popular sport."
  }
]
```

### 3. `format_memory(memory)`

**Purpose:** Converts structured conversation data into a readable transcript.

Example:

```text
User: My favorite sport is cricket.
Assistant: That's great! Cricket is a popular sport.
```

This formatted text is passed to the LLM through the prompt template.

### 4. `generate_response(user_input, memory)`

**Purpose:** Generates a response based on the conversation history and current user input.

The function:

1. Formats the previous conversation.
2. Creates a prompt using `PromptTemplate`.
3. Connects the prompt to the LLM using LCEL.
4. Invokes the model.
5. Returns the generated response as a string.

The LCEL pipeline is:

```python
chain = prompt | llm
```

The model is invoked using:

```python
result = chain.invoke({
    "history": history,
    "user_input": user_input
})
```

The assistant's text is extracted using:

```python
return result.content
```

### 5. `chatbot()`
  
**Purpose:** Controls the application's main execution loop.

* Loads the saved conversation.
* Accepts user input.
* Handles exit commands.
* Calls `generate_response()`.
* Displays the response.
* Updates the conversation history.
* Saves the updated history.

## 🧠 Concepts Demonstrated

This project provides hands-on practice with the following concepts:

| Concept               | What You Learn                                              |
| --------------------- | ----------------------------------------------------------- |
| Stateless LLM calls   | Why previous context must be supplied to the model          |
| Prompt engineering    | How to structure instructions and conversation history      |
| `PromptTemplate`      | How to define reusable prompts with input variables         |
| LCEL                  | How to compose LangChain components using the pipe operator |
| Conversation memory   | How to manage messages across multiple turns                |
| JSON serialization    | How to convert Python objects into persistent JSON data     |
| Environment variables | How to manage API credentials securely                      |
| Python functions      | How to organize application logic into reusable components  |
| Exception handling    | How to handle common file and runtime failures              |

## ⚠️ Limitations

This project is designed as a learning project and a basic local chatbot.

Current limitations include:

* **Growing context:** The entire conversation history is included in each prompt, increasing token usage as the conversation grows.
* **JSON storage:** JSON is suitable for a simple local application but is not ideal for concurrent writes or multiple users.
* **No user isolation:** All interactions use the same local memory file.
* **No summarization:** Old messages are not automatically summarized.
* **No graphical interface:** The application runs in the terminal.
* **No authentication:** The application does not implement user login or access controls.
* **Model dependency:** Successful execution depends on API credentials, network availability, model availability, and account access.

## 🔮 Future Enhancements

Possible improvements include:

* Implement a sliding window to limit conversation history.
* Add conversation summarization for long-running chats.
* Store conversations in SQLite or PostgreSQL.
* Add user-specific memory.
* Build a Streamlit chat interface.
* Create a FastAPI backend.
* Add automated tests using `pytest`.
* Implement structured logging and improved error handling.
* Add conversation export and deletion features.
* Deploy the chatbot to a cloud platform.

## 🧪 Troubleshooting

### 1. `openai.AuthenticationError`

**Possible cause:** The API key is missing or invalid.

**Solution:** Verify the `OPENAI_API_KEY` value in your `.env` file and ensure the environment variables are loaded.

### 2. `model_not_found` or HTTP 404

**Possible cause:** The selected model is unavailable to the API project, or the model identifier is incorrect.

**Solution:** Verify the model identifier and confirm model access for the API project associated with your key.

### 3. `ModuleNotFoundError`

**Possible cause:** Required dependencies are not installed in the active Python environment.

**Solution:**

```bash
pip install langchain langchain-openai langchain-core python-dotenv
```

### 4. `JSONDecodeError`

**Possible cause:** The existing `memory.json` file contains invalid JSON.

**Solution:** Inspect the file and restore valid JSON. If the conversation history is disposable, back up the file before replacing it with an empty JSON list:

```json
[]
```

### 5. The chatbot does not remember earlier messages

**Possible causes:**

* The history is not being formatted or passed into the prompt.
* The conversation history is not being saved.
* The application is running from a different working directory.
* The saved JSON file contains unexpected data.

**Solution:** Verify that `load_memory()`, `format_memory()`, and `save_memory()` are working correctly.

## 🔐 Security Considerations

* Keep API credentials in environment variables.
* Never commit `.env` files or API keys to GitHub.
* Add `memory.json` to `.gitignore` if it contains personal or sensitive conversations.
* Avoid sharing real user conversations in public repositories.
* For production deployments, use appropriate secret management, access controls, and database security.

## 📚 Learning Outcomes

By completing this project, you will understand how to:

* Integrate an OpenAI chat model with LangChain.
* Build an LCEL processing pipeline.
* Construct prompts using conversation history.
* Implement basic conversational memory.
* Persist application state using JSON.
* Manage environment variables and API credentials.
* Design a modular Python application.

## 👨‍💻 Author

AV RAJANNA

Add your GitHub profile or LinkedIn profile here.

## 📄 License

This project is intended for educational and learning purposes.

If you plan to publish it as an open-source project, consider adding an appropriate license, such as the MIT License.

````

---

## 2. Create your `requirements.txt`

For this project, create a file named `requirements.txt` containing:

```text
langchain
langchain-openai
langchain-core
python-dotenv
````

Install the packages using:

```bash
pip install -r requirements.txt
```

For reproducible installations, you can later pin the tested package versions.

## 3. Before pushing to GitHub

From your project directory, execute:

```bash
git status
```

Verify that `.env` and `memory.json` are not staged or tracked.

If both are untracked and correctly excluded by `.gitignore`, stage your project files:

```bash
git add main.py README.md requirements.txt .gitignore
```

Then commit and push:

```bash
git commit -m "Add chatbot with conversational memory"
git push origin main
```

**Important:** If `.env` or `memory.json` was already committed in an earlier commit, adding it to `.gitignore` alone does not remove it from Git tracking. Remove it from tracking and rotate any exposed API key.

### Final recommendation

Your project is a useful foundation for understanding conversational memory, prompt engineering, and LangChain LCEL. Once the basic implementation works, adding **conversation summarization, a Streamlit interface, and database-backed memory** would make it a stronger portfolio project for AI Engineer roles.