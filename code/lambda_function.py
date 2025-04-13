import json
import requests
import urllib3
import os

urllib3.disable_warnings()

def lambda_handler(event, context):
    url = os.getenv("URL")
    response = requests.get(url, verify=False)
    numeros = json.loads(response.text)['dezenas']
    #print(numeros)

    return {
        'statusCode': 200,
        'body': json.dumps(numeros)
    }