from google_play_scraper import Sort, reviews
from csv import writer
import mysql.connector



def get_result(url,cont_token):

    result, continuation_token = reviews(
        url,
        lang='en',  # defaults to 'en'
        country='us',  # defaults to 'us'
        count=1000,
        sort=Sort.MOST_RELEVANT,  # defaults to Sort.MOST_RELEVANT
        continuation_token=cont_token  # defaults to None(load from the beginning)
    )

    return result, continuation_token

# def fileWrite(result, url):
#     df = pd.DataFrame(list())
#     df.to_csv(url + '.csv')
#     f = open(url + '.csv', 'a', newline='', encoding="utf-8")
#
#
#     writer = csv.writer(f)
#
#     contents = []
#     for r in result:
#
#         user_comment = [r['reviewId'], r['userName'], r['userImage'], r['content'], r['score'],
#                         r['reviewCreatedVersion'],
#                         r['at'], r['replyContent'], r['repliedAt']]
#         contents.append(user_comment)
#     header = ['review id', 'User name', 'image', 'Comments', 'score', 'thumbsUpCount', 'reviewCreatedVersion',
#               'date-time',
#               'replyContent', 'repliedAt']
#     writer.writerow(header)
#     writer.writerows(contents)
#     # print(contents)
#     f.close()

def main():
    print("Enter URL:")
    url = input()
    token = None
    count = 0
    contents = []

    import time
    while True:
        result = get_result(url, token)
        if count > 1000000:
            break

        for r in result[0]:
            user_comment = [r['reviewId'], r['userName'], r['userImage'], r['content'], r['score'],
                                r['reviewCreatedVersion'],
                                r['at'], r['replyContent'], r['repliedAt']]
            contents.append(user_comment)

        with open('report.csv', 'a', newline='', encoding="utf-8") as f_object:
            writer_object = writer(f_object)
            writer_object.writerows(contents)
            f_object.close()

        token = result[1]
        count += 1000
        time.sleep(5)


if __name__ == "__main__":
    main()
