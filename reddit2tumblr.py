# py 3.6 in users\rin\appdata\local\programs\python\python36
import os
import praw  # reddit api
import urllib  # view websites
import time  # get time
from imgur_downloader import ImgurDownloader    #get images (specifically gifv)
import pytumblr #tumblr api
from pytube import YouTube  #youtube downloading api
import glob # for deleting things in the image folder

# SETTINGS
client = pytumblr.TumblrRestClient('A',    # TUMBLR secrets. don't share
                                   'B',
                                   'C',
                                   'D')

blog_name = '30MinuteTest'  # your blog name on the url www.BLOGNAME.tumblr.com

r = praw.Reddit(client_id='X',  # REDDIT secrests. again don't share these
                client_secret='Y',
                user_agent='reddit2tumblr v.5 by rin')

# subreddit(s) you want to grab posts from. if you want to do more than one do "sub1+sub2"
subreddit = r.subreddit("funny+meirl+me_irl+AdviceAnimals+teenagers+HistoryMemes+anime_irl+bikibottomtwitter+blackpeoplegifs+blackpeopletwitter+comedycemetery+dankmemes+humor+meme_irl+memes+wholesomememes+surrealmemes+DeepFriedMemes+ComedyNecrophilia+bonehurtingjuice+trippinthroughtime+wholesomebpt+youdontsurf+4chan+fakehistoryporn+hmmm+dank_meme+2juicy4bones+deepfriedsurrealmemes+Patrig+whothefuckup+anthologymemes+equelMemes+OTMemes+PrequelMemes+SequelMemes+WhitePeopleTwitter+youtubehaiku+NotTimAndEric+InterdimensionalCable+gifs+combinedgifs+HighQualityGifs+reactiongifs+reallifedoodles")

min_score = 1  # min score a post can have to post

post_limit = 5    # number of posts you want to upload. if it fails to upload it still counts

post_sort = 'day'   # how to tell reddit to sort them

delete_images_when_done = True  # if you want the program to delete everything in the images folder when its done


def unic(msg):  # convert text for saving in .txt
    return msg.encode("utf-8")


def getTags(redsub):    # input subreddit and
    print("Input Sub: " + str.lower(str(redsub)))

    normal = ["meme", "memes", "dank", "funny", "lol", "humor", "humour", "lmao", "dank meme", "dank memes",
              "super dank", "lolz", "funny pics", "funny post", "funny", "lmfao", "me_irl", "30minute"]

    starwars = ["star wars", "starwars", "star wars memes", "starwars memes", "prequelmemes", "prequel memes", "sequel memes"]

    history = ["history", "history memes", "fake history", "fake history porn", "funny history"]

    surreal = ["surreal", "surreal memes", "weird memes", "wierd memes", "deep fried memes", "fired memes"]

    wholesome = ["wholesome", "wholesome memes", "nice memes"]

    twitter = ["twitter memes", "black people twitter", "white people twitter", "funny twitter"]

    anime = ["anime memes", "anime", "funny anime", "animememes", "animemes"]

    stockphoto = ["stockphoto memes", "stock photo memes", "stock photo", "stock photos"]

    chan = ["4chan", "greentext", "green text"]

    hmmm = ["hm", "hmm", "hmmm", "hmmmm", "makes you think", "think", "wierd", "weird"]

    youtube = ["youtube", "video", "gif", "gifs", "funny videos", "videos", "meme video"]

    gifs = ["gif", "gifs", "funny gif", "funny gifs", "jif", "high quality gifs"]

    # STAR WARS MEMES
    if str.lower(str(redsub)) == ('anthologymemes') or str.lower(str(redsub)) == ('equelmemes') or str.lower(
            str(redsub)) == ('otMemes') or str.lower(str(redsub)) == ('prequelmemes') or str.lower(str(redsub)) == (
    'sequelmemes'):
        print("Output Tags: STAR WARS")
        tags = normal
        tags.extend(starwars)

        print(tags)

        return tags

    # HISTORY MEMES
    if str.lower(str(redsub)) == ('mistoryMemes') or str.lower(str(redsub)) == ('trippinthroughtime') or str.lower(
            str(redsub)) == ('fakehistoryporn'):
        print("Output Tags: HISTORY")
        tags = normal
        tags.extend(history)

        print(tags)

        return tags

    # SURREAL MEMES / DEEP FRIED MEMES
    if (str.lower(str(redsub)) == ('deepfriedmemes') or str.lower(str(redsub)) == (
    'deepfriedsurrealmemes') or str.lower(str(redsub)) == ('surrealmemes') or str.lower(str(redsub)) == (
    'whothefuckup')):
        print("Output Tags: SURREAL")
        tags = normal
        tags.extend(surreal)

        print(tags)

        return tags

    # WHOLESOME MEMES
    if str.lower(str(redsub)) == ('wholesomememes') or str.lower(str(redsub)) == ('wholesomebpt'):
        print("Output Tags: WHOLESOME")
        tags = normal
        tags.extend(wholesome)

        print(tags)

        return tags

    # TWITTER MEMES
    if (str.lower(str(redsub)) == ('bikibottomtwitter') or str.lower(str(redsub)) == (
    'blackpeopletwitter') or str.lower(str(redsub)) == ('whitepeopletwitter')):
        print("Output Tags: TWITTER")
        tags = normal
        tags.extend(twitter)

        print(tags)

        return tags
    # ANIME MEMES
    if (str.lower(str(redsub)) == ('anime_irl')):
        print("Output Tags: ANIME")
        tags = normal
        tags.extend(anime)

        print(tags)

        return tags

    # STOCK PHOTO MEMES
    if str.lower(str(redsub)) == ('youdontsurf'):
        print("Output Tags: YOUDONTSURF")
        tags = normal
        tags.extend(stockphoto)

        print(tags)

        return tags

    # 4CHAN MEMES
    if str.lower(str(redsub)) == ('4chan'):
        print("Output Tags: 4CHAN")

        tags = normal
        tags.extend(chan)

        print(tags)

        return tags

    # YOUTUBE / VIDEO
    if str.lower(str(redsub)) == 'youtubehaiku' or str.lower(str(redsub)) == 'nottimanderic' or str.lower(str(redsub)) == 'interdimensionalcable':
        print('Output Tags: YouTube / Video')

        tags = normal
        tags.extend(youtube)

        return tags

    # GIFS
    if str.lower(str(redsub)) == 'gifs' or str.lower(str(redsub)) == 'combinedgifs' or str.lower(str(redsub)) == 'highqualitygifs' or str.lower(str(redsub)) == 'reactiongifs' or str.lower(str(redsub)) == 'reallifedoodles':
        print('Oyput Tags: GIFS')

        tags = normal
        tags.extend(gifs)

        return tags

    # HMMM MEMES
    if str.lower(str(redsub)) == ("hmmm"):
        print('Output Tags: HMMM')
        tags = normal
        tags.extend(hmmm)

        print(tags)

        return tags
    if (str.lower(str(redsub)) == ('funny') or str.lower(str(redsub)) == ('meirl') or str.lower(str(redsub)) == (
    'me_irl') or str.lower(str(redsub)) == ('adviceanimals') or str.lower(str(redsub)) == ('teenagers') or str.lower(
            str(redsub)) == ('blackpeoplegifs') or str.lower(str(redsub)) == ('comedycemetery') or str.lower(
            str(redsub)) == ('dankmemes') or str.lower(str(redsub)) == ('humor') or str.lower(str(redsub)) == (
    'meme_irl') or str.lower(str(redsub)) == ('memes') or str.lower(str(redsub)) == ('comedynecrophilia') or str.lower(
            str(redsub)) == ('bonehurtingjuice') or str.lower(str(redsub)) == ('dank_meme') or str.lower(
            str(redsub)) == ('2juicy4bones') or str.lower(str(redsub)) == ('patrig') or str.lower(str(redsub)) == ('gifs') or str.lower(str(redsub)) == ('youtubehaiku')):
        print("Output Tags: NORMIE")
        return (normal)


def q_post(file_name, file_type, subreddit, caption):  # i made q_post it's own function because i'm lazy and don't want to type out this post thing so much
    if file_type == 'photo':
        client.create_photo(blog_name, caption=caption, state='queue', tags=getTags(subreddit), data=file_name)
    elif file_type == 'video':
        client.create_video(blog_name, caption=caption, state='queue', tags=getTags(subreddit), data=file_name)
    else:
        print('Only photo and video supported currently')


