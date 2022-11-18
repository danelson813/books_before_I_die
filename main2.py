import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_best-selling_books"
base = "https://en.wikipedia.org/"

books = pd.read_html(url)

df = pd.DataFrame()

# for i in range(4):
#     df = pd.concat([df, books[i]], axis=0)    
# print(df.tail())
# df.fillna('Unknown', inplace=True)
# df.to_csv('results.csv', index=False)
df = pd.read_csv('results.csv')
print(df.info())
