🧠 Multi-Agent Assistant (with Handoffs)

This project demonstrates how to build an intelligent multi-agent system using the agents framework.
The setup includes agents that can calculate, translate to Chinese, and act as a main assistant capable of delegating (handoffing) tasks to the right specialized agent.

🚀 Features

🤖 Assistant Agent – Acts as the main interface. It listens to user requests and decides whether to answer directly or hand off to a more suitable agent.

🧮 Calculator Agent – Handles all types of arithmetic calculations.

🇨🇳 Chinese Agent – Translates any text into natural and fluent Chinese.

🔁 Handoff Mechanism – Automatically transfers a request to the correct agent when needed.

🏗️ Project Structure
.
├── main.py              # Your main Python script
├── .env                 # Stores GEMINI_API_KEY and BASE_URL
└── README.md            # Documentation file (this file)

⚙️ Environment Setup

Clone or download this repository.

Create a .env file in the root directory and add your API credentials:

GEMINI_API_KEY=your_api_key_here
BASE_URL=https://your_base_url_here


Install dependencies:

pip install python-dotenv rich httpx agents

🧩 How It Works

The script loads environment variables and initializes a Gemini client using the provided API key.

Three agents are created:

calculate → performs calculations.

chines → translates to Chinese.

coach → acts as a main assistant and can hand off tasks to either of the above agents.

The Runner.run_sync() function executes the main coach agent with a prompt.

If the query involves math, coach hands it off to calculate.
If it’s about translation, it hands off to chines.

🧠 Example Usage
result = Runner.run_sync(coach, "what is 37 + 32 = ?")
print(result.final_output)


Output:

69

🧰 Dependencies

agents

httpx

rich

python-dotenv

🧾 License

This project is free to use for educational and experimental purposes.