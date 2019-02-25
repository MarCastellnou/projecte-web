from urllib.request import urlopen
import bs4

class Pagina(object):
    """clase Pagina"""
    def __init__(self):
        super(Pagina, self).__init__()

    def download_page(arg):

        f = urlopen("https://www.banggood.com/Flashdeals.html")
        page = f.read()
        f.close()
        return page

    def search_offer(self,page):
        tree = bs4.BeautifulSoup(page,"lxml")
        text = tree.find_all("div","scroll_box")
        list=[]
        for activity in text:
            offer_p = activity.find("span","price")
            original_p = activity.find("span","price_old")
            name = activity.find("span","title")
            list.append((name.text, offer_p.text, original_p.text))
            return list

    def run(self):
        page = self.download_page()
        data = self.search_offer(page)
        print(data)


if __name__=="__main__":
    p = Pagina()
    p.run()
