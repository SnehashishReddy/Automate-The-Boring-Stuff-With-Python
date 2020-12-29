import requests,bs4,os,shutil

URL = 'http://www.lefthandedtoons.com/'
page = requests.get(URL)
cwd = os.getcwd()
soup = bs4.BeautifulSoup(page.content, 'html.parser')
results = soup.find_all(class_ = 'comicimage')
time = soup.find_all(class_ = 'comictitlearea')
command = 'curl -O ' + results[0].get('src')
os.system(command)
file_name = ((results[0].get('src')).split('/'))[-1]
os.system('mv ' + cwd + '/' + file_name + ' ' + '~/Desktop/')