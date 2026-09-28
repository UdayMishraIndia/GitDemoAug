from google import genai

# py -m pip install google-genai - execute this in the termial to install the google-genai package

api_key = "API-KEY"  # Replace with your actual API key

client = genai.Client(api_key=api_key)

# Function to call the Gemini API with a given prompt
def call_gemini_api(prompt):
    # Create a chat session with the Gemini API
    chat = client.chats.create(
        model="gemini-3.8-flash")

    # Send a message to the chat session and get the response
    response = chat.send_message(prompt)
    return response.text

def process_text(text):
    prompt = f"Give me the output in 3 bullet points {text}"
    return call_gemini_api(prompt)

user_input = input("What you want to know about: ")
processed_content = process_text(user_input)
print("Processed Content:\n", processed_content)


