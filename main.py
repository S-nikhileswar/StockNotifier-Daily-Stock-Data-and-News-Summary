import smtplib
from tkinter import *
import requests

class mail:
    def __init__(self):
        self.my_email="stocknotificationforu@gmail.com"
        self.password="lbyvoiphhrgcbbpn"
    def send_mail(self):
        self.connection = smtplib.SMTP("smtp.gmail.com")
        self.connection.starttls()
        self.connection.login(user=self.my_email,password=self.password)
        self.others_mail=d.user_mail
        self.final = f'''subject:{i.STOCK_NAME} data on {i.yesterday_date}\n\nOpen  : {i.yesterday_opening_price}\nHigh  : {i.yesterday_highest_price}\nLow   : {i.yesterday_lowest_price}\nClose : {i.yesterday_closing_price}\nVolume: {i.yesterday_volume}\n\nOne-Day Percentage increase or decrease : {i.diff_percentage}\nOne-Month Percentage increase or decrease : {i.one_month_percentage_difference}\nThree-Month Percentage Increase or Decrease : {i.three_month_percentage_difference}'''
        self.connection.sendmail(from_addr=self.my_email,to_addrs=self.others_mail,msg=self.final)
        self.connection.close()
        

class display: 
    def __init__(self):
        self.THICK_GREEN = "#16423C"
        self.MEDIUM_GREEN = "#6A9C89"
        self.LIGHT_GREEN = "#C4DAD2"
        self.WHITE = "#E9EFEC"
        self.RED = "#B8001F"
        
    def button_clicked(self):
        self.company_code = self.input_company_code.get()
        self.company_name = self.input_company_name.get()
        self.user_mail = self.input_user_mail.get()
        
    def features(self):
        self.window = Tk()
        self.window.title("Stock_info")
        self.window.minsize(width=700,height=250)
        self.window.config(padx = 100,pady = 50,bg=self.LIGHT_GREEN)

        self.title_label = Label(text="StockReport",fg=self.THICK_GREEN,bg=self.LIGHT_GREEN,font=("Courier",25,"bold"))
        self.title_label.grid(column=1,row=0)

        self.company_code = Label(text="Enter Company Code",fg=self.MEDIUM_GREEN,bg=self.LIGHT_GREEN,font=("Courier",15,"bold"))
        self.company_code.grid(column=0,row=1)
        self.line1 = Label(text="----------------->",fg=self.THICK_GREEN,bg=self.LIGHT_GREEN,font=("Courier",15,"bold"))
        self.line1.grid(column=1,row=1)
        self.input_company_code = Entry(width=50,bg=self.WHITE,bd=0,font=("Calibri",11,"bold"),justify="center")
        self.input_company_code.grid(column=2,row=1)

        self.company_name = Label(text="Enter Company Name",fg=self.MEDIUM_GREEN,bg=self.LIGHT_GREEN,font=("Courier",15,"bold"))
        self.company_name.grid(column=0,row=2)
        self.line2 = Label(text="----------------->",fg=self.THICK_GREEN,bg=self.LIGHT_GREEN,font=("Courier",15,"bold"))
        self.line2.grid(column=1,row=2)
        self.input_company_name = Entry(width=50,bg=self.WHITE,bd=0,font=("Calibri",11,"bold"),justify="center")
        self.input_company_name.grid(column=2,row=2)

        self.user_mail = Label(text="Enter Mail ID",fg=self.MEDIUM_GREEN,bg=self.LIGHT_GREEN,font=("Courier",15,"bold"))
        self.user_mail.grid(column=0,row=3)
        self.line3 = Label(text="----------------->",fg=self.THICK_GREEN,bg=self.LIGHT_GREEN,font=("Courier",15,"bold"))
        self.line3.grid(column=1,row=3)
        self.input_user_mail = Entry(width=50,bg=self.WHITE,bd=0,font=("Calibri",11,"bold"),justify="center")
        self.input_user_mail.grid(column=2,row=3)

        self.button = Button(text="Enter",command=self.button_clicked)
        self.button.grid(column=1,row=4)

        self.window.mainloop()

class information:
    def __init__(self):
        self.STOCK_NAME = (d.company_code)+".BSE"
        self.COMPANY_NAME = d.company_name
        
        self.STOCK_ENDPOINT="https://www.alphavantage.co/query?"
        self.NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

        self.STOCK_API_KEY="P59CV50I95O8V2IW"
        self.NEWS_API_KEY = "4c02993474af499793355edfa0890474"

    def yesterday(self):
        #Get yesterday's closing stock price
        self.stock_params={
            "function":"TIME_SERIES_DAILY",
            "symbol":self.STOCK_NAME,
            "apikey":self.STOCK_API_KEY,
            }
        self.response = requests.get(self.STOCK_ENDPOINT,params=self.stock_params)
        self.data = self.response.json()['Time Series (Daily)']
        self.data_list = [value for (key,value) in self.data.items()]
        self.date_list = [key for (key,value) in self.data.items()]
        self.yesterday_data = self.data_list[0]

        #Get the yesterday's date
        self.yesterday_date = self.date_list[0]
        #Get the yesterday's open price
        self.yesterday_opening_price = self.yesterday_data["1. open"]
        #Get the yesterday's high price
        self.yesterday_highest_price = self.yesterday_data["2. high"]
        #Get the yesterday's low price
        self.yesterday_lowest_price = self.yesterday_data["3. low"]
        #Get the yesterday's close price
        self.yesterday_closing_price = self.yesterday_data["4. close"]
        #Get the yesterday's volume
        self.yesterday_volume = self.yesterday_data["5. volume"]
        
        
        
        #Get 1Day Percentage Increase or Decrease in Price
        self.day_before_yesterday_data = self.data_list[1]
        self.day_before_yesterday_closing_price = self.day_before_yesterday_data["4. close"]
        self.difference = float(self.yesterday_closing_price) - float(self.day_before_yesterday_closing_price)
        self.diff_percentage = int((self.difference / float(self.day_before_yesterday_closing_price))*10000)/100

        #Get 1Month Percentage Increase or Decrease in Price
        self.one_month_before_data = self.data_list[21]
        self.one_month_before_closing_price = self.one_month_before_data["4. close"]
        self.one_month_difference = float(self.yesterday_closing_price) - float(self.one_month_before_closing_price)
        self.one_month_percentage_difference = int((self.one_month_difference/float(self.one_month_before_closing_price))*10000)/100

        #Get 3Month Percentage Increase or Decrease in Price
        self.three_month_before_data = self.data_list[63]
        self.three_month_before_closing_price = self.three_month_before_data["4. close"]
        self.three_month_difference = float(self.yesterday_closing_price) - float(self.three_month_before_closing_price)
        self.three_month_percentage_difference = int((self.three_month_difference/float(self.three_month_before_closing_price))*10000)/100

           
        self.news_params = {
            "apiKey" : self.NEWS_API_KEY,
            "qInTitle" : self.COMPANY_NAME,
            }
        self.news_response = requests.get(self.NEWS_ENDPOINT,params=self.news_params)
        self.articles = self.news_response.json()["articles"]
        self.three_articles = self.articles[:3]
        self.formatted_articles = [f"Headline : {article['title']}.\nBrief : {article['description']}" for article in self.three_articles]
        self.news = ""
        for i in self.formatted_articles:
            self.news+=i
                        

d=display()
d.features()
i=information()
i.yesterday()
m=mail()
m.send_mail()

