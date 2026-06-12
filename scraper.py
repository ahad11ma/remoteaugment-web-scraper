import requests
from bs4 import BeautifulSoup
import csv

# 1. Target URL jahan services list hain
url = "https://remoteaugment.com"  # Agar alag se /services page ho to wo lagayein

# 2. Headers lagana zaroori hai taake website ko lage koi real browser request kar raha hai
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

print("Website se data fetch ho raha hai...")

try:
    # 3. Website ko request bhejna
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        print("Website kamyabi se khul gayi! Ab data extract kar rahe hain...\n")
        
        # HTML parse karna
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Note: Yeh HTML tags aur classes website ke design ke mutabiq change ho sakti hain.
        # Biasanya services 'div' tags mein hoti hain jin ki koi class hoti hai jaise 'service-card' ya 'service-box'
        services_list = []
        
        # Chalein website par maujood standard headings (h3 ya h4) ko target karte hain jahan service names hote hain
        # Hum pooray service section ko dhoondne ki koshish kar rahe hain
        services = soup.find_all(['h3', 'h4']) # Ye script page ki headings uthaye gi
        
        for service in services:
            service_name = service.text.strip()
            
            # Agar heading ke baad koi paragraph (<p>) hai, to wo uski description hogi
            next_element = service.find_next('p')
            service_desc = next_element.text.strip() if next_element else "No description available"
            
            # Sirf tab add karein jab text khali na ho aur relevant lagay
            if len(service_name) > 3:
                services_list.append({
                    "Service Name": service_name,
                    "Description": service_desc
                })
        
        # 4. Data ko Console par dikhana
        for idx, item in enumerate(services_list, 1):
            print(f"{idx}. {item['Service Name']}")
            print(f"   Detail: {item['Description']}\n" + "-"*50)
            
        # 5. Data ko CSV (Excel) file mein save karna
        with open('remoteaugment_services.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["Service Name", "Description"])
            writer.writeheader()
            writer.writerows(services_list)
            
        print(f"\n Mubarak ho! Total {len(services_list)} services ka data 'remoteaugment_services.csv' mein save ho gaya hai.")

    else:
        print(f"Website access nahi ho saki. Status Code: {response.status_code}")

except Exception as e:
    print(f"Koi error aya hai: {e}")