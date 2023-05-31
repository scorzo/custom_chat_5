import openai

# Set up your OpenAI API credentials
openai.api_key = ''

# Define your initial prompt (paragraph-long)
prompt = """


Session Start:
"""
#engine="text-davinci-003",
# Start the session
session_prompt = prompt
response = openai.Completion.create(
    engine="text-davinci-003",
    #engine="ada",
    prompt=session_prompt,
    max_tokens=100  # Adjust the desired length of the response
)

# Function to append user question and generate AI response
def generate_response(question, session_prompt):
    # Append user question to the session prompt
    session_prompt += "\nUser: " + question
    #engine="text-davinci-003",
    response = openai.Completion.create(
        #engine="ada",
        engine="text-davinci-003",
        prompt=session_prompt,
        max_tokens=100  # Adjust the desired length of the response
    )
    # Extract the generated answer
    answer = response.choices[0].text.strip()
    # Append user question and AI response to the session prompt
    session_prompt += "\nAI: " + answer
    return answer, session_prompt

# Example conversation loop
while True:
    # Get user input
    user_input = input("User: ")
    # Check for exit condition
    if user_input.lower() in ['exit', 'quit']:
        break
    # Generate AI response
    ai_answer, session_prompt = generate_response(user_input, session_prompt)
    # Print AI response
    print("AI:", ai_answer)
