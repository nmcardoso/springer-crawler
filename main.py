import requests
import re
import os

def download(url, output):
  r = requests.get(url)

  with open(output, 'wb') as f:
    f.write(r.content)
  
def get_title(url):
  r = requests.get(url, allow_redirects=True)
  match = re.search(r'<title>(.*?)</title>', str(r.content))
  title = match.group(1)
  return title.split('|')[0].strip()

def main():
  print('Starting...')

  if not os.path.exists('outputs'):
    os.mkdir('outputs')

  with open('links.txt', 'r') as f:
    txt = ' '.join(f.readlines())
    ids = re.findall(r'doi\.org\/([\d\.]+\/[\d\w-]+)', txt)
    
    for i, _id in enumerate(ids):
      title = get_title(f'http://doi.org/{_id}')
      print(f'[{i + 1}/{len(ids)}]: Downloading {title}') 
      download(f'https://link.springer.com/content/pdf/{_id}.pdf', f'outputs/{title}.pdf')

if __name__ == '__main__':
  main()