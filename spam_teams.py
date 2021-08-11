import requests
import json

from extract_quotes import read_quote

# URL til #Kaffe på Teams 
url = 'https://Your Teams Webhook URL here'

def post_on_teams():
    null=None
    quote = read_quote()
    kaffe_tekst = f"**Fresh coffee in the Kitchen!**\n\n *{quote}*"

    myobj2 = '''{
   "type":"message",
   "attachments":[
      {
         "contentType":"application/vnd.microsoft.card.adaptive",
         "contentUrl":null,
         "content":{
            "$schema":"http://adaptivecards.io/schemas/adaptive-card.json",
            "type":"AdaptiveCard",
            "version":"1.2",
            "body":[
                {
                "type": "TextBlock",
                "text": "%s",
                "wrap": true
                }
            ]
         }
      }
   ]
}''' % (kaffe_tekst)
    x = requests.post(url, data=myobj2)
    print(x.text)

if __name__=="__main__":
    post_on_teams()