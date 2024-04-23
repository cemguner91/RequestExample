import tkinter
import requests
from bs4 import BeautifulSoup


target_url = "https://news.ycombinator.com/"
foundList = []
screen = tkinter.Tk()
screen.minsize(1000,800)
screen.title("Haber Linlklerini Getir")
entry_text = tkinter.Text()
entry_text.size()
entry_text.pack()

def make_request(url):
    response = requests.get(url)
    souping = BeautifulSoup(response.text, "html.parser")
    return souping


def take_links(url):
    links = make_request(url)
    new_links = []
    for link in links.find_all("a"):
        found_link = link.get("href")
        if found_link and found_link.startswith("https://"):
            if found_link not in foundList:
                foundList.append(found_link)
                new_links.append(found_link)
    return new_links


def entry_writing():
    new_links = take_links(target_url)
    for link in new_links:
        entry_text.insert(tkinter.END, link + "\n")


news_buton = tkinter.Button(command=entry_writing)
news_buton.config(text="Haberlerin Linklerini Göster")
news_buton.pack()

screen.mainloop()