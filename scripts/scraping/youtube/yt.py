import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Enter your API key here
API_KEY = "YOUR_API_KEY"

# Authenticate the app
credentials, _ = google.auth.default(scopes=["https://www.googleapis.com/auth/youtube.readonly"])
youtube = build("youtube", "v3", credentials=credentials)

# Search for trending YouTube videos
request = youtube.videos().list(
    part="snippet",
    chart="mostPopular",
    regionCode="BD",
    maxResults=25,
    key=API_KEY
)
response = request.execute()

# Print the title of each video
for video in response["items"]:
    print(video["snippet"]["title"])

#pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
# 