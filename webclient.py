
from urllib.request import urlopen
import bs4

class webClient(object):
    """webClient class"""
    def __init__(self):
        super(webClient, self).__init__()

    def download_page(arg):

        f = urlopen("http://www.eps.udl.cat/ca/")
        page = f.read()
        f.close()
        return page

    def search_activities(self, page):
        tree = bs4.BeautifulSoup(page,"lxml")
        activities = tree.find_all("div","featured-links-item")
        act_list=[]
        for activity in activities:
            title = activity.find("span","flink-title")
            link = activity.find("a")
            act_list.append((title.text,link["href"]))
            return act_list

    def run(self):
        #download a web page
        page = self.download_page()
        #search activity in a web page
        data = self.search_activities(page)
        #print the activities
        print(data)



if __name__ == "__main__":
    c = webClient()
    c.run()
