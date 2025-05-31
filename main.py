"""
    model = lms.llm("google/gemma-3-12b")
    
    result = model.respond("Respond in one sentence only. What is the meaning of life? ")
    
    print(result)
"""


import os
import sys
import requests
import urllib3
import lmstudio as lms
import bs4
import json

class reqAi:
    def __init__(self):
        self.http = urllib3.PoolManager()
        
        self.base = "http://localhost:1234/v1/chat/completions"
        self.header = {"Content-Type": "application/json"}

        
        
    def requestEndPoint(self, data):
        self.data = {
            "model": "google/gemma-3-12b",
            "messages": [
                { "role": "system", "content": "Answer in one sentence on what this webpage is." },
                { "role": "user", "content": data }
            ],
            "temperature": 0.7,
            "max_tokens": 4096,
            "stream": False
        }
        
        req = self.http.request(
            "POST",
            self.base,
            headers=self.header,
            body=json.dumps(self.data)
        )
        
        if req.status == 200:
            try:
                no_bit = req.data.decode('utf-8')
                load = json.loads(no_bit)
                dumped = json.dumps(load, indent=4, sort_keys=True)
                print(dumped)   
            except json.JSONDecodeError:
                print("Error: Response is not in json format")
                print("Raw response: ", req.data.decode('utf-8'))         

        else: 
            print("ERROR: Could not access API")



class getSiteData:
    """
        Objective:  
            Get the html data of website to pass into AI
            
        Steps:
            1. Open possiblesites.txt
            2. parse through each one
            3. if website was success then you pass it onto the ai
            4. if at any moment the program has to stop, store the last website visited in a text file.
            5. only continue once the AI is done generating
            6. write what the AI said
    """
    
    def __init__(self):
        self.possible_sites = open("assets/possiblesites.txt", "r")
    
    def get_site(self):
        for item in self.possible_sites:
            print(item)
    
def main():
    # get website data
    site_data = getSiteData()
    site_data.get_site()

    # make the request to the AI
    #cl = reqAi()
    #res = cl.requestEndPoint()
    #print(res)

if __name__ == "__main__":
    main()