import openai

# Set your API key
openai.api_key = ""


prompt = "Hello, my name is"
response = openai.Completion.create(
    engine="ada",
    prompt=prompt,
    max_tokens=10,
    n=1,
    stop=None,
    temperature=0.5,
)

# Print the response
print(response.choices[0].text.strip())
