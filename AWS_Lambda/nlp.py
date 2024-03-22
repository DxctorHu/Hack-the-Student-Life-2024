import json
from openai import OpenAI
from os import getenv

# gets API Key from environment variable OPENAI_API_KEY
def generate_label(content: str, is_event: bool):
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=getenv("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"),
    )
    completion = client.chat.completions.create(
        #   extra_headers={
        #     "HTTP-Referer": $YOUR_SITE_URL, # Optional, for including your app on openrouter.ai rankings.
        #     "X-Title": $YOUR_APP_NAME, # Optional. Shows in rankings on openrouter.ai.
        #   },
        model="cognitivecomputations/dolphin-mixtral-8x7b",
        messages=[
            {
                "role": "admin",
                "content": "Generate a comma separated list with the FIVE MOST IMPORTANT keywords from the following information: " + content,
            },
        ],
    )
    keywords = completion.choices[0].message.content
    # output_list = output_text.split(", ")
    date = "0000"
    if is_event:
        date = "0402"
    completion2 = client.chat.completions.create(
        #   extra_headers={
        #     "HTTP-Referer": $YOUR_SITE_URL, # Optional, for including your app on openrouter.ai rankings.
        #     "X-Title": $YOUR_APP_NAME, # Optional. Shows in rankings on openrouter.ai.
        #   }
        model="cognitivecomputations/dolphin-mixtral-8x7b",
        messages=[
            {
                "role": "admin",
                "content": "Provide a very very short summary of the following: " + content,
            },
        ],
    )
    summary = completion2.choices[0].message.content
    # for i in range(len(output_list)):
    #     output_list[i].strip()
    return date, keywords, summary
