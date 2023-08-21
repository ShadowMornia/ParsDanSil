import tkinter as tk
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

def search_films():
    search_query = search_entry.get()
    result_text.delete(1.0, tk.END)  
    result_text.insert(tk.END, f"Идет поиск фильмов по запросу: {search_query}\n\n")

    chromedriver_path = "C:/Python/chromedriver-win64/chromedriver.exe"
    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Chrome(service=Service(chromedriver_path), options=options)
    
    try:
        url = "https://kinobase.org/films"
        browser.get(url)
        open_search = browser.find_element(By.CLASS_NAME, "form-control")
        open_search.click()

        search = browser.find_element(By.CLASS_NAME, "form-control")
        search.send_keys(search_query)
        search.send_keys(Keys.RETURN)

        time.sleep(5)

        soup = BeautifulSoup(browser.page_source, 'lxml')
        film_links = []

        film_items = soup.find_all('div', class_='col-xs-2 item')
        for item in film_items:
            link = item.find('a', class_='link')
            if link and 'href' in link.attrs:
                film_links.append(link['href'])

        for link in film_links:
            result_text.insert(tk.END, f"{link}\n")

    except Exception as e:
        result_text.insert(tk.END, f"An error occurred: {str(e)}\n")
    finally:
        browser.quit()

root = tk.Tk()
root.title("Поиск фильмов")

search_label = tk.Label(root, text="Введите запрос:")
search_entry = tk.Entry(root)
search_button = tk.Button(root, text="Найти", command=search_films)
result_text = tk.Text(root, wrap=tk.WORD, width=50, height=15)

search_label.pack(pady=10)
search_entry.pack(pady=5)
search_button.pack(pady=5)
result_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

root.mainloop()
