from urllib.request import urlopen
import bs4

class Pagina(object):
    """clase Pagina"""
    def __init__(self):
        super(Pagina, self).__init__()

    def download_page(arg):

        f = urlopen("https://www.banggood.com/es/Wholesale-Electronics-c-1091.html?newversion=1")
        page = f.read()
        f.close()
        return page



    def run(self):
        #descargar pagina
        page = self.download_page()
        #buscar determinado texto en pagina
        #printar texto
        print(page)


if __name__=="__main__":
    p = Pagina()
    p.run()
