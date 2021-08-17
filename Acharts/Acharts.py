import requests
from bs4 import BeautifulSoup
import argparse
import time
import random
import json

chart_data = []

def get_chart(url, fromweek, toweek):
    
    check_url = url+toweek
    url = url+fromweek
    
    week_data = {}
    
    
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
        "Accept-Encoding": "gzip, deflate, br", 
        "Accept-Language": "en,de;q=0.9,en-US;q=0.8,fr-FR;q=0.7,fr;q=0.6,es;q=0.5",  
        "authority": "acharts.co", 
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Research Project with the University of Birmingham (cxa643@student.bham.ac.uk)")
    }   
    
    r = requests.get(url, headers=headers)
    r.encoding = 'utf-8'
 
    e = r.status_code
    if e >= 400:
        if e == 400:
            print('Error', e, ': the request was not encoded correctly')
            exit()
        elif e == 404:
            if len(chart_data) == 0:
                print('Error', e, ': page not found. Ensure that the information you have supplied is valid and correctly formatted')
                exit()
            else:
                print("\nAcharts does not contain archive data for\n", toweek)
                return
        elif e == 410:
            print('Error', e, ': the page you have requested is missing/no longer exists')
            exit()    
        elif e >= 500:
            print('Error', e, ': there is a problem with the server')
            exit()
        else:
            print("Error", e, "returned")
            exit()
    
    check_r = requests.get(check_url, headers=headers)
    if check_r.status_code == 404:
        print("The week you asked to scrape back to is not contained within the Acharts archive")
        exit()
        
    week_data.update({fromweek: {}})
    
    soup = BeautifulSoup(r.text, 'html.parser')
    for item in soup.select("td"):
        if item['class'][0] == 'cPrinciple':
            song = item.a.span.get_text()
            e = item.find("span", { "class" : "Sub" })
            if e is not None:
                results = e.find("span",{"itemprop":"name"})
                try:
                    artist = results.get_text()
                except AttributeError:
                    break
                week_data[fromweek].update({song: artist})
    chart_data.append(week_data)
if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(add_help=False)
    required = parser.add_argument_group("Required arguments")
    optional = parser.add_argument_group("Optional arguments")
    required.add_argument("--url", '-u', help="URL of chart, eg. -u https://acharts.co/canada_singles_top_100")
    required.add_argument("--toweek", '-t', help="Scrape charts back to specified week of the year. The script will scrape up to the week after the specified week. Format=YYYY/WW")
    optional.add_argument("--fromweek", '-f', help="Scrape charts starting from specified week of the year. If left blank, scraping will start from the most recent week. Format=YYYY/WW.")
    optional.add_argument("--output", '-o', help="Output file name")
    optional.add_argument("--help", '-h', help="Help", action='help')
    args = parser.parse_args()

    x = time.time() - 604800
    gmweek = time.gmtime(x)
    fromweek = "{}/{}".format(time.strftime("%Y", gmweek),time.strftime("%U", gmweek))
    
    if args.fromweek:
        fromweek = args.fromweek

    toweek = args.toweek
    
    output = "Charts_data"
    if args.output:
        output = args.output
    
    url = args.url
        

    
    #-----------------------------------------------------------------------------------#
    if url[-1] != "/":
        url = url+"/"
        
    weeklist = ["01", "02", "03", "04", "05", "06", "07", "08", "09"]
    for x in range(10, 53):
        x = str(x)
        weeklist.append(x)
    
    while toweek != fromweek:
        print("Scraping week of:", fromweek, end="\r")
        get_chart(url, fromweek, toweek)
        with open (f'Data/{output}.json', "w", encoding='utf8') as f:
            json.dump(chart_data, f, ensure_ascii=False)
            
        
        splitdate = fromweek.split("/")   #separates supplied date into week and year  
        year = splitdate[0]     
        year = int(year)
        week = splitdate[1]

        w = weeklist.index(week) 

        if w == 0:
            year-=1
            week = weeklist[len(weeklist)-1]
        else:
            week = weeklist[w-1]

        year = str(year)
        fromweek = year + "/" + week
        
        time.sleep(random.randint(3, 5))

        
