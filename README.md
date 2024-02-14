# YouTube Video Downloader

This Python application is built using Streamlit and allows users to download YouTube videos by entering the video's URL and selecting the desired quality and file type.

## Features

- User interface created with Streamlit to input video URL and select options.
- Uses an external API to fetch download links for YouTube videos.
- Provides video quality selection such as 360p, 480p, 720p, and 1080p.
- Allows users to choose the file type; currently supports MP4 and WEBM formats.
- Includes a download button which redirects users to the direct download URL.

## Usage

1. Run the application using Streamlit.
   ```sh
   streamlit run main.py
   ```

2. A web interface will open where you input the URL for the YouTube video you wish to download.

3. Select the desired quality for the video from the dropdown menu.

4. Choose the file type you prefer for the download.

5. Click the "Download" button, and you will be redirected to a new tab where the video can be downloaded directly.

## External API Integration

- The application utilizes the `youtube86.p.rapidapi.com` API to resolve video URLs to downloadable media files.
- API requests include necessary headers: Content-Type, X-Forwarded-For, X-RapidAPI-Key, and X-RapidAPI-Host.

## Security Notes

- This application contains a hardcoded API key, which is generally not recommended. For production applications, it's advisable to use environment variables or secret management services to handle API keys securely.
- The `X-Forwarded-For` header is also hardcoded which might be for testing purposes but should not be included like this in a production environment.

## Requirements

Dependencies required to run the application are listed in the `requirements.txt`, which can be installed using:
```sh
pip install -r requirements.txt
```

## Development Notes

- Streamlit's simplicity allows for rapid development of data applications with minimal setup.
- The `unsafe_allow_html` parameter is enabled in Streamlit markdown functions, which can pose a security risk if used with untrusted input.
- Function `download_video(url)` handles the API request and returns a dictionary with download URLs.

## Known Limitations

- This tool's availability is dependent on the external API service.
- Not handling potential API errors such as rate limits or video unavailability in the current implementation.

## Future Improvements

- Implement error handling for API responses.
- Remove hardcoded API keys and headers for enhanced security.
- Extend functionality to support audio-only downloads or additional file formats.
- Add capability to display previews or additional metadata of the videos. 

**Developer**: Remember to review and ensure that sensitive data like API keys are stored securely before deploying or sharing the code. Additionally, check and handle any potential API changes or data privacy concerns that might arise with the use of external services.
