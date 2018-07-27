# reddit2tumblr
Takes posts from Reddit and queues them to your tumblr blog

Uses posts subreddit to give Tumblr post specific tags

This was based off of and inspired by [HourlyMemes (RIP)](https://hourlymemes.tumblr.com/)

reddit2tumblr supports:
- Photos
- GIFs (**only** Imgur currently)
- Videos / GIFV (**only** YouTube currently)

# Starting
1. Getting dependancies
   - [praw](https://github.com/praw-dev/praw)
   - [imgur_downloader](https://github.com/jtara1/imgur_downloader)
   - [pytumblr](https://github.com/tumblr/pytumblr)
   - [pytube](https://github.com/nficano/pytube)
2. Setting up applications
   - [Register Tumblr application](https://www.tumblr.com/oauth/register)
     - Write down your secrets
   - [Register Reddit Application](https://github.com/reddit-archive/reddit/wiki/OAuth2)
3. Editing settings
   - Open reddit2tumblr.py in your preferred text editor
   - Enter your secrets
   - Replace blogname value with yours
   - Adjust subreddit, min_score, post_limit, post_sort and delete_images_when_done to your preferences
   - If needed you can change the tags in the get_tags functions. Use the existing categories as a reference on how to structure them
