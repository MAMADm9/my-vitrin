import requests
import re
import urllib.parse

CHANNELS = ['TEST_HTM', 'isor1n', 'planB_net'] 

def get_configs():
    found_configs = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }

    for channel in CHANNELS:
        try:
            url = f"https://t.me/s/{channel}"
            response = requests.get(url, headers=headers, timeout=15)
            
            # پیدا کردن تمام لینک‌هایی که با vless, vmess, trojan, ss شروع می‌شن
            # این مدل Regex خیلی سخت‌گیرتر و دقیق‌تره
            raw_matches = re.findall(r"(?:vless|vmess|trojan|ss)://[^\s<\"']+", response.text)
            
            for m in raw_matches:
                # تمیز کردن لینک از کدهای اضافه HTML (مثل &amp;)
                clean_config = urllib.parse.unquote(m).split('<')[0].split('"')[0].split('&')[0].strip()
                
                # اگه لینک سالم بود و تکراری نبود، اضافه‌اش کن
                if clean_config and clean_config not in [c.split('#')[0] for c in found_configs]:
                    found_configs.append(f"{clean_config}#{channel}")
            
            print(f"✅ چنل {channel} اسکن شد.")
        except Exception as e:
            print(f"❌ خطا در {channel}: {e}")
            
    # ذخیره در فایل
    with open("data.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(found_configs))
    print(f"--- پایان عملیات. تعداد کل: {len(found_configs)} ---")

if __name__ == "__main__":
    get_configs()
    
