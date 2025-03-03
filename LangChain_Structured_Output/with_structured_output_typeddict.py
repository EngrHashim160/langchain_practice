from langchain_groq import ChatGroq
from typing import TypedDict, Annotated, Literal, Optional
from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(model="mixtral-8x7b-32768")

# schema

class review(TypedDict):
    name_of_item: Annotated[str, "About which item the review is?"]
    key_themes: Annotated[list[str], "Write down all the key themes discussed in the review."]
    summary: Annotated[str, 'Write a brief summary of the review.']
    sentiment: Annotated[Literal["pos", "neg", "neu"], 'Is the review postive, negative or neutral?']
    pros: Annotated[Optional[list[str]], "Pros of the items given in the review in list format."]
    cons: Annotated[Optional[list[str]], "Cons of the items given in the review in list format."]
    # rating: Annotated[Optional[float], 'What rating does the user give to the specified item in the review?']
    rating: Annotated[Optional[str], 'What rating does the user give to the specified item in the review?']
    reviewer_name: Annotated[str, 'What is the name of the reviewer?']




structured_model = llm.with_structured_output(review)

result = structured_model.invoke("""
        User Review: Samsung Galaxy S24 Ultra
I recently upgraded to the Samsung Galaxy S24 Ultra, and after a few weeks of use, I can confidently say it's one of the most feature-packed and powerful smartphones on the market. Samsung has truly pushed the boundaries with hardware, AI capabilities, and camera technology in this iteration.

Performance & Battery Life
The Snapdragon 8 Gen 3 processor delivers blazing-fast performance, whether I'm gaming, multitasking, or editing videos. Apps load instantly, and even the most demanding games run smoothly at max settings. The 12GB RAM makes multitasking seamless, allowing me to switch between heavy applications without lag.

Battery life is exceptional—the 5000mAh battery comfortably lasts a full day, even with intensive usage. 45W fast charging is a lifesaver, juicing up the phone to 50% in about 30 minutes. However, I wish Samsung included a charger in the box.

Display & S-Pen
The 6.8-inch QHD+ Dynamic AMOLED 2X display is simply breathtaking. Colors are rich, blacks are deep, and the 120Hz adaptive refresh rate makes everything buttery smooth. Whether I'm streaming HDR content, gaming, or reading in bright sunlight, the display never fails to impress.

The S-Pen integration is a fantastic touch, especially for productivity and note-taking. Handwriting recognition is surprisingly accurate, and the air gestures add extra functionality. However, I don't use it often enough to justify it being a major selling point.

Camera System
Samsung has taken smartphone photography to a whole new level with its quad-camera setup. The 200MP primary sensor captures stunningly detailed photos, even when cropping in. Night mode performance is exceptional, producing vibrant and well-lit images even in near darkness.

The periscope zoom lens is a game-changer—10x optical zoom is super sharp, and even at 30x digital zoom, images remain usable. Beyond 50x, the quality starts to degrade, but it's still impressive for a smartphone. The selfie camera is also excellent, delivering sharp and natural skin tones.

Software & AI Features
Samsung's One UI 6.1 is polished and feature-rich, though it still comes with a bit of bloatware. The new AI-driven features are impressive, particularly photo remastering, AI-generated wallpapers, and live translation during calls.

However, I find Samsung’s push for its own ecosystem a bit frustrating—why do I need multiple Samsung apps when I already use Google's services?

Build Quality & Ergonomics
The titanium frame gives the phone a premium feel, and Gorilla Glass Victus 2 ensures durability. However, the size and weight make it less comfortable for one-handed use. At 233g, it’s definitely on the heavier side.

Price & Value
At $1,299, the S24 Ultra is undeniably expensive. While it offers best-in-class performance, a cutting-edge camera system, and long software support, the price tag is a hard pill to swallow, especially when competitors offer similar features for less.

Pros & Cons
✅ Pros:
Insanely powerful Snapdragon 8 Gen 3 processor (great for gaming and multitasking)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen adds unique productivity features
Bright and vibrant 6.8-inch AMOLED display
AI-powered features improve user experience
❌ Cons:
Bulky and heavy—not ideal for one-handed use
Samsung’s One UI still comes with unnecessary bloatware
Lacks a charger in the box
Very expensive compared to competitors
Final Verdict
The Samsung Galaxy S24 Ultra is a powerhouse smartphone with top-of-the-line specs, a mind-blowing camera, and cutting-edge AI features. However, its high price, large form factor, and Samsung’s software bloat may not be for everyone. If you want the absolute best flagship phone available today, this is the one to beat.

Rating: 9/10 ⭐⭐⭐⭐⭐⭐⭐⭐⭐
                                 
reviewed by Moona
""")
print("\n",result.keys())
print("\n")
print(result)

