'''
Author: rosa wang 
Date: 2021-02-16 16:53:57
LastEditTime: 2021-02-16 19:00:26
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /ten_apps/Users/rosawang/Desktop/cs_application/resume_projects/zillowScraper.py
'''
import requests
from bs4 import BeautifulSoup
import csv


class ZillowScraper:
    results = []

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'cache-control': 'max-age=0',
        'cookie': 'zguid=23|%24130fad5f-ec73-46ab-8b08-164f5e600d51; zgsession=1|d109a0bd-aaea-4327-ba8b-6a1e07e101a9; zjs_anonymous_id=%22130fad5f-ec73-46ab-8b08-164f5e600d51%22; _ga=GA1.2.1366003292.1606196308; _gid=GA1.2.1621946796.1606196308; _gcl_au=1.1.2119618559.1606196308; KruxPixel=true; DoubleClickSession=true; _pxvid=46fcba6e-2e17-11eb-a3bb-0242ac120008; JSESSIONID=ADA6C199E18AAC44C03E859DBE1A4BFA; _fbp=fb.1.1606196307815.44750306; _pin_unauth=dWlkPU4yRmxZalV5WldZdFlUbGpNaTAwTURSbUxUbGtNRGN0T1RGbVpqWTVNRFJoTjJSaw; __gads=ID=fb7d66100d34c50c:T=1606196318:S=ALNI_MaeGOWKvq7t0fptEWfEMHEcXt4KgQ; ki_r=; KruxAddition=true; ki_s=; G_ENABLED_IDPS=google; loginmemento=1|7f99ce28916589aaa34b3bd3bb773bfe65b608aad0bdc39e168bc26704a17432; ZILLOW_SSID=1|AAAAAVVbFRIBVVsVEtZM9%2F7vxMX883J5K%2B68Jsx39kNluUUAzIycx57o1Zqf5Gcacp9M%2F0Fkao1tWZ4SkBTImii22u5d; userid=X|3|68effc57631fe0cc%7C2%7ClGLIm7LVZ_QSJAnmTM0L8HLC4XhQtVuUr1Iuq2L-RXg%3D; ZILLOW_SID=1|AAAAAVVbFRIBVVsVEg0sVoK2%2FSfVoMAeri9zCxGSi5K8eoNgu8PqUFLxexzdurCt%2Bf6ob7nDqG4abAH8DN0JAVHYHgsB; zjs_user_id=%22X1-ZUtj1ki00qcvm1_2599o%22; optimizelyEndUserId=oeu1606201443171r0.9810999660065434; FSsampler=1267573903; _px3=0c8c5c98e7e3118904fadf5e5ab5663e1af3ff48b2bec4ce0e35375d4d988c6e:ZYOK+qlgTxGFd43nL/GqxypGsg+AGKKC3t03zjpkGM8bkfsCGiqOzEieNE1dkkqZZkRwv+m93C/43F4bsZABmg==:1000:IMxftrXcTjULXAolEeOuGBH7GbrnsIh5MbDqDZk08vErGn9fcvn2UgoVI37//vO0RUEb1NhmiAcMbc1Nxmp+hVcxmUTbOJoe0jKtxVvgfp/MNv5XWVZj/oHY0EEH53Lh2OJdAT+YzoaaOHHsRaSMiK9lOJfNLJXcvkyLpLp3Gkg=; _uetsid=4720a3502e1711eb809c13d79d4144d4; _uetvid=4720c0002e1711ebb98ac5cc20cd7896; ki_t=1606196318513%3B1606196318513%3B1606205078467%3B1%3B52; AWSALB=V/JTHrfSJGECKbS2gi+51/fdX3dXtU4LHLzI9O7Rg+FX9vva0TOb3RdwbEoWFQpuZMZI0iD5MteCUzlMpY8clTe29ZsqqxfmlCtMaammVQNRZOoP2RtByAWvlext; AWSALBCORS=V/JTHrfSJGECKbS2gi+51/fdX3dXtU4LHLzI9O7Rg+FX9vva0TOb3RdwbEoWFQpuZMZI0iD5MteCUzlMpY8clTe29ZsqqxfmlCtMaammVQNRZOoP2RtByAWvlext; search=6|1608797078502%7Crect%3D37.463887656692116%252C-122.00925505236816%252C37.34347864154035%252C-122.15327894763183%26rid%3D32999%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26sort%3Ddays%26z%3D1%26type%3Dhouse%252Ccondo%252Ctownhouse%252Capartment%26fs%3D0%26fr%3D1%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%09%0932999%09%09%09%09%09%09; _gat=1',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36'
    }

    def fetch(self, url, params):
        print('HTTP GET request to URL: %s' % url, end='')
        res = requests.get(url, params=params, headers=self.headers)
        print(' | Status code: %s' % res.status_code)
        
        return res
   
    def save_response(self, res):
        with open('res.html', 'w') as html_file:
            html_file.write(res)

    def load_response(self):
        html = ''
        
        with open('res.html', 'r') as html_file:
            for line in html_file:
                html += line
        
        return html
   
    def parse(self, html):
        content = BeautifulSoup(html, 'lxml')
        cards = content.findAll('article', {'class': 'list-card'})
        
        for card in cards:
            try:
                ba = card.find('ul', {'class': 'list-card-details'}).findAll('li')[1].text.split(' ')[0]
            except:
                ba = 'N/A'
            
            try:
                sqft = card.find('ul', {'class': 'list-card-details'}).findAll('li')[2].text.split(' ')[0]
            except:
                sqft = 'N/A'
            
            try:
                image = card.find('img')['src']
            except:
                image = 'N/A'

            self.results.append({
                'price': card.find('div', {'class': 'list-card-price'}).text,
                'address': card.find('address', {'class': 'list-card-addr'}).text,
                'bds': card.find('ul', {'class': 'list-card-details'}).findAll('li')[0].text.split(' ')[0],
                'ba': ba,
                'sqft': sqft,
                'image': image
            })
    
    def to_csv(self):
        with open('zillow1.csv', 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.results[0].keys())
            writer.writeheader()
            
            for row in self.results:
                writer.writerow(row)
        
    def run(self):
        for page in range(1, 5):
            params = {
                searchQueryState: {"pagination":{},"usersSearchTerm":"mountain view, ca","mapBounds":{"west":-122.15327894763183,"east":-122.00925505236816,"south":37.34347864154035,"north":37.463887656692116},"regionSelection":[{"regionId":32999,"regionType":6}],"isMapVisible":true,"filterState":{"fsba":{"value":false},"fsbo":{"value":false},"nc":{"value":false},"fore":{"value":false},"cmsn":{"value":false},"auc":{"value":false},"pmf":{"value":false},"pf":{"value":false},"fr":{"value":true},"ah":{"value":true}},"isListVisible":true,"mapZoom":13}" %page}
            }
            

            res = self.fetch('https://www.zillow.com/mountain-view-ca/rentals/', params)
            self.parse(res.text)

        self.to_csv()
        

if __name__ == '__main__':
    scraper = ZillowScraper()
    scraper.run()












