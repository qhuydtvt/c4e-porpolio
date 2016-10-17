import bs4
import urllib.request
from movie import Movie
from mlab import  *

# Get HTML from web site
link = "https://www.themoviedb.org/discover/movie?sort_by=popularity.desc"
response = urllib.request.urlopen(link)
html = response.read()

# Parse html
soup = bs4.BeautifulSoup(html, 'html.parser')
results_tag = soup.find("div", "results")
item_tags = soup.find_all("div", "item poster card")

mlab_connect()

for movie in Movie.objects:
    movie.delete()

print("Done removing")

for item_tag in item_tags:
    div_info = item_tag.find("div", "info")
    title = (div_info.find("a","title"))["title"]
    desc = div_info.find("p", "overview").string
    img_link = item_tag.find("img", "poster")["data-src"]
    rate = float(str(div_info.find("span", "vote_average"))[27:30])
    # print("< {0}, {1}, {2} >".format(title, desc, img_link))
    print("Saving movie {0}".format(title))
    (Movie(title=title, desc=desc, img_link=img_link, rate=rate)).save()
    print("Done")