import requests
import pandas as pd
from bs4 import BeautifulSoup
# 发送get请求
url = 'https://iftp.chinamoney.com.cn/english/bdInfo/'
params = {
    'disclosureType': 'Primary+Market+Issue+Disclosure',
    'bondType': 'Treasury+Bond',
    'issueYear': '2023',
    'page': '1'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
}
response = requests.get(url, params=params, headers=headers)
html = response.content

# 解析HTML并提取表格数据
soup = BeautifulSoup(html, 'html.parser')
table_html = soup.find('table', {'class': 'iftp-tbl'})
table_data = []
headers = [header.text.strip() for header in table_html.find_all('th')]
for row in table_html.find_all('tr'):
    row_data = []
    for cell in row.find_all('td'):
        row_data.append(cell.text.strip())
    if row_data:
        table_data.append(row_data)
# 保存为CSV文件
df = pd.DataFrame(table_data, columns=headers)
df.to_csv('treasury_bonds_2023.csv', index=False)

print('保存成功！')