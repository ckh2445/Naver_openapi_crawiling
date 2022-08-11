import requests
import openpyxl

class Naver_shop_crawling():
    def __init__(self):
        self.client_id = "8DGCP3FB3cB3kHuHiUXK"
        self.client_secret = "v74NqCsiJd"
        self.header_params = {"X-Naver-Client-Id": self.client_id, "X-Naver-Client-Secret": self.client_secret}
        self.Search = ""
        
    def get_data(self,Search:str, Start:int, Display:int):
        self.naver_open_api = "https://openapi.naver.com/v1/search/shop.json?query=" + Search + "&display=" + str(Display) + "&start=" + str(Start)
        self.res = requests.get(self.naver_open_api, headers=self.header_params)
        self.Search = Search
        if self.res.status_code == 200:
            return self.res.json()
            
        else:
            print("error")
    
    def get_name(self):
        return self.Search
        
    def save(self,filename:str,lists:list):
        self.excel_file = openpyxl.Workbook()
        self.excel_sheet = self.excel_file.active
        self.excel_sheet.column_dimensions['A'].width = 10
        self.excel_sheet.column_dimensions['B'].width = 100
        self.excel_sheet.column_dimensions['C'].width = 100
        self.title = ["번호","제품명","링크"]
        
        self.excel_sheet.append(self.title)
        self.excel_sheet.title = filename
        
        for item in lists:
            self.excel_sheet.append(item)
            
        self.excel_file.save(filename)
        self.excel_file.close()
            
            
if __name__ == "__main__":
    openapi = Naver_shop_crawling()
    idx = 1
    lists = list()
    
    for x in range(10):
        data = openapi.get_data("삼성휴대폰",Start= x+idx, Display = 100)
        for num, item in enumerate(data['items']):
            lists.append([idx, item['title'], item['link']])
            idx += 1
            
    openapi.save(openapi.get_name()+".xlsx", lists)