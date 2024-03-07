
import openai
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.environ.get("OPENAI_API_KEY")
openai.api_key = api_key

def recommend_text(result):
    text=f" {result}Imagine you're a calorie expert helping someone track their dietary intake . Based on the provided data and considering the general average daily calorie requirement of around 2200 calories, provide personalized recommendations to adjust their diet. Offer suggestions to increase or decrease their calorie intake , Remember to focus on balanced nutrition and overall well-being in your recommendations. Use the data given to highlight what is being recommneded Strictly windup in five small bullet points"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use the GPT-3.5 Turbo model
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": text},
        ],
    )
    
    return response.choices[0].message["content"]



