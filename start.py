from main import SummarizeUrl
from pprint import pprint


url1='https://timesofindia.indiatimes.com/entertainment/hindi/movie-reviews/padmaavat/movie-review/62622503.cms'

url2='https://www.ndtv.com/entertainment/padmaavat-movie-review-deepika-padukone-is-to-die-for-in-sanjay-leela-bhansalis-tepid-film-1804438'

url3='http://indianexpress.com/article/entertainment/movie-review/padmavati-movie-review-star-rating-5036330/'


summaries1 = SummarizeUrl(url1)
summaries2 = SummarizeUrl(url2)
summaries3 = SummarizeUrl(url3)

print summaries1
print "\n"
print summaries2
print "\n"
print summaries3
print "\n"


summaries1 = " ".join(summaries1)
summaries2 = " ".join(summaries2)
summaries3 = " ".join(summaries3)

pprint(summaries1)
print "\n"
pprint(summaries2)
print "\n"
pprint(summaries3)
print "\n"
