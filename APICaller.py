import requests
url = "https://find.some.api"

dataexample = '''{
  "query": {
    "bool": {
      "must": [
        {
          "text": {
            "record.document": "SOME_JOURNAL"
          }
        },
        {
          "text": {
            "record.articleTitle": "farmers"
          }
        }
      ],
      "must_not": [],
      "should": []
    }
  },
  "from": 0,
  "size": 50,
  "sort": [],
  "facets": {}
}'''

def sendRequest() :
    response = requests.get(url)
    return response

def parseResponse(response, type) :
    match type:
        case "rent":
            return response
        case "condo":
            return response
        case "plex":
            return response
        case "popStat":
            return response