Task 1
------

I have added my solution in min_coins.py file. Also I have attached few unit
tests. In this solution, if the user provides real numbers to return_coins
method say 2, 3, 4 etc, then I multiply them with 100 to get the euro coins. If
the user needs to provide 5 cents as input then 0.05 is accepted one becaus
0.05 * 100 = 5.


Task 2
------
The solution file is xkcd_fetch.py

I have assumed here that the image names provided by a link from xkcd is unique.
Meaning no different urls will share same image. Hence I am checking for the
image names. But if that's not the case then the alternative would be to
compare either with sha256 or md5sum, though I am aware that it would be
difficult to scale with md5sum or sha256 for larger files. 

We can add this code to cronjob which can be called every hour or 2 hours based
on the configuration. This has its own problems. Debugging would be a mess.

But if we think more in terms of microservice solution, celery would be a
good choice. I have not used celery in the code. But I am aware of the fact
that using celery we can have reliable system.

Task 3
------

I have created a simple web app, using Postgresql + Flask + Docker

To run in you may execute `docker-compose build up --build`

There is room for improvement for this app. Some of them which I would like to
highlight here:
1. Instead of API_KEY a token based auth would have been apt for this tiny app.
2. More unit tests required.
3. There is still room for improvement in the UI
4. Nginx in front of gunicorn would have been really nice.

