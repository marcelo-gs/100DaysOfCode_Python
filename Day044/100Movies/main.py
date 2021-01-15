from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
empireonline = response.text

soup = BeautifulSoup(empireonline, "html.parser")

titles = soup.find_all(name="h3", class_="title")
movies= {}
for title in titles:
    if ")" in title.getText():
        movies[int(title.getText().split(")")[0])] = title.getText().split(")")[1].strip()
    elif ":" in title.getText():
        movies[int(title.getText().split(":")[0])] = title.getText().split(":")[1].strip()
    elif "Trainspotting" in title.getText():
        movies[49] = title.getText()
    else:
        #the first one!
        movies[1] = title.getText()

with open("top100-best_movies.txt", "w", encoding="utf-8") as file:
    for i in range(101):
        if i > 0:
            try:
                file.write(f"{i}) -> {movies[i]}\n")
            except:
                file.write(f"{i}) -> No Movie on this index\n")