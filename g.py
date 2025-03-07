import requests
import json

def send_request(prompt):
    url = "https://api.binjie.fun/api/generateStream"
    headers = {
        "authority": "api.binjie.fun",
        "method": "POST",
        "path": "/api/generateStream",
        "scheme": "https",
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "origin": "https://chat18.aichatos.xyz",
        "referer": "https://chat18.aichatos.xyz/",
        "sec-ch-ua": "\"Google Chrome\";v=\"105\", \"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"105\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
        "Content-Type": "application/json"
    }

    data = {
        "prompt": prompt,
        "userId": "#/chat/1711529530173",
        "network": True,
        "system": "",
        "withoutContext": False,
        "stream": False
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data), verify=True)
        response.raise_for_status()  # بررسی وضعیت پاسخ (اگر 4xx یا 5xx باشد خطا ایجاد می‌کند)

        if response.status_code == 200:
            try:
                # بررسی نوع محتوا (در صورتی که JSON باشد، آن را تجزیه می‌کنیم)
                if 'application/json' in response.headers.get('Content-Type', ''):
                    result = response.json()  # تجزیه پاسخ به فرمت JSON
                    print(result["text"])  # چاپ متن پاسخ
                else:
                    # اگر پاسخ JSON نباشد، به صورت متن خام چاپ می‌شود
                    print("پاسخ دریافتی: ", response.text)
            except json.JSONDecodeError:
                print("خطا در تجزیه پاسخ JSON")
                print(f"پاسخ دریافتی از سرور: {response.text}")  # چاپ پاسخ خام در صورت بروز خطا
        else:
            print(f"خطا: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"خطا در ارسال درخواست: {e}")

# دریافت ورودی از کاربر و درخواست مکرر
while True:
    prompt = input("لطفا سوال یا درخواست خود را وارد کنید: ")
    if prompt.lower() == 'خروج':
        print("خروج از برنامه...")
        break
    send_request(prompt)
