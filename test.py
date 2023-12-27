import requests
from bs4 import BeautifulSoup

# 設定目標網址
url = 'https://in.ncu.edu.tw/alumni/web/benefits.phparea=&keyword=&type=restaurant&page=0'

# 發送HTTP請求
response = requests.get(url)

# 檢查請求是否成功
if response.status_code == 200:
    # 解析HTML內容
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 找到所有優惠區塊
    offers = soup.find_all('div', class_='row py-3')  # 這可能需要根據實際HTML結構調整
    
    # 儲存結果的列表
    results = []
    
    # 遍歷每個優惠區塊，提取和整理資訊
    for offer in offers:
        # 提取標題（例如店名或優惠名稱）
        title = offer.find('h4').text.strip() if offer.find('h4') else ''
        
        # 提取內容，將所有段落整合成一個字符串
        content = ' '.join(p.text.strip() for p in offer.find_all('p'))
        
        # 將提取的資訊添加到結果列表
        results.append(f"{title} {content}")
    
    # 打印結果
    for result in results:
        print(result)
else:
    print(f"Error: Unable to fetch the page. Status code: {response.status_code}")
