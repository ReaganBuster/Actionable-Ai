from ollama import Client
from groq import Groq

class Ai_engine():
    
    def __init__(self, apiKey, goal, reviews, business_data) -> None:
        self.api_Key = apiKey
        self.goal = goal
        self.reviews = reviews
        self.business_data = business_data

    def query_local_model(Self) -> str:
        models = ['deepseek-r1:7b','deepseek-r1:1.5b']
        client = Client(
        host='http://localhost:11434',
        headers={'x-some-header': 'some-value'}
        )
        output = client.chat(model=models[1], messages=[{'role': 'user', 'content': f"{Self.goal}, contantly keeping that in memory, commence with the following data {Self.business_data} {Self.reviews}."},])
        return(output.message.content)
    
    def query_online_model(Self) -> str :
        

        client = Groq(
            api_key=Self.api_Key,
        )

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"{Self.goal}, contantly keeping that in memory and previous context/recomendations if any {Self.business_data} for a more non repeatitive nuanced discussion on this business' success, commence with the following data {Self.reviews}.",
                }
            ],
            model="llama-3.3-70b-versatile",
        )

        return chat_completion.choices[0].message.content
    

    def generate_random_reviews(Self) -> str:
            client = Groq(
                api_key=Self.api_Key,
            )

            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": "Generate 30 random reviews for a fictional restaurant, make them believable, absoletly nothing should come after the last review please, not even an acknowlegment of response from you",
                    }
                ],
                model="llama-3.3-70b-versatile",
            )

            print(chat_completion.choices[0].message.content)
