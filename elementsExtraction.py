# Extracts the titles and descriptions from the news dictionary and prints them to the console
def listNews(news):
  titles = [article["title"] for article in news["articles"]]
  descriptions = [article["description"] for article in news["articles"]]
  for title, description in zip(titles, descriptions):
    print(title+"\n")
    print (description.replace('\n', ''))
    print("\n"+'{:-^50}'.format('')+"\n")

# Grabs the titles, descriptions and contents from the news dictionary and returns them as a list of strings
def newsGrabber(news):
  titles = [article["title"] for article in news["articles"]]
  descriptions = [article["description"] for article in news["articles"]]
  contentQuantity = [article["content"] for article in news["articles"]]
  data=[]
  for title, description, content in zip(titles, descriptions, contentQuantity):
    input = title + description + content
    data.append(input)
  return data