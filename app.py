from openai import OpenAI

client = OpenAI()

problem = input("Describe the issue: ")

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {
            "role": "system",
            "content": "You are a troubleshooting assistant for technical equipment. Respond in this format:\nPossible Causes:\n1. ...\n2. ...\n\nRecommended Checks:\n1. ...\n2. ..."
        },
        {
            "role": "user",
            "content": problem
        }
    ]
)

print("\nIssue received:")
print(problem)

print("\nAI Troubleshooting Response:")
print(response.choices[0].message.content)

