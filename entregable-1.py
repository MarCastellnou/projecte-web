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

    def page_lxml(self,page):
        tree = bs4.BeautifulSoup(page,"lxml")
        return tree

    def search_prices(self,page):
        text = page.find_all("div","priceitem")
        list_price=[]
        for activity in text:
            offer_p = activity.find("span","price")
            original_p = activity.find("span","price_old")
            list_price.append((offer_p.text, original_p.text))
        return list_price

    def search_name_product(self,page):
        text1 = page.find_all("span","title")
        list_name=[]
        for activity in text1:
            name = activity.find("a")
            list_name.append(name.text)
        return list_name

    def print_data(self,price,name):
        for x in range(len(price)):
            print("\nNombre del producto= ",name[x],"\nPrecio en oferta= ",price[x][0],"\nPrecio original= ",price[x][1])

    def run(self):
        page = self.download_page()
        lxml = self.page_lxml(page)
        price = self.search_prices(lxml)
        name = self.search_name_product(lxml)
        self.print_data(price,name)


if __name__=="__main__":
    p = Pagina()
    p.run()
