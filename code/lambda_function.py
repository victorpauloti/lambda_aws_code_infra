import json
import requests
import urllib3

urllib3.disable_warnings()

def lambda_handler(event, context):
    url = 'https://loteriascaixa-api.herokuapp.com/api/megasena/latest'
    response = requests.get(url, verify=False)
    numeros = json.loads(response.text)['dezenas']
    #print(numeros)

    return {
        'statusCode': 200,
        'body': json.dumps(numeros)
    }