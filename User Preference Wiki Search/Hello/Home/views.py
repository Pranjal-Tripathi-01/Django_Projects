from django.shortcuts import render, HttpResponse
import wikipediaapi, requests, webbrowser
from Home.models import get_choice

def index(request):
    global  ch, title1, url
    title1= ''
    url= ''

    if request.method== 'POST':
        if request.POST.get('choice'):
            ch = request.POST.get('choice')


            wiki_wiki = wikipediaapi.Wikipedia('en')

            S = requests.Session()

            URL = "https://en.wikipedia.org/w/api.php"
            SEARCHPAGE = ch

            PARAMS = {
                "action": "query",
                "format": "json",
                "list": "search",
                "srsearch": SEARCHPAGE,
                "srlimit":"500"
            }

            Response = S.get(url=URL, params=PARAMS)
            DATA = Response.json()
            title1= "".join(i for i in DATA['query']['search'][100]['title'] if ord(i)<128)
            url= 'http://en.wikipedia.org/wiki/'+title1.replace(" ","_")

            return render(request,'index.html', context={'title': title1, 'url':url})

        if request.POST.get('user_choice'):
            user_choice= request.POST.get('user_choice')
            wiki_wiki = wikipediaapi.Wikipedia('en')

            S = requests.Session()

            URL = "https://en.wikipedia.org/w/api.php"
            SEARCHPAGE = ch

            PARAMS = {
                "action": "query",
                "format": "json",
                "list": "search",
                "srsearch": SEARCHPAGE,
                "srlimit":"500"
            }

            Response = S.get(url=URL, params=PARAMS)
            DATA = Response.json()
            condition= False
            while not condition:
                if user_choice == 'n':
                    for next in range(499):
                        title2= "".join(i for i in DATA['query']['search'][next]['title'] if ord(i)<128)
                        url= 'http://en.wikipedia.org/wiki/'+title2.replace(" ","_")
                    return render(request, 'index.html', context={'title': title2, 'url':url})
                    
                
                
    else:
        return render(request, 'index.html')