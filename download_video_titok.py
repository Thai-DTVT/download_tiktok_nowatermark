import re
import random
import requests

def download_tiktok_video(url):
    endpoint = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/index"
    headers = {
        "x-rapidapi-key": "3f80d2c0cdmshdaa67aae6ea1adap1c1308jsn4a47d1ecb2d2",
        "x-rapidapi-host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"
    }
    
 
    params = {"url": url}
    try:
        
        response = requests.get(endpoint, headers=headers, params=params)
        response.raise_for_status()  
             
        data = response.json()   
        print(f"Response for URL {url}: {data}")
        
        video_url = None
         
        if 'video' in data and data['video']:
            video_url = data['video'][0]
        elif 'OriginalWatermarkedVideo' in data and data['OriginalWatermarkedVideo']:
            video_url = data['OriginalWatermarkedVideo'][0]
        
        if video_url:
            
            output_name = f'video/{random.randrange(1, 1000)}.mp4'
            
            r = requests.get(video_url)
            with open(output_name, 'wb') as f:
                f.write(r.content)
            
            print(f"Downloaded video from URL: {url} and save {output_name}")
        else:
            print(f"No video found : {url}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error downloading video from URL: {url}, {e}")

def download_videos_from_file(file_path):
    with open(file_path, 'r') as file:
        urls = file.readlines()
    
    for url in urls:
        url = url.strip() 
        if url.startswith('http'):  
            download_tiktok_video(url)
        else:
            print(f"Skip invalid URL: {url}")


file_path = 'list_of_urls.txt'  
download_videos_from_file(file_path)
