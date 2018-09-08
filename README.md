# reddit2tumblr
Takes posts from Reddit and queues them to your tumblr blog

Uses posts subreddit to give Tumblr post specific tags

This was based off of and inspired by [HourlyMemes (RIP)](https://hourlymemes.tumblr.com/)

reddit2tumblr supports:
- Photos
- GIFs (Gfycat and non gifv Imgur)
- Videos / GIFV (Youtube and v.reddit currently)

# Starting
1. Getting dependancies
   - [praw](https://github.com/praw-dev/praw)
   - [imgur_downloader](https://github.com/jtara1/imgur_downloader)
   - [pytumblr](https://github.com/tumblr/pytumblr)
   - [youtube-dl](https://github.com/rg3/youtube-dl)
2. Setting up applications
   - [Register Tumblr application](https://www.tumblr.com/oauth/register)
     - Write down your secrets
   - [Register Reddit Application](https://github.com/reddit-archive/reddit/wiki/OAuth2)
3. Editing settings
   - Open secrets_reddit and replace the lines with the corresponding secret / token
   - Open secrets_tumblr and replace the lines with the corresponding secret / token
   - Open reddit2tumblr.py in your preferred text editor
   - Edit settings
      - Subreddit(s)
      - Minnimum score
      - Post limit
      - Post sort
      - Delete images folder when done
      - Blogname
   - Set up your tags and and make tag categories
