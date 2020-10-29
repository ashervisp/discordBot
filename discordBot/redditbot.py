import praw
import pandas as pd
import botAuthorize

def refresh_bot():
    subreddit = botAuthorize.reddit.subreddit("catpictures")
    image_dict={"title":[],\
                "score":[],\
                "url":[]}
    print('here')
    for submission in subreddit.hot(limit=100):
                    #if "tuna" in submission.title.lower():
        url = str(submission.url)
        if url.endswith("jpg") or url.endswith("jpeg") or url.endswith("png"):
            image_dict["title"].append(submission.title)
            image_dict["score"].append(submission.score)
            image_dict["url"].append(submission.url)

    image_data = pd.DataFrame(image_dict)
    image_data.to_excel('Images_Bot.xlsx',index=False)
    return
