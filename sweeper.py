import requests
import re

# آیدی‌های چنل‌ها
CHANNELS = ['TEST_HTM', 'isor1n', 'planB_net'] 

def get_configs():
    found_configs = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    for channel in CHANNELS:
        try:
            url = f"https://t.me/s/{channel}"
            response = requests.get(url, headers=headers, timeout=15)
            
            # رنکس (تور) قوی‌تر: 
            # دنبال vless/vmess/trojan/ss می‌گرده و تا جایی که به کاراکتر غیرمجاز (مثل < یا ") نرسه ادامه می‌ده
            pattern = r"(vless|vmess|trojan|ss|vtt)://[a-zA-Z0-9\-\.\_\~\:\/\?\#\[\]\@\!\$\&\'\(\)\*\+\,\;\=\%]+"
            matches = re.findall(pattern, response.text)
            
            for m in matches:
                # پاکسازی نهایی (جلوگیری از ورود کدهای HTML احتمالی)
                clean_config = m.replace('<', '').replace('"', '').replace("'", '').strip()
                
                # جلوگیری از تکراری شدن
                if clean_config not in [c.split('#')[0] for c in found_configs]:
                    found_configs.append(f"{clean_config}#{channel}")
            
            print(f"✅ {channel} چک شد.")
        except Exception as e:
            print(f"❌ خطا در {channel}: {e}")
            
    with open("data.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(found_configs))

if __name__ == "__main__":
    get_configs()
    
