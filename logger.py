import requests

class SlackWebhook():
    def __init__(self, webhook_url, verbose=False):
        self.webhook_url = webhook_url
        self.verbose = verbose
    
    def __call__(self, *args, **kwargs):
        message, sep = "", " - "
        for a in args: 
            message += "{}".format(a) + sep
        for key, val in kwargs.items(): 
            message += "{}: {}".format(key, val) + sep 
        message = message.strip(sep)
        self.send(message)
    
    def log(self, message):
        if self.verbose: print("{}".format(message))
            
    def send(self, message):
        try:
            res = requests.post(url=self.webhook_url, headers={"Content-type": "application/json"}, json={"text":message})
            self.log(res.status_code)
        except Exception as e:
            self.log(e)
        
        
webhook_url = "slack-webhook-url"
slack_loggger = SlackWebhook(webhook_url)
slack_loggger("New Model",  epoch=1, val_score=1.23)
    
