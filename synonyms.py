import json
import lemma
import requests

# Declaring variables for the Thesaurus API
def API(word, context):
    jsonData = []

    app_id  = "0717c053"
    app_key  = "9689bea0754bc4e29feb8874fa185efe"
    endpoint = "thesaurus"
    language_code = "en-us"
    url = "https://od-api.oxforddictionaries.com/api/v2/" + endpoint + "/" + language_code + "/" + word.lower()

    r = requests.get(url, headers = {"app_id": app_id, "app_key": app_key})
    response_json = r.json()
    if not 'results' in response_json: 
        return []
    
    data = response_json["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["subsenses"][0]["synonyms"]
    for x in range(len(data)):
        jsonData.append(lemma.Lemma(data[x]["text"], context))

    jsonDump = json.dumps(jsonData)
    return jsonDump