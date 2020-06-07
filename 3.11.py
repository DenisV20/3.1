
import xml.etree.ElementTree as ET

list_description = []
dict_description_split = {}
parser = ET.XMLParser(encoding= 'UTF-8')
tree = ET.parse('newsafr.xml', parser)
root = tree.getroot()

xml_description = root.findall('channel/item/description')
for descript in xml_description:
    descript = descript.text
    list_description.append(descript)
    list_description_split = str(list_description).title().split()

def list_top_10(list_of_words):
    for word in list_of_words:
        if len(word) > 6 and word in dict_description_split:
            dict_description_split[word] += 1
        else:
            dict_description_split[word] = 1
    sort_values_10 = sorted(dict_description_split.items(), key=lambda x: x[1], reverse=True)[0:10]
    # print(sort_values_10)
    return sort_values_10

# list_top_10(list_description_split)

for top in list_top_10(list_description_split):
    print(top[0],top[1])







