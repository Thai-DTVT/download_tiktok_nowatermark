from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def get_tiktok_video_href(keyword):
    url = f"https://www.tiktok.com/search?q={keyword}"
    
    
    options = Options()
    options.add_argument("--headless")  
    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get(url)
        
        
        driver.implicitly_wait(10)  
        
        
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        
        video_links = soup.find_all('a', class_='css-1yvkaiq-CanvasPlaceholder e19c29qe2')  
        
        if video_links:
            first_video_href = video_links[0]['href']
            full_video_href = f"https://www.tiktok.com{first_video_href}"
            return full_video_href
        else:
            print("Không tìm thấy video với từ khóa này.")
            return None
    
    except Exception as e:
        print(f"Lỗi khi lấy href của video TikTok: {e}")
    
    finally:
        driver.quit()  

keyword = "meo"
video_href = get_tiktok_video_href(keyword)
if video_href:
    print(f"Link của video TikTok với từ khóa '{keyword}':")
    print(video_href)
