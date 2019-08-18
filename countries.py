import json
import wikipedia


countries_list = []
with open('countries.json', encoding="utf-8") as datafile:
  json_data = json.load(datafile)
  for item in json_data:
    country_name_dict = item['name']['common']
    countries_list.append(country_name_dict)


wiki_url = []
for i in countries_list:
  try:
    a = wikipedia.page(i).url
  except wikipedia.exceptions.DisambiguationError as e:
    a = wikipedia.page(e.options[0]).url
  wiki_url.append(a)


countries_url = dict(zip(countries_list, wiki_url))


def countries_wiki(dicty, out):
  with open(out,'w', encoding="utf-8") as output:
    for k, v in dicty.items():
      output.write('{} - {}\n'.format(k, v))

if __name__ == '__main__':
  countries_wiki(countries_url, 'countries_wiki.txt')



