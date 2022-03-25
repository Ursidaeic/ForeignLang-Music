# YouTube API V3 comment downloader 
This is a tool to download all the comments and replies to a YouTube music video using Google's YouTube API V3 (note: at present, the API only supports the downloading of replies to top-level comments, not replies to replies). The vast majority of the code is taken from [hobogalaxy's script](https://github.com/ashleve/youtube_multi_video_comment_downloader/blob/master/yt-comment-scraper.py), however I have made a couple of changed regarding the package used to make the requests and also intergration into the wider project.

For this program you will need to create a developer key, which can be done by following the steps found [here](https://developers.google.com/youtube/v3/getting-started). This key will need to be supplied at the command line and has a limit of (roughly) 1 million comments per day.

Additionally, the url and video name will need to be placed in a .txt file in the same folder as the scraper_api.py file. In this folder, the video ID, artist name, and song name will need to be formatted as follows: videoId|ArtistName-SongName, eg. 0lapF4DQPKQ|BTS-BlackSwan.
