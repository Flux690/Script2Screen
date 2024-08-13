import requests

# OpenAI API configuration
openai_api_key = 'Paste your OpenAI API Key here'

def extract_keywords(text):
    url = 'https://api.openai.com/v1/engines/text-davinci-003/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {openai_api_key}'
    }
    data = {
        'prompt': f'Extract the top 5 most relevant keywords from this text. Make the first letter of every word uppercase and separate with commas:\n\n{text}',
        'temperature': 0.5,
        'max_tokens': 60,
        'top_p': 1.0,
        'frequency_penalty': 0.8,
        'presence_penalty': 0.0
    }

    response = requests.post(url, headers=headers, json=data)
    response_data = response.json()

    # Extract the keywords from the response
    choices = response_data['choices']
    if len(choices) > 0:
        keywords = choices[0]['text'].strip().split(',')
        keywords = [keyword.strip().capitalize() for keyword in keywords]
        return keywords[:5]
    else:
        return []