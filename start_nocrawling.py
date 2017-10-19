from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import re

def DownloadFile(url,local_filename):
    global content_length;
	try:
		head = requests.head(url)
		if  ('Content-Length' in str(head.headers)) and (int(head.headers['Content-Length']) < content_length):
			r = requests.get(url)
			f = open(local_filename, 'wb')
			for chunk in r.iter_content(chunk_size=512 * 1024): 
				if chunk: # filter out keep-alive new chunks
					f.write(chunk)
			f.close()
		else:
			print(str(head.headers))
	except:
		print('Didn\'t work with string :\n'+url)
	return 1


def GetGoogleLinks(google_site):
	tempsoup = BeautifulSoup(google_site,'html.parser')
	templinks = tempsoup.findAll('a');
	out = [];
	for el in templinks:
		# Ensure link is the one of multiples we want, make sure starts with http(s)
		if ('/url?q=' in str(el)) and ('webcache' not in str(el)) and (str(el)[16:20] == 'http') or (str(el)[16:19] == 'www'):
			# only print out starting letter (leave out "/url?q="
			temptext = str(el['href'])[7:];
			temptext = temptext.partition("/&sa")[0];
			out.append(temptext.partition("&sa")[0]);
	return out

def GetFiles(soup,field):
	global wav_counter,mp3_counter,mp4_counter;
	for el in soup:
		try:
			cur_string = el[field]
			# Find if type attribute is audio/wav 
			if ('.wav' in str(el)) : # and (el['type'] == 'audio/wav') :
				DownloadFile(el[field], wav_output_dir+'/'+str(wav_counter)+'.wav');
				print('wav') or ('.WAV' in str(el))
				print(el[field])
				wav_counter += 1;
			if ('.mp3' in str(el)):
				print('mp3') or ('.MP3' in str(el))
				print(el[field])
				DownloadFile(el[field], wav_output_dir+'/'+str(mp3_counter)+'.mp3');
				mp3_counter += 1;
			if ('.mp4' in str(el)) or ('.MP4' in str(el)):
				print('mp4')
				print(el[field])
				DownloadFile(el[field], video_output_dir+'/'+str(mp4_counter)+'.mp4');
				mp4_counter += 1;
			if ('.webm' in str(el)) or ('.WEBM' in str(el)):
				print('mp4')
				print(el[field])
				DownloadFile(el[field], video_output_dir+'/'+str(mp4_counter)+'.webm');
				mp4_counter += 1;	
		except:
			print 'no write'
			
search_term = 'trump+election+mp3+wav';
runs = 15; # Equals number of Google sites looked at.
content_length = 5621404;

wav_output_dir = 'E:/wavs/audio';	
video_output_dir = 'E:/wavs/video';	


search_start = 'http://www.google.at/search?q='+str(search_term);
links_ = list();

for i in range(runs):
	search_now = search_start + '&start=' + str(i*10);
	list_now   = GetGoogleLinks(requests.get(search_now).text);
	links_.extend([x for x in list_now]);
	time.sleep(2)

#ddgo_res = pd.read_json(requests.get(search_start).text);

wav_counter = 0;
mp3_counter = 0;
mp4_counter = 0;

for link in links_:
	print(link)
	try:
		r  = requests.get(link,headers={'Accept-Encoding': 'identity'});
	except:
		print('some error');
	data = r.text
	soup = BeautifulSoup(data,'html.parser')
	sources = soup.select('div source[src]');
	links = soup.select('link');
	GetFiles(links,'href');
	GetFiles(sources,'src');




		
		
## Todo:
## Implement Threading to parallelize
## 		
## base_url = "https://peal.io/soundboards/donald-trump";
		
		
		
		
		
		
		
		
		

