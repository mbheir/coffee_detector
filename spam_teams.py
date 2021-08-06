import requests
import json

from extract_quotes import read_quote

# url = 'https://silabs.webhook.office.com/webhookb2/fb53d7d8-fe80-4116-bad7-8950b263c3c9@54dbd822-5231-4b20-944d-6f4abcd541fb/IncomingWebhook/e54f7df6d4444cd7933466378feef43f/b4fb2744-6e52-48e2-ae42-0d8ce6fde3fd'

# URL til #Kaffe på Teams 
url = 'https://silabs.webhook.office.com/webhookb2/94763cb3-0096-456a-b236-fc8a6dadb0d6@54dbd822-5231-4b20-944d-6f4abcd541fb/IncomingWebhook/e75c67c9391343a58926c7aaebcbbbe2/b4fb2744-6e52-48e2-ae42-0d8ce6fde3fd'

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