import os
import praw  # reddit api
import urllib  # view websites
import time  # get time
from imgur_downloader import ImgurDownloader    #get images (specifically gifv)
import pytumblr #tumblr api
import glob # for deleting things in the image folder


def read_secrets(filename):
    try:
        text = open(filename, 'r')
        lines = []
        for line in text:
            line = line.replace('\n', '')
            lines.append(line)
        text.close()
        return lines
    except:
        print('!!! Cannot find ' + filename + ' or it has been deleted !!!')


# SETTINGS
client = pytumblr.TumblrRestClient(read_secrets('secrets_tumblr')[0],    # TUMBLR secrets. don't share
                                   read_secrets('secrets_tumblr')[1],
                                   read_secrets('secrets_tumblr')[2],
                                   read_secrets('secrets_tumblr')[3])

blog_name = 'BLOGNAME'  # your blog name on the url www.BLOGNAME.tumblr.com

r = praw.Reddit(client_id=read_secrets('secrets_reddit')[0],  # REDDIT secrests. again don't share these
                client_secret=read_secrets('secrets_reddit')[1],
                user_agent='reddit2tumblr v.6 by rin')

# subreddit(s) you want to grab posts from. if you want to do more than one do "sub1+sub2"
subreddit = r.subreddit("SUBREDDITS")

min_score = 1  # min score a post can have to post

post_limit = 5    # number of posts you want to upload. if it fails to upload it still counts

post_sort = 'day'   # how to tell reddit to sort them

delete_images_when_done = True  # if you want the program to delete everything in the images folder when its done


def unic(msg):  # convert text for saving in .txt
    return msg.encode("utf-8")


def getTags(sub):
    '''
    You give it a subreddit and it will return a list of tags based on that subreddit

    First it make the sub to be a string since praw passes an object instead of a string (???)

    base_tags are the tags that will be applied to every single post.
        Example: You run a meme blog and want every post to have the 'meme' tag in it, put it in here rather than typing it over and over

    category_1_tags is another category with tags specific to that category. Obviously change the name to fit the category

    Print statment is there to tell you what the subreddit was and to make sure the categories were right

    Sets the tags to the base tags since every post gets them

    Then the If statment part category part:
        It checks if the input subreddit is the same as one of the subreddits listed in that category
        Then prints out the output category name
        Then adds the additional tags to the post tag list

        I wouldn't use elif because some subs can be multiple categories
            Example: r/wholesomebpt in my implementation of this program is both in the twitter category and the wholesome category

        Make as many categories as you want. It doesn't  have to be one

    Just for some consistency, if the tags are the same as the base tags it will tell you


    Once all the appropriate tags are added return the tags for the post
    '''

    sub = str(sub)

    base_tags = ["example tag 1", "example tag 2"]  # base tags are what every single post will get

    category_1_tags = ["additional tag example 1", "aditional tag example 2"]

    print("Input Sub: " + str.lower(sub))
    tags = base_tags

    # CATEGORY 1
    if str.lower(sub) == ('example_subreddit') or str.lower(sub) == ('another_example_sub'):
        print("Output Tags: CATEGORY NAME")
        tags.extend(category_1_tags)

    if tags == base_tags:
        print("Output Tags: NORMIE")

    return tags


def q_post(file_name, file_type, subreddit, caption):  # i made q_post it's own function because i'm lazy and don't want to type out this post thing so much
    if file_type == 'photo':
        client.create_photo(blog_name, caption=caption, state='queue', tags=getTags(subreddit), data=file_name)
    elif file_type == 'video':
        client.create_video(blog_name, caption=caption, state='queue', tags=getTags(subreddit), data=file_name)
    else:
        print('Only photo and video supported currently')


