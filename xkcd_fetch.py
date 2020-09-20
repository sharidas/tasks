"""
xkcd module to download unique images from xkcd website.
To call this module every hour:
1. we can update the cron job in our Linux machine.
2. We can use celery
"""
import os
import time
import xkcd

def get_xkcd():
    """
    Get xkcd images from the website. The images are downloaded
    to the images folder. The images folder will have maximum of
    2 images. Once 2 images are available in the images folder, the
    older image will be unlinked and the new one would be downloaded
    to the images folder.

    Assumption made: the file downloaded per url is unique from xkcd.
    
    If that's not the case, I would implement the solution with md5 or
    sha256 on the files. Since its an xkcd image the file size I see is
    very minimal and in such case md5 or sha256 would not hurt.
    """

    random_comic = xkcd.getRandomComic()

    filaname = "xkcd-" + str(random_comic.number) + "-" + random_comic.imageName

    if not os.path.exists("images"):
        os.mkdir("images")

    local_images = ["images/" + file for file in os.listdir("images")]
    local_images.sort(key=os.path.getmtime)

    if filaname in local_images:
        for _ in range(5):
            random_comic = xkcd.getRandomComic()
            new_image_filename = ("xkcd-" + str(random_comic.number) + "-" +
                                random_comic.imageName)
            if new_image_filename not in local_images:
                break

            time.sleep(5)

    if len(os.listdir("images")) < 2:
        random_comic.download("images", "")
    else:
        os.unlink(local_images.pop(0))
        random_comic.download("images", "")

    print("Image downloaded")


if __name__ == "__main__":
    get_xkcd()
