# %% 
from bs4 import BeautifulSoup
import requests


# %% 
def get_rank(url):
    response = requests.get(url)
    print(response.text)
    soup = BeautifulSoup(response.text,'html.parser')

    for link in soup.find('div',{'class':'rank_innner_v2'}):
        if 'href' in link.attrs:


                if 'href' in link.attrs:


        print(link)

    return rank


if __name__ == '__main__':
    url = 'https://datalab.naver.com/'

    
   

    rank = get_rank(url)
    print(rank)
