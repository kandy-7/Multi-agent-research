from src.tools.groq_client import client
from src.prompts.planner_prompt import PLANNER_PROMPT
def planner_agent(topic):
    response = client.chat.completions.create(model="llama-3.3-70b-versatile",
                                              messages=[{
 "role":"system",
 "content": PLANNER_PROMPT
},{
 "role":"user",
 "content": topic
}])
    return response.choices[0].message.content