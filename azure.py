    import requests
    import json

    endpoint=""
    subscription_key=""

    language_api_url=endpiont +"/text/analytics/v3.1/languages"

    def detect_language(text):
        documents={
            "document":{
                {"id":"1","text":text}
            }
        }

        headers={
            "Ocp-Apim-Subscription-Key":subscription_key,
            "Content-Type":"application/json"
        }

        response=requests.post(language_api_url,headers=headers,json=documents)

        if response.status_code==200:
            language=response.json()
            return language
        else:
            return f"Error{response.status_code}"

    user_input=input("Enter your text to detect language")

    result=detect_language(user_input)

    print("Detected language(s)")
    print(json.dumps(result,indent=4))