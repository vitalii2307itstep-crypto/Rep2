import sqlite3
import requests
import tkinter as tk
from tkinter import simpledialog
from bs4 import BeautifulSoup
class Database:
    def __init__(self):
        self.db = sqlite3.connect("sites.db")
        self.cursor = self.db.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS sites (url TEXT)"
        )
        self.db.commit()
    def add_site(self, url):
        self.cursor.execute(
            "INSERT INTO sites VALUES (?)", (url,)
        )
        self.db.commit()
    def get_sites(self):
        self.cursor.execute("SELECT url FROM sites")
        return self.cursor.fetchall()
    def clear(self):
        self.cursor.execute("DELETE FROM sites")
        self.db.commit()
class Parser:
    def search(self, word, sites):
        results = []
        for site in sites:
            try:
                page = requests.get(site[0], timeout=5)
                soup = BeautifulSoup(page.text, "html.parser")
                text = soup.get_text().lower()
                count = text.count(word.lower())
                if count > 0:
                    results.append((site[0], count))

            except requests.RequestException:
                pass
        results.sort(key=lambda x: x[1], reverse=True)
        return results
db = Database()
parser = Parser()
window = tk.Tk()
window.title("Web Search")
window.geometry("600x400")
window.configure(bg="#222222")
entry = tk.Entry(window, font=("Arial", 14))
entry.pack(pady=10)
def search():
    results.delete(0, tk.END)
    for site, count in parser.search(entry.get(), db.get_sites()):
        results.insert(tk.END, f"{count} coincidences: {site}")
def add_site():
    url = simpledialog.askstring("Website", "Enter URL:")
    if url:
        db.add_site(url)
def clear():
    db.clear()
    results.delete(0, tk.END)
tk.Button(window, text="Search", command=search).pack()
tk.Button(window, text="Add site", command=add_site).pack(pady=5)
tk.Button(window, text="Clear the database", command=clear).pack()
results = tk.Listbox(
    window, bg="#333333", fg="white", width=70
)
results.pack(pady=10, fill="both", expand=True)
window.mainloop()
db.db.close()
