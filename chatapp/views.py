from django.shortcuts import render
import requests
import openai
def home(request):
    if request.method == 'POST':
        user_input = request.POST['user_input']
        openai_key = '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'
        response = get_openai_response(user_input, openai_key)
        return render(request, 'home.html', {'user_input': user_input, 'response': response})
    return render(request, 'home.html')

def get_openai_response(input_text, api_key):
    url = 'https://api.openai.com/v1/engines/davinci-codex/completions'
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {api_key}'}
    data = {
        'prompt': input_text,
        'max_tokens': 50
    }
    
    try:
        response = requests.post(url, json=data, headers=headers)
        print(response.status_code)  # แสดง HTTP status code
        print(response.text)  # แสดงเนื้อหาของ response

        response_data = response.json()
        
        if 'choices' in response_data and response_data['choices']:
            return response_data['choices'][0]['text']
        else:
            return "Error: No response from AI"
    except Exception as e:
        return f"Error: {str(e)}"

