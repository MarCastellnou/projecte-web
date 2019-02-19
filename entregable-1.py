from urllib.request import urlopen
import bs4

class Pagina(object):
    """clase Pagina"""
    def __init__(self):
        super(Pagina, self).__init__()

    def download_page(arg):

        f = urlopen("https://www.banggood.com/es/Flashdeals.html")
        page = f.read()
        f.close()
        return page

    def search_text(self,page):
        tree = bs4.BeautifulSoup(page,"lxml")
        text = tree.find_all("div","category_new_list")
        act_list=[]
        for activity in text:
            title = activity.find("span","price wh_cn")
            link = activity.find("")
            act_list.append((title.text,link[""]))
            return title

    def run(self):
        #descargar pagina
        page = self.download_page()
        #buscar determinado texto en pagina
        data = self.search_text(page)
        #printar texto
        print(data)


if __name__=="__main__":
    p = Pagina()
    p.run()
