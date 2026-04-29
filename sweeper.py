import requests
import re

# آیدی‌های نهایی که گفتی
CHANNELS = ['TEST_HTM', 'isor1n', 'planB_net'] 

def get_configs():
    found_configs = []
    headers = {'User-Agent': 'Mozilla/5.0'}

    for channel in CHANNELS:
        try:
            url = f"https://t.me/s/{channel}"
            response = requests.get(url, headers=headers, timeout=10)
            # پیدا کردن لینک‌های کانفیگ
            pattern = r"(vless|vmess|trojan|ss)://[^\s<\"' ]+"
            matches = re.findall(pattern, response.text)
            for m in matches:
                clean = m.split('<')[0].split('"')[0]
                if clean not in [c.split('#')[0] for c in found_configs]:
                    found_configs.append(f"{clean}#{channel}")
        except: continue
            
    with open("data.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(found_configs))

if __name__ == "__main__":
    get_configs()
