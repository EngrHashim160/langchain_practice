from langchain_groq import ChatGroq
from typing import TypedDict
from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(model="mixtral-8x7b-32768")

# schema

class review(TypedDict):
    summary: str
    sentiment: str


structured_model = llm.with_structured_output(review)

result = structured_model.invoke("""
        I've been using the SmartFit Pro for two weeks now, and overall, it's a great smartwatch! The battery life is impressive, lasting almost five days on a single charge. The display is bright and easy to read, even in sunlight. However, the heart rate monitor sometimes gives inaccurate readings, which can be frustrating during workouts. Also, the app sync is a bit slow at times. Despite these minor issues, it's a solid choice for fitness tracking and notifications. Would recommend!
""")

print(result)
print(f"\nSummary: {result['summary']}")
print(f"\nSentiment: {result['sentiment']}")
