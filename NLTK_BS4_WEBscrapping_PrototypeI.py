#Webcrawler
#AUTHOR: Eric Ávila
#rexfarell@gmail.com

import nltk
from nltk import *
import re, pprint
from urllib import request
from bs4 import BeautifulSoup as bs
from nltk import word_tokenize
import requests

#Notes:
#If you only want the text part of a document or tag, you can use the get_text() method.It returns all the text in a document or beneath a tag, as a single Unicode string:



def Crawler():

    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)     Chrome/37.0.2049.0 Safari/537.36'}
    r = requests.get("https://en.wikipedia.org/wiki/Chatbot", headers=headers)
    print (r)
    #print ("headers",r.headers)
    url= "https://en.wikipedia.org/wiki/Chatbot"
    html = request.urlopen(url).read().decode("utf8")
    html[:10000]
    raw=bs(html, "html.parser").get_text()
    tokens= word_tokenize(raw)
    print("Quantity of total Tokens in the target: ",len(tokens))
    end_tokens=tokens[874:4701]
    print("Quantity of  useful Tokens in the target: ")
    print("""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                                                                                                                        
      WEBSCRAPER V.01                                                                                                                   
            INSTRUCTIONS:
            This program automatically crawls the target (A Wikipedia article about chabots)
            However, if you want to see the preliminary results on Screen you need to
            *TYPE: Crawler()

            Likewise, If you want to save the text in a txt file, just *TYPE: savingToTXT() .It will also give you a  cleaner preview
            The file will be saved in your Python working folder under the name " " 

            HAPPY CRAWLING
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


""") 
    return end_tokens

#Uncoment to find the aprox beginning and end indexes of the article
#print("Beginning",tokens.index("convincingly"))
#print("End",tokens.index("Forrester"))


end_tokens=Crawler()

def savingToTXT():
      #txtOutput= (end_tokens)
      txt=textwrap.fill(' '.join(map(str, end_tokens)),100)
      print(txt[:15])
      with open("WebScrapped_Chatbot_Article.txt","w") as f:
          f_contents=f.write(txt)
      return txt


def main():
      print("Welcome to my webscrapper program")
      end_tokens= Crawler()
   



