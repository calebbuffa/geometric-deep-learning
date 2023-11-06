import requests

URLS = (
  "https://github.com/calebbuffa/geometric-deep-learning/raw/main/data/test.ply",
  "https://github.com/calebbuffa/geometric-deep-learning/raw/main/data/train.ply"
)

def main():
  for url in URLS:
    resp = requests.get(url)
    with open(url.split("/")[-1], "wb") as f:
      f.write(resp.content)

if __name__ == "__main__":
  main()
