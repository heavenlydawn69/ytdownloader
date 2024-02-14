import streamlit as st
import os
# from dotenv import load_dotenv
import requests

# def configure():
#     load_dotenv()

rapid_api_key = os.getenv('RAPID_API_KEY')

def download_video(url):
    # configure()
    api_url = "https://youtube86.p.rapidapi.com/api/youtube/links"
    headers = {
        "content-type": "application/json",
        "X-Forwarded-For": "70.41.3.18",
        "X-RapidAPI-Key": rapid_api_key,
        "X-RapidAPI-Host": "youtube86.p.rapidapi.com"
    }
    payload = { "url": url }
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

st.title('YouTube Video Downloader')

url = st.text_input('Enter the URL of the YouTube video')

select_quality = ['360', '480', '720', '1080']
quality = st.selectbox('Select Quality', select_quality)

select_name = ['MP4', 'WEBM']
typeOffile = st.selectbox('Select Type', select_name)

if url:
    result = download_video(url)
    if 'urls' in result[0]:
        for video in result[0]['urls']:
            if video['quality'] == quality and video['name'] == typeOffile and video['isBundle'] == True:
                video_url = video['url']
                # st.markdown(video_url, unsafe_allow_html=True)
                if st.button('Download'):
                    st.markdown(f'<a href="{video_url}" target="_blank">Click Here!</a>', unsafe_allow_html=True)
