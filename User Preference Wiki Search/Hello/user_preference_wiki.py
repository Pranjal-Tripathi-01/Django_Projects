import wikipediaapi, requests, webbrowser

wiki_wiki = wikipediaapi.Wikipedia('en')

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"
choice= str(input("Enter Your Choice: "))
SEARCHPAGE = choice

PARAMS = {
    "action": "query",
    "format": "json",
    "list": "search",
    "srsearch": SEARCHPAGE,
    "srlimit":"500"
}

Response = S.get(url=URL, params=PARAMS)
DATA = Response.json()

count= 0
condition= False
while not condition:
    title= "".join(i for i in DATA['query']['search'][count]['title'] if ord(i)<128)
    url= 'http://en.wikipedia.org/wiki/'+title.replace(" ","_")
    print("Article Title: ",title)
    user_choice= str(input("Do you want to read this article? (y/n) "))
    print()
    if user_choice == "y":
        condition= True
        webbrowser.open_new_tab(url)
    elif user_choice == 'n':
        count+=1

