import os
import openai
import datetime

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

openai.api_key = open_file('openaiapikey.txt')
open_ai_api_key = os.getenv(openai.api_key)
# print(openai.FineTune.list())
response = openai.FineTune.list()   
obim = input('Skraceni izvestaj d/n? ')
print('')

if obim == 'd':
    print("Valid fine tuned models: ")
    m=0
    for model in response['data']:
        if model['fine_tuned_model'] is not None:
            m=m+1
            timestamp=model['created_at']
            dt_object = datetime.datetime.fromtimestamp(timestamp)
            # Convert datetime object to a string in a desired format
            formatted_date = dt_object.strftime("%Y-%m-%d %H:%M:%S")
            print('')
            print(f"Model no {m} ", end='')
            print(f"kreiran {formatted_date} ", end='')
            print(model['model'] + ' ', end='')
            print(model['fine_tuned_model'] + ' ', end='')
            print(model['status'])
            
else:
    print("All fine tuned models: ")
    print('')
    print(response)
print('')


