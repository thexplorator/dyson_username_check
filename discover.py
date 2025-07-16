import sys
import requests
import json

def main():
    if len(sys.argv) != 2:
        print(f"Uso: {sys.argv[0]} <email>")
        sys.exit(1)

    email = sys.argv[1]

    url = "https://api.dyson.pt/apiman-gateway/dyson/session/1.0/username_check"

    headers = {
        "Host": "api.dyson.pt",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:140.0) Gecko/20100101 Firefox/140.0",
        "Accept": "application/json",
        "Accept-Language": "pt-PT,pt;q=0.8,en;q=0.5,en-US;q=0.3",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Content-Type": "application/json",
        "Referer": "https://www.dyson.pt/",
        "x-csrf-token": "38EqqEVhbzHwnXb",
        "Origin": "https://www.dyson.pt",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "Connection": "keep-alive",
        "Cookie": "CSRF_TOKEN=38EqqEVhbzHwnXb;",
        "Priority": "u=0"
    }

    payload = {
        "email": email
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        print(f"Status Code: {response.status_code}")
        print("Resposta:")
        print(response.text)
    except requests.RequestException as e:
        print(f"Erro ao fazer o pedido: {e}")

if __name__ == "__main__":
    main()

