from urllib.request import urlopen
import bs4

class Weather(object):
    """clase Weather"""
    def __init__(self):
        super(Weather, self).__init__()

    def download_page(arg):

        f = urlopen("http://api.openweathermap.org/data/2.5/weather?q=Fraga,es&APPID=2a6e456423f423494c4488f01698b2b6&mode=xml&units=metric")
        page = f.read()
        f.close()
        return page

    def search_text(self,page):
        tree = bs4.BeautifulSoup(page,"lxml")
        text = tree.find_all("city")
        act_list=[]
        for activity in text:
            title = activity.find("sun")
            act_list.append((title["set"]))
        return act_list

    def run(self):
        #descargar pagina
        page = self.download_page()
        #buscar determinado texto en pagina
        data = self.search_text(page)
        #printar texto
        print(data)


if __name__=="__main__":
    p = Weather()
    p.run()
