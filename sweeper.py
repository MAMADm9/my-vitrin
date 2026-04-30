import requests
import re
import datetime

CHANNELS = ['TEST_HTM', 'isor1n', 'planB_net'] 

def get_configs():
    found_configs = []
    headers = {'User-Agent': 'Mozilla/5.0'}

    for channel in CHANNELS:
        try:
            url = f"https://t.me/s/{channel}"
            response = requests.get(url, headers=headers, timeout=15)
            # پیدا کردن پروتکل‌های مختلف
            raw_matches = re.findall(r"(?:vless|vmess|trojan|ss)://[^\s<\"']+", response.text)
            for m in raw_matches:
                clean_config = m.split('<')[0].split('"')[0].split('&')[0].strip()
                if clean_config not in [c.split('#')[0] for c in found_configs]:
                    found_configs.append(f"{clean_config}#{channel}")
        except: continue
            
    # ذخیره در فایل به همراه زمان آپدیت برای اجبار گیت‌هاب به تغییر
    with open("data.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(found_configs))
    
    print(f"Updated at {datetime.datetime.now()}")

if __name__ == "__main__":
    get_configs()
    
