
from bs4 import BeautifulSoup
import requests
	
def DownloadFile(url,local_filename):
    #local_filename = url.split('/')[-1]
    r = requests.get(url)
    f = open(local_filename, 'wb')
    for chunk in r.iter_content(chunk_size=512 * 1024): 
        if chunk: # filter out keep-alive new chunks
            f.write(chunk)
    f.close()
    return 1
	
	
r  = requests.get("http://www.soundboard.com/sb/Donald_Trump_audio_clips");
data = r.text
soup = BeautifulSoup(data,'html.parser')

#soup.select('div source[src]')[0]['src']
sources = soup.select('div source[src]');

wav_counter = 0;
for el in sources:
	if el['type'] == 'audio/wav':
		DownloadFile(el['src'],'wav/'+str(wav_counter)+'.wav');
		wav_counter += 1;
	if el['type'] == 'audio/mp3':
		print('mp3')

