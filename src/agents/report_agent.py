from src.tools.groq_client import client
from src.prompts.report_prompt import REPORT_PROMPT


def report_agent(research_notes):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": REPORT_PROMPT
            },
            {
                "role": "user",
                "content": research_notes
            }
        ]
    )

    return response.choices[0].message.content