
from urllib.request import urlopen

class webClient(object):
    """webClient class"""
    def __init__(self):
        super(webClient, self).__init__()

    def download_page(arg):

        f = urlopen("http://www.eps.udl.cat/ca/")
        page = f.read()
        f.close()
        return page

    def run(self):
        #download a web page
        page = self.download_page()
        #search activity in a web page
        #print the activities
        print(page)


if __name__ == "__main__":
    c = webClient()
    c.run()
