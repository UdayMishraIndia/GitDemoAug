from openai import OpenAI

api_key = "api-key"

client = OpenAI(api_key=api_key)

# Function to call the OpenAI API with a given prompt
def call_openai_api(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

def process_text(text):
    prompt = f"Give me the output in 3 bullet points {text}"
    return call_openai_api(prompt)

#with open("input.txt", "r") as file:
#    content = file.read()
#    processed_content = process_text(content)
#    print("Processed Content:\n", processed_content)

user_input = input("What you want to know about: ")
processed_content = process_text(user_input)
