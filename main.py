import requests
from bs4 import BeautifulSoup

urls = {
    'restaurant': ['https://in.ncu.edu.tw/alumni/web/benefits.php?area=&keyword=&type=restaurant&page=0',
                   'https://in.ncu.edu.tw/alumni/web/benefits.php?area=&keyword=&type=restaurant&page=10',
                   'https://in.ncu.edu.tw/alumni/web/benefits.php?area=&keyword=&type=restaurant&page=20',
                   'https://in.ncu.edu.tw/alumni/web/benefits.php?area=&keyword=&type=restaurant&page=30',
                   'https://in.ncu.edu.tw/alumni/web/benefits.php?area=&keyword=&type=restaurant&page=40',
                   'https://in.ncu.edu.tw/alumni/web/benefits.php?area=&keyword=&type=restaurant&page=50',
                   'https://in.ncu.edu.tw/alumni/web/benefits.php?area=&keyword=&type=restaurant&page=60'],
    'transportation': ['https://in.ncu.edu.tw/alumni/web/benefits.php?type=transportation#'],
    'grocery': ['https://in.ncu.edu.tw/alumni/web/benefits.php?area=&keyword=&type=grocery&page=0',
                'https://in.ncu.edu.tw/alumni/web/benefits.php?area=&keyword=&type=grocery&page=10',
                'https://in.ncu.edu.tw/alumni/web/benefits.php?area=&keyword=&type=grocery&page=20'],
    'amusement': ['https://in.ncu.edu.tw/alumni/web/benefits.php?area=&keyword=&type=amusement&page=0',
                  'https://in.ncu.edu.tw/alumni/web/benefits.php?area=&keyword=&type=amusement&page=10'],
    'snack': ['https://in.ncu.edu.tw/alumni/web/benefits.php?area=&keyword=&type=snack&page=0',
              'https://in.ncu.edu.tw/alumni/web/benefits.php?area=&keyword=&type=snack&page=10',
              'https://in.ncu.edu.tw/alumni/web/benefits.php?area=&keyword=&type=snack&page=20'],
    'school': ['https://in.ncu.edu.tw/alumni/web/benefits.php?type=school#'],
    'hotel': ['https://in.ncu.edu.tw/alumni/web/benefits.php?area=&keyword=&type=hotel&page=0',
              'https://in.ncu.edu.tw/alumni/web/benefits.php?area=&keyword=&type=hotel&page=10',
              'https://in.ncu.edu.tw/alumni/web/benefits.php?area=&keyword=&type=hotel&page=20',
              'https://in.ncu.edu.tw/alumni/web/benefits.php?area=&keyword=&type=hotel&page=30',
              'https://in.ncu.edu.tw/alumni/web/benefits.php?area=&keyword=&type=hotel&page=40',
              'https://in.ncu.edu.tw/alumni/web/benefits.php?area=&keyword=&type=hotel&page=50',
              'https://in.ncu.edu.tw/alumni/web/benefits.php?area=&keyword=&type=hotel&page=60',
              'https://in.ncu.edu.tw/alumni/web/benefits.php?area=&keyword=&type=hotel&page=70',
              'https://in.ncu.edu.tw/alumni/web/benefits.php?area=&keyword=&type=hotel&page=80',
              'https://in.ncu.edu.tw/alumni/web/benefits.php?area=&keyword=&type=hotel&page=90'],
    'medicine': ['https://in.ncu.edu.tw/alumni/web/benefits.php?type=aesthetic%20medicine#']
}
typelist = ['restaurant']#, 'transportation', 'grocery', 'amusement', 'snack', 'school', 'hotel', 'medicine']

for i in typelist:
    typeurl = urls[i]
    length = len(typeurl)
    for j in range(1):
        url = typeurl[j]
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        elements = soup.find_all(class_='row py-3')
        
        for element in elements:
            slist = []
            title = element.find('h4', class_='my-1')
            slist.append(title.get_text(strip = True))
            content = element.find_all('p', class_='my-0')
            index1 = ''
            index = 0
            for c in content:
                if index != 4:
                    index1 += c.get_text(strip=True)
                    index1 += '\n'
                print(c.get_text(strip=True))
            print()
            
            
            
    
        
        
    

exit()

# Finding elements with class 'my-1'
elements = soup.find_all(class_='my-1')

# Extracting and printing the text from each element
for element in elements:
    print(element.get_text(strip=True))
