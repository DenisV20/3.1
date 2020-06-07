import json
list_description_split = []
dict_description_split ={}
word_title = []
with open('newsafr.json', 'r', encoding= 'UTF-8') as f:
    data = json.load(f)
    for list_items in data['rss']['channel']['items']:
        list_description_split.append(list_items['description'])
    for words in list_description_split:
        word_title.extend(words.title().split())

def list_top_10(list_of_words):
    for word in list_of_words:
        if len(word) > 6 and word in dict_description_split:
            dict_description_split[word] += 1
        else:
           dict_description_split[word] = 1

    sort_values_10 = sorted(dict_description_split.items(), key=lambda x: x[1], reverse=True)[0:10]
    #print(sort_values_10)
    return sort_values_10

#top_list = list_top_10(word_title)
for top in list_top_10(word_title):
    print(top[0],top[1])




























































