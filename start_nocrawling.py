
from bs4 import BeautifulSoup
#import requests
import pandas as pd
from selenium import webdriver

def DownloadFile(url,local_filename):
    #local_filename = url.split('/')[-1]
    r = requests.get(url)
    f = open(local_filename, 'wb')
    for chunk in r.iter_content(chunk_size=512 * 1024): 
        if chunk: # filter out keep-alive new chunks
            f.write(chunk)
    f.close()
    return 1
	
	
wav_output_dir = 'E:\wavs';	
	
	
#r  = requests.get("https://peal.io/soundboards/donald-trump");
#data = r.text
driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
base_url = "https://peal.io/soundboards/donald-trump";

driver.get(base_url)
pageSource = driver.page_source


soup = BeautifulSoup(pageSource,'html.parser')


sources = soup.select('div source[src]');

wav_counter = 0;
for el in sources:
	if el['type'] == 'audio/wav':
		DownloadFile(el['src'], wav_output_dir+'/'+str(wav_counter)+'.wav');
		wav_counter += 1;
	if el['type'] == 'audio/mp3':
		print('mp3')






