import requests

query = input("请输入一个你喜欢的明星:")

url = f"https://www.sogou.com/web?query={query}"

dic = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
}

resp = requests.get(url, headers=dic)

print(resp)
print(resp.text)
