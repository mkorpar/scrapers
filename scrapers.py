from urllib.request import urlopen
import http.client, urllib, os, datetime, time

url_base='https://www.hep.hr/ods/bez-struje/19?dp=zagreb&el=ZG&datum='
cache_file = '/data/used_dates'

def scrape_hep():
  open(cache_file, 'a', encoding='utf-8').close()
  for i in range(7):
    d=(datetime.date.today() + datetime.timedelta(days=i)).strftime('%d.%m.%Y')
    page = urlopen(url_base + d)
    html_bytes = page.read()
    html = html_bytes.decode('utf-8')
    if 'ogrizo' in html.lower() and d not in open(cache_file, 'r', encoding='utf-8').read():
      print(d)
      conn = http.client.HTTPSConnection("api.pushover.net:443")
      conn.request("POST", "/1/messages.json",
      urllib.parse.urlencode({
        'token': os.getenv('PUSHOVER_APP_TOKEN'),
        'user': os.getenv('PUSHOVER_USER_TOKEN'),
        'message': 'Check date ' + d,
        'title': 'HEP',
      }), { "Content-type": "application/x-www-form-urlencoded" })
      conn.getresponse()
      open(cache_file, 'a', encoding='utf-8').write(d + '\n')

def main_loop():
  while True:
    print(str(datetime.datetime.now()) + " scraping")
    scrape_hep()
    time.sleep(1800) # 1800 seconds = 30 minutes

if __name__ == "__main__":
  main_loop()
