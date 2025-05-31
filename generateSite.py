"""
    This program is just to generate all possible website domains on the surface web
"""

import os
import sys
import json

class createWeb:
    def __init__(self):
        # open the files that contain each part
        self.possible = open("assets/possiblesites.txt", "a")
        self.wordlist = open("assets/words.txt", "r")
        self.domain_extension = open("assets/domainextensions.json", "r")
        
        self.body_obj = []
        
        #self.wordlist_json = json.load(self.wordlist)
        self.domain_extension_json = json.load(self.domain_extension)
        
    def one_word_gen(self):
        li = self.domain_extension_json['domain_extension'] #  get the domain extension
        
        for a in self.wordlist:
            body = a.strip()
            for dom in li:
                self.body_obj.append(f"{body}{dom}")
        
        for item in self.body_obj:
            self.possible.write(f"{item}\n")

        # close the files
        self.wordlist.close()
        self.domain_extension.close()
        self.possible.close()

def main():
    obj = createWeb()
    
    obj.one_word_gen()
    

main()