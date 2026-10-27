from datetime import datetime
import requests


class Chatbot:
    def __init__(self):
        self.url = "http://localhost:11434/api/chat"
        self.model = "qwen2.5:1.5b"
        self.messages = []

        
    def get_ai_response(self):
        today = datetime.now().astimezone().strftime("%A, %d %B %Y")

        system_message = {
            "role": "system",
            
            "content": (
                f"Today's date is {today}. "
                "You are a friendly AI assistant and beginner-friendly Python tutor. "
                "Explain technical topics in simple English. "
                "Give small, clear examples when helpful. "
                "When teaching coding, explain step by step. "
                "If you do not know an answer, say so instead of guessing. "
                "Use the provided date when answering questions about today, "
                "tomorrow, or yesterday. "
                "Do not invent a different current date."
            )

        }

        data = {
            "model": self.model,
            "messages": [system_message] + self.messages,
            "stream": False
        }

        try:
            response = requests.post(
                self.url,
                json=data,
                timeout=120
            )
            response.raise_for_status()

            result = response.json()
            return result["message"]["content"]

        except requests.exceptions.ConnectionError:
            return "ERROR: Could not connect to Ollama."

        except requests.exceptions.Timeout:
            return "ERROR: The request took too long."

        except requests.exceptions.RequestException:
            return "ERROR: A request error occurred."

        except (ValueError, KeyError, TypeError):
            return "ERROR: Could not read the AI response."

    def start_chat(self):
        print("==============================")
        print("       MY AI CHATBOT")
        print("==============================")
        print("Type 'exit' to stop chatting.\n")

        while True:
            question = input("You: ").strip()

            if question.lower() == "exit":
                print("AI: Goodbye! Have a nice day.")
                break

            if not question:
                print("AI: Please enter a question.\n")
                continue

            self.messages.append({
                "role": "user",
                "content": question
            })

            answer = self.get_ai_response()

            if answer.startswith("ERROR:"):
                self.messages.pop()
                print("AI:", answer, "\n")
                continue

            print("\nAI:", answer, "\n")

            self.messages.append({
                "role": "assistant",
                "content": answer
            })


# Create a chatbot object and start chatting
my_chatbot = Chatbot()
my_chatbot.start_chat()
