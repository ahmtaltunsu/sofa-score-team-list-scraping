from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

# Web driver'ı başlat
driver = webdriver.Chrome()
driver.maximize_window()

# Sayfayı yükle
driver.get("https://www.Takımın-Sofa-Score-Linki")
driver.execute_script("document.body.style.zoom='25%'")

# WebDriverWait nesnesini başlat
wait = WebDriverWait(driver, 10)
# Sayfanın tam olarak yüklenmesini bekle
time.sleep(5)

wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'sc-fqkvVR') and contains(@class, 'fSBPoD')]")))

# Sayfanın en altına kaydırma
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(5) # Sayfanın yüklenmesi için biraz daha bekleyin

# Oyuncuların bilgilerini toplama
players_data = []

# Oyuncu listesi için düzeltilmiş XPath
players = driver.find_elements(By.XPATH, "//div[contains(@class, 'sc-fqkvVR') and contains(@class, 'fSBPoD')]")

for player in players:
    try:
        # Göreli XPath kullanarak her bir oyuncunun isim bilgisini al
        name = player.find_element(By.XPATH, ".//div[@class='sc-gFqAkR efGspm']").text
        # Göreli XPath kullanarak her bir oyuncunun numara bilgisini al
        shirt_no = player.find_element(By.XPATH, ".//div[contains(@class, 'cRdApW')]").text
        country = player.find_element(By.XPATH, ".//span[contains(@class, 'sc-gFqAkR') and contains(@class, 'jWDedj')]").text
        position = player.find_element(By.XPATH, ".//div[contains(@class, 'sc-fqkvVR') and contains(@class, 'sc-dcJsrY') and contains(@class, 'eyfIZS') and contains(@class, 'eOzYQf')]/span").text
        players_data.append({
            'Name': name,
            'Number': shirt_no,
            'Nationality': country,
            'Position' : position
        })
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

# WebDriver'ı kapatma
driver.quit()

# Pandas DataFrame oluşturma

df_players = pd.DataFrame(players_data)
# DataFrame'i CSV dosyasına kaydetme
csv_file_path = '/Hedeflenen Dizin/dosya_adi.csv' #Kaydetmek istenilen dizin, dosya adı ve uzantısı
df_players.to_csv(csv_file_path, index=False, encoding='utf-8')

print("CSV dosyası başarıyla kaydedildi:", csv_file_path)