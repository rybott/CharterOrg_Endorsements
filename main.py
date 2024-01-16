from bs4 import BeautifulSoup
import requests

print("Runnning")

url = "https://www.looktothestars.org/charity"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
Organizations = soup.find_all('h3',{'class': 'media-heading'})


# Getting the Celebrities
Organization_List = []
Celebrity_List = []

for Organization in Organizations:
  Organization_Name = Organization.find('a').get_text()
  Supporter_URL = Organization.find('a')['href']
  
  response_new = requests.get(Supporter_URL)
  soup_new = BeautifulSoup(response_new.content, 'html.parser') 

  supporters = soup_new.find('section', {'id': 'supporters'})
  celebrities = supporters.find_all('div', {'class': 'media-body'})

  for celebrity in celebrities:
    name_clean1 = celebrity.text
    
    Organization_List.append(Organization_Name)
    Celebrity_List.append(name_clean1)

print(Organization_List)
print(Celebrity_List)