def main():
    # Initializing
    current_dir = os.path.dirname(os.path.realpath(__file__))  # pytube download requires a full file path and using this to get it

    print("opening file..")  # open output in writing mode
    target = open("output.txt", "w")

    print("removing file..")  # reset output
    target.truncate()

    print("writing file..")

    print('getting submission')
    submissions = subreddit.top(post_sort, limit=post_limit)  # can be 'day' 'week' 'month' 'year' and probably 'all'e
    print('obtianed submission')
    with open('cache.txt', 'r') as cache:  # go through all the cached posts
        existing = cache.read().splitlines()

    with open('cache.txt', 'a+') as cache:  # with cache open
        for submission in submissions:  # go through all submissions gathered
            time.sleep(.025)  # wait so i can watch it work
            if submission.id not in existing and submission.score >= min_score:     # if we don't have it and it has enough points

                # Adding to cache
                existing.append(submission.id)      # writes down the submission id so we post it again
                cache.write(submission.id + '\n')

                # Image sites
                if submission.domain == 'i.imgur.com' or submission.domain == 'm.imgur.com' or submission.domain == 'imgur.com' or submission.domain == 'i.reddit.com':

                    print('\n______________________________\n')

                    # GIFs (but not GIFV)
                    if '.gif' in submission.url and '.gifv' not in submission.url:
                        print('File format: GIF')
                        urllib.request.urlretrieve(submission.url, 'images/' + submission.id + '.gif')
                        q_post('images/' + submission.id + '.gif', 'photo', submission.subreddit, submission.title)
                        continue

                    # JPG
                    elif '.jpg' in submission.url:
                        print('File format: JPG')
                        urllib.request.urlretrieve(submission.url, 'images/' + submission.id + '.jpg')
                        q_post('images/' + submission.id + '.jpg', 'photo', submission.subreddit, submission.title)
                        continue

                    # PNG
                    elif '.png' in submission.url:
                        print('File Format: PNG')
                        urllib.request.urlretrieve(submission.url, 'images/' + submission.id + '.png')
                        q_post('images/' + submission.id + '.png', 'photo', submission.subreddit, submission.title)
                        continue

                    # JPEG
                    elif '.JPEG' in submission.url:
                        print('File Format: JPEG')
                        urllib.request.urlretrieve(submission.url, 'images/' + submission.id + '.JPEG')
                        q_post('images/' + submission.id + '.JPEG', 'photo', submission.subreddit, submission.title)
                        continue

                # YouTube
                if submission.domain == 'youtu.be' or submission.domain == 'youtube.com':

                    print('\n______________________________\n')

                    print('File Format: Video (YouTube)')
                    try:
                        os.system('youtube-dl ' + submission.url + ' -o images/' + submission.id + '.mp4')
                    except:
                        print('!!! Could not download YouTube video !!!')
                        continue

                    # this if elif is if the video came from youtubehaiku
                    # they put stuff like this in front of the name, so i remove it
                    new_title = submission.title
                    if '[poetry]' in str.lower(submission.title):
                        new_title = submission.title[9:]
                    elif '[haiku]' in str.lower(submission.title):
                        new_title = submission.title[8:]
                    q_post(current_dir + '/images/' + submission.id + '.mp4', 'video', submission.subreddit, new_title)
                    continue

                # GFYCAT
                if '.gifv' in submission.url and submission.domain == 'gfycat.com':

                    print('\n______________________________\n')

                    print('File Format: GIF (GFYCAT)')
                    # gotta do substrings because the link reddit gives is wrong 100% of the time
                    gfycat_d = submission.url[:8] + 'thumbs.' + submission.url[8:] + '-size_restricted.gif'
                    try:
                        urllib.request.urlretrieve(gfycat_d, 'images/' + submission.id + '.gif')
                    except:
                        print("!!! Tried to download GFYCAT, failed !!!")
                        continue
                    q_post('images/' + submission.id + '.gif', 'photo', submission.subreddit, submission.title)
                    continue

                # v.reddit.com
                if submission.domain == 'v.reddit.com':

                    print('\n______________________________\n')

                    print('File format: Video (v.reddit)')
                    try:
                        os.system('youtube-dl ' + submission.url + ' -o images/' + submission.id + '.mp4')
                    except:
                        print('!!! Could not download YouTube video !!!')
                        continue

                    q_post('images/' + submission.id + '.mp4', 'video', submission.subreddit, submission.title)
                    continue
            else:
                print('Already have ' + submission.id + '!')



    if delete_images_when_done:
        folder = current_dir + '/images/*'
        files = glob.glob(folder)
        for f in files:
            os.remove(f)

        print('Images folder cleared')
    print('!!! DONE STEALING MEMES !!!')
    target.close()  # unload the text
    input()


if __name__ == "__main__":
    main()