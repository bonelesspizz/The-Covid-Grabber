import tkinter as tk
import tkinter.font as tkFont
import requests
from bs4 import BeautifulSoup

def get_info():
    country = country_input.get().lower()
    if country == "south korea" or country == "southkorea":
        country = "S. Korea"
    elif country == "uk" or country == "usa":
        country = country.upper()
    else:
        country = country.title()
    
    html = requests.get("https://covid19statistics.org/")
    soup = BeautifulSoup(html.text,'html.parser')
    info = soup.find(id=country)
    info_list = info.find_all("td")

    total_cases_str = f"Total cases: {str(info_list[1])[4:-5]}"
    todays_cases_str = f"Today's cases: {str(info_list[2])[4:-5]}"
    total_deaths_str = f"Total deaths: {str(info_list[3])[4:-5]}"
    todays_deaths_str = f"Todays deaths: {str(info_list[4])[22:-5]}"
    recovered_str = f"Recovered: {str(info_list[5])[4:-5]}"
    critical_str = f"Critical: {str(info_list[6])[4:-5]}"

    total_cases_label['text'] = total_cases_str
    todays_cases_label['text'] = todays_cases_str
    total_deaths_label['text'] = total_deaths_str
    todays_deaths_label['text'] = todays_deaths_str
    recovered_label['text'] = recovered_str
    critical_label['text'] = critical_str


root = tk.Tk()
root.resizable(0, 0)
root.title("The Covid Grabber")

fontType = tkFont.Font(family='Lucida Grande',size=15)

HEIGHT = 600
WIDTH = 800

bg = tk.PhotoImage(file="background.png")

canvas = tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()
canvas.create_image(0,0, image=bg, anchor="nw")

input_frame = tk.Frame(root,bg='#ff4444',bd=1)
input_frame.place(relx=0.1,rely=0.08,relwidth=0.8,relheight=0.06)

country_input = tk.Entry(input_frame,bg='white')
country_input.place(relx=0.005,rely=0.1,relwidth=0.775,relheight=0.8)

get_weather = tk.Button(input_frame,text="Get info",bg='white', command=get_info)
get_weather.place(relx=0.995,rely=0.1,relwidth=0.2,relheight=0.8,anchor='ne')

output_frame = tk.Frame(root,bg='#ff4444')
output_frame.place(relx=0.1,rely=0.18,relwidth=0.8,relheight=0.72)

total_cases_label = tk.Label(output_frame,bg='white',font=fontType)
total_cases_label.place(relx=0.02,rely=0.05,relwidth=0.95,relheight=0.15)

todays_cases_label = tk.Label(output_frame,bg='white',font=fontType)
todays_cases_label.place(relx=0.02,rely=0.20,relwidth=0.95,relheight=0.15)

total_deaths_label = tk.Label(output_frame,bg='white',font=fontType)
total_deaths_label.place(relx=0.02,rely=0.35,relwidth=0.95,relheight=0.15)

todays_deaths_label = tk.Label(output_frame,bg='white',font=fontType)
todays_deaths_label.place(relx=0.02,rely=0.49,relwidth=0.95,relheight=0.15)

recovered_label = tk.Label(output_frame,bg='white',font=fontType)
recovered_label.place(relx=0.02,rely=0.64,relwidth=0.95,relheight=0.15)

critical_label = tk.Label(output_frame,bg='white',font=fontType)
critical_label.place(relx=0.02,rely=0.79,relwidth=0.95,relheight=0.15)

root.mainloop()