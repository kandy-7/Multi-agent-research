from src.tools.groq_client import client
from src.prompts.summary_prompt import SUMMARY_PROMPT


def summary_agent(content):

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": SUMMARY_PROMPT
            },
            {
                "role": "user",
                "content": content
            }
        ]
    )

    return response.choices[0].message.content