import random
import string
import requests
from bs4 import BeautifulSoup
import colorama
from os import getcwd
def randstr():
    letters = string.ascii_lowercase+string.ascii_uppercase+string.digits
    result_str = ''.join(random.choice(letters) for i in range(3))
    return result_str

def main(tlets,savefile):
    while True:
        session = requests.Session()
        linkz = f'https://dosyaupload.com/{tlets}{randstr()}'
        resp = session.get(linkz)
        if resp.status_code == 200:
            sup = BeautifulSoup(resp.content, "html.parser")
            file_name = sup.find('div',{'class':'heading-1'}).get_text(strip=True).rsplit('indir')[0]
            if not 'Hata' in file_name:
                print(colorama.Fore.GREEN,f'File name : {file_name} - Download link : {linkz} - Scraped by blueshillz')
                if savefile == 'y':
                    with open('hits.txt','a',encoding='UTF-8') as sfile:
                        sfile.write(f'File name : {file_name} - Download link : {linkz} - Scraped by blueshillz\n')

if __name__=='__main__':
    print(colorama.Fore.RED,'Blueshillz dosyaupload scraper\nGithub : https://github.com/blueshillz/dosyaupload-scraper')
    tlets = input(f'{colorama.Fore.CYAN}Enter 2 letters of an exist link\n')
    savefile = input(f'{colorama.Fore.CYAN}Do you want to save hits to a file? (y/n)\n')
    if savefile == 'y':
        print(colorama.Fore.GREEN,f'Hits will be saved to {getcwd()}\\hits.txt')
    main(tlets,savefile)