def main():
    current_dir = os.path.dirname(os.path.realpath(__file__))  # pytube download requires a full file path and using this to get it

    print("opening file..")  # open output in writing mode
    target = open("output.txt", "w")

    print("removing file..")  # reset output
    target.truncate()

    print("writing file..\n______________________________\n")

    print('getting submission')
    submissions = subreddit.top(post_sort, limit=post_limit)  # can be 'day' 'week' 'month' 'year' and probably 'all'e
    print('obtianed submission')
    with open('cache.txt', 'r') as cache:  # go through all the cached posts
        existing = cache.read().splitlines()

    with open('cache.txt', 'a+') as cache:  # with cache open
        for submission in submissions:  # go through all submissions gathered
            time.sleep(.025)  # wait so i can watch it work
            # the line below is a mess, it checks if the submission hasn't been grabbed, then if the domain is valid and the score is okay
            if submission.id not in existing and submission.score >= min_score and (
                    submission.domain == "i.imgur.com" or submission.domain == "m.imgur.com" or submission.domain == "imgur.com" or submission.domain == "i.redd.it" or submission.domain == 'gfycat.com' or submission.domain == 'youtu.be' or submission.domain == 'youtube.com') and (
                    '.gif' not in submission.url or '.jpg' in submission.url or '.png' in submission.url or '.JPEG' in submission.url):
                print("\n______________________________\nadding " + submission.id + " to cache")
                existing.append(submission.id)
                cache.write(submission.id + "\n")
                if '.gif' in submission.url and '.gifv' not in submission.url or 'cat' in submission.domain:  # if it is a gif and not a gifv
                    print('File format: GIF')
                    if 'gfycat' in submission.domain:
                        gfycat_d = submission.url[:8] + 'thumbs.' + submission.url[8:] + '-size_restricted.gif'  # gotta do substrings because the link reddit gives is wrong 100% of the time
                        urllib.request.urlretrieve(gfycat_d, 'images/' + submission.id + '.gif')
                    else:
                        urllib.request.urlretrieve(submission.url, "images/" + submission.id + ".gif")
                    q_post('images/' + submission.id + '.gif', 'photo', submission.subreddit, submission.title)
                elif '.jpg' in submission.url:
                    print('File format: jpg')
                    urllib.request.urlretrieve(submission.url, "images/" + submission.id + ".jpg")
                    q_post('images/' + submission.id + '.jpg', 'photo', submission.subreddit, submission.title)
                elif '.png' in submission.url:
                    print('File format: png')
                    urllib.request.urlretrieve(submission.url, "images/" + submission.id + ".png")
                    q_post('images/' + submission.id + '.png', 'photo', submission.subreddit, submission.title)
                elif '.JPEG' in submission.url:
                    print('File format: JPEG')
                    urllib.request.urlretrieve(submission.url, "images/" + submission.id + ".JPEG")
                    q_post('images/' + submission.id + '.JPEG', 'photo', submission.subreddit, submission.title)
                elif '.gifv' in submission.url or 'cat' in submission.url:
                    print('File format: GIFV, saved as mp4')
                    if 'imgur' in submission.url:
                        print('from imgur')
                        ImgurDownloader(submission.url, 'images/').save_images()
                    q_post('images/' + submission.id + '.mp4', 'video', submission.subreddit, submission.title)
                elif 'youtu.be' in submission.domain or 'youtube.com' in submission.domain:
                    video = YouTube(submission.url)
                    stream = video.streams.filter(file_extension='mp4').first()
                    print(stream)

                    print(current_dir)
                    stream.download(current_dir + '/images')    #
                    print(submission.url)
                    new_title = submission.title    # made this because posts from r/youtubehaiku have a [poetry] or [haiku] prefix and the below if/elif cuts out the prefix
                    if '[poetry]' in str.lower(submission.title):
                        new_title = submission.title[9:]
                    elif '[haiku]' in str.lower(submission.title):
                        new_title = submission.title[8:]
                    q_post(current_dir + '\\images\\' + video.title + '.mp4', 'video', submission.subreddit, new_title)
                else:
                    print("!!! COULD NOT DOWNLOAD MEME !!!")

            elif submission.id not in existing:  # why i had that whole thing in one line
                existing.append(submission.id)  # cache this submission
                cache.write(submission.id + "\n")
            else:
                print("Already Have " + str(submission.id) + "!")

    if delete_images_when_done:
        folder = current_dir + '\\images\\*'
        files = glob.glob(folder)
        for f in files:
            os.remove(f)

        print('Images folder cleared')
    print('!!! DONE STEALING MEMES !!!')
    target.close()  # unload the text
    input();


if __name__ == "__main__":
    main()
