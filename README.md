# PhotoBucketGrabber
Download all your photos from PhotoBucket using this Python script.

## Requirements
Python 3.4+, I think? Just use the latest Python 3 version.
Also, you'll have to manually edit line 33: https://github.com/trwnh/PhotoBucketGrabber/blob/b0826bcab35b93becea1b30eb739ccbe1e2774f8/grab.py#L33

## Instructions
### Get the direct URLs
1. Log in to your Photobucket account. Go to your "Library".
![image](https://i.imgur.com/u9KhheY.png)
2. Click the checkbox on any photo.
![image](https://i.imgur.com/QRyIzSJ.png)
4. Click "Select all" at the top of your bucket. (This should add those photos to a black bar at the bottom.)
![image](https://i.imgur.com/DA3ntZU.png)
5. Navigate to each of your albums and click "Select all" to add them to the total selection.
![image](https://i.imgur.com/dEopKo8.png)
6. Once you have selected all the photos you want to download, click "Link" on the bottom bar.
![image](https://i.imgur.com/UiqUkwJ.png)
7. Copy the "Direct" link box.
![image](https://i.imgur.com/F5JgWV1.png)
8. Paste those links into a file called "photo.txt" in the same directory as the Python script. Save that file.

### Edit the script
9. Copy the prefix from any one of the URLs you just grabbed. Paste it into the variable `prefix` on line 33. The prefix is part of the URL up to and including your username and the trailing slash. https://github.com/trwnh/PhotoBucketGrabber/blob/b0826bcab35b93becea1b30eb739ccbe1e2774f8/grab.py#L33
10. Run `grab.py`.
11. Watch your photos get downloaded.
12. Feel free to delete your Photobucket account if the photos aren't linked anywhere live anymore.

## Etc
[![mastodon](https://i.imgur.com/ahOT5QI.png)](https://mastodon.social/@trwnh) Contact/follow me: [mastodon.social/@trwnh](https://mastodon.social/@trwnh)

[![email](https://cdn0.iconfinder.com/data/icons/woocons1/Mail.png)](mailto:a@trwnh.com) Email/XMPP: a@trwnh.com
[![xmpp online status](http://trwnh.com:5280/status_alt/a)](xmpp:a@trwnh.com)

[![paypal](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRGOZY1FoaRFdYzeDvRKK3aFHmPnFYMmgd8K3UuZhab-exTZfCc4g)](https://paypal.me/trwnh) Tip me: [paypal.me/trwnh](https://paypal.me/trwnh)

[![liberapay](https://i.imgur.com/B8RZn2y.png)](https://liberapay.com/trwnh) Recurring patronage: [liberapay.com/trwnh](https://liberapay.com/trwnh)
