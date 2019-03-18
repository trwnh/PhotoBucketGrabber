import requests
from urllib.parse import unquote
from pathlib import Path

def main():
  errorCount = 0
  with open('photo.txt', 'r') as file: # edit
    lines = file.readlines()
  for line in lines:
    url = line.strip()
    download(url)
  print("Done! Processed "
        + str(len(lines)) + " files with "
        + str(errorCount) + " errors.",
        flush=True
       )

def download(url):
  global errorCount
  r = requests.get(url, headers={'referer': 'http://s.photobucket.com'})
  if r.status_code == 200:
    filename = unquote(strip(url))
    path = Path(filename)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(filename, 'wb') as file:
      file.write(r.content)
      print("WRITE: " + filename, flush=True)
  else:
    print("ERROR: " + url, flush=True)
    errorCount += 1

def strip(url):
  prefix = "http://i604.photobucket.com/albums/tt122/PaperMarioBlog/" # edit
  return url[len(prefix):]

main()
