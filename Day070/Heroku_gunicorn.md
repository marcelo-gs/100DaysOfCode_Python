Step 2 - Use gunicorn and Heroku to host your website
Now that our project code is uploaded to GitHub we can use Heroku to host the code and deploy our website.



1. Sign up for a free account on www.heroku.com



2. Create a new application on Heroku:

https://img-a.udemycdn.com/redactor/raw/2020-10-26_16-32-25-f9bd4f726cab144c630915203f926063.png?bdWlb6u7Aq9y33A9FUjEN9EuKOFc1hkluffTvXdhkUiJgYGboYfmhNUYe67bREtkwYk5r4J9o2xtRfU-12cWau4NtoMB2DA5d5gqwmvVb4EpXCgZ4R3HM0h17wpI0zUKeQEHU2aodGvfxVQawmKI8yphUMQNnQr7EriiFp-llSAPEZ5l

Give your new app a unique name, I used angela-blog which means that no one else can use that name. It's just like a web address, it has to be unique. Leave the region as US and click Create App.

https://img-a.udemycdn.com/redactor/raw/2020-10-26_16-34-22-0674fa6bd49a1685028bc71c1b73adcd.png?JRBcGWJQWVeL7ocrQXfLdRpuSkJUJiT2whMoaiDafUwW7bmfvhect0RmJUO5nKQPRMFay8TusvhGzFmSdk-XQHLyJpMtdaE3duKXUvXw0cG2JMEGmfLc-c6jbDuAFdBHwMjRVfZKi-t7zZJI9JrqRbKU8sMNlik2fwwfEuY1AsM-Rf-o


3. Connect Heroku to your GitHub project. Under the Deploy tab, select Connect to GitHub

https://img-a.udemycdn.com/redactor/raw/2020-10-26_16-35-59-b1a9f26b6a488609b1062025d57045c8.png?ANPUB2NyjLN9iC7FWNCQ5u4Kw_6X7C26EFa9OARMqHVBX3EwU1DxKoksHE6jCIe3iogBo3k-xkxEQCcazhRLkDkIi2w4sdFiIjT_DnZm_JNuyiRfMXi5Jvi2RTyqotxhp68L5kYYnmjmy8mf3v4iQJ-kyemAr3Ferrr44Ho0XESciMYs

https://img-a.udemycdn.com/redactor/raw/2020-10-26_16-36-43-0afbb4f841ecd633593ec9d3245321b1.png?In_g0Y4nfJ2Y-xhjQuAdYOWSrd1tMAocDT1THplugWFGr6FEJJA1dijpxaxCGavROGJcqZXnx1NihrccSQy4k9UMdafggRbwA_loc36G3xn0K_MIvsE3oEXFk_6vAixvTpF9R7xX8N1Bu4HlImohO7YLxquMn1BIeRBj8AqDFLFeyb6Q

4. Sign in to your GitHub account (the account where your blog project repository exists).



5. Search for the name of your blog project repository name (if in doubt check GitHub) and connect it to Heroku.

https://img-a.udemycdn.com/redactor/raw/2020-10-26_16-41-54-e06e2bbd79962b0693aa21cb2e3e7d2f.png?HR7teBXpGfd2kUYwNXi_1zbtsVTY-T5nrwlaqQg-v2reJVlgjouMIIptZXrbT3Ftki8285BI_3ulZxww5VDMW8fsCWXkJBsz80BkEZtuMICnVyxicXDQnKZF9sYnA3gxQc6u55YO_nXvF-HLo4DX1UYWQuQEqciaNLg7f5C-uNdknRpS

6. Scrolling further down the page on the deploy pane, click on Enable Automatic Deploys. This means that whenever you push a new commit to your remote GitHub repository, it will automatically re-deploy your server with the changes.

https://img-a.udemycdn.com/redactor/raw/2020-10-26_16-44-11-68a19c0e183510b159c6254e65a4a854.png?jfy8FeNKPURl6wlVuENV25VGu3IPRH9ORHK4SFJVS7mppR8K3XYE1SrLTqT6QfxX-M3se4aL-wpojygzcovj3nyIOOj5Xleb_OhYad26cSHD7viBJ8GNawGQlZr4TPxmQ1zheGsrpfIBqXMYK8Nui3lsi4A0Dk5gHnFtKbSOzHsp05g_


7. Finally, in Manual deploys, click on Deploy Branch to deploy for the first time.

https://img-a.udemycdn.com/redactor/raw/2020-10-26_16-44-43-9192f8c786101ac4288a4509ca2a66c1.png?hFmwonAVV5-w3Yx_EGg_at7lamO1dpZ_xvhXzJEADdRAvWWjYEh5Cklj7GwIBj-6utgX3Q1_mhfkIFMpssPq5-37vxSrB2Io4YjqBssdgiqqXRqiQahnnn2IfOleakH6pDlb00F29kNPhp0kv5jsm_m6lk1VePSNRPCpq2CLT6U6mmeS

NOTE: This step will take some time, but you can watch the logs for any errors and Google them if they prevent deployment. It might mean that you miss a step that we covered.

8. Once it's done, click View to see your web app, NOTE: it won't work just yet:

https://img-a.udemycdn.com/redactor/raw/2020-10-26_16-48-25-ce00c9229df91e3a58568bf3bd8d5a27.png?COCHRJXEhCly60HhM-uBLZb9lF9JnZWjgHWusnqRQLVsroLiFqvIE5kNUSQtzV4sdqTW4mWEr53pIOPKpQYv7Lv18k4QJ_zNG8a2seizTJU10jkUz8zfceWMRdUG_-aP_BuTQKXS58bmEvpFpsTVbBoFv1hslwJIPyNKyC4Vx2Gz6DJn

If everything went well, you should see the following:

https://img-a.udemycdn.com/redactor/raw/2020-10-26_16-49-18-e08ed41d379603ed1975556cacb3a84c.png?66AGN1mewrCwHXJJsFXcPWrG9BFttqbYUi9KtaaagS6t6LRlpWed1WBd9iZiZg2kMK4uqSuKWCJ4j7MeaJxtZ4WRnN4z8stHnJyTpq7FuBZ8qLiOXWpP_onRO6ralh1FpXhtLq-r12ZaEwqbCaUaCgWNTQqn3NOAhmM04_78lCPKbSPW

It tells us to see the Heroku logs to see what went wrong.

9. Instead of using the command line as they suggested, we're going to view the logs on heroku.com

Make sure that you're in your app's dashboard page, go to More -> View Logs

https://img-a.udemycdn.com/redactor/raw/2020-10-26_16-51-22-f2acb361947e7aebd6c878e0ce276a41.png?8HTmMMeoVbcMakc4ggMLz6OSPtuS3G3U2RXfE8oym0q73VGhKbzEAKUhvOwjR-FOaZD5L0DMKBGYzx7fp1wLvtEB-JJ8LU7fiXEc8KOjzyvG64fvKqPYO23PPqn-wzoWpik9-cfgEO5cVhAByIuzn7IyPHp2d-3NsZoqyYpq5djPYebQ

In my case, it tells me that there are no web processes running:

https://img-a.udemycdn.com/redactor/raw/2020-10-26_16-53-01-ceef810c6a490ff5bbb468efc4ac26f2.png?3KJDEzmHgnzRf_Szmyi2Qf_dIaiAvgYmpJmUnfR6JoLizqZeKidF2_aMSo3sSLCzZT6qKpEf0AtzxeTH0uxI1jk6tlKFHXmsJDfg1Ts47b48ScNsjQ7SHaypTE7GY6PY-XcfVtxXdoKDsZyd3taQdtNmgmOqLBiMwogrJd6RUMMw2wje

This error tells me that our code is successfully hosted on Heroku but it doesn't know how to run our app.

That's what we'll do in the next lesson.
************************************************

Step 3 - Setup a WSGI server with gunicorn

You might recall that every time we ran our app, we got a warning telling us that when we want to make our website go live and go from development to production mode that we should use a WSGI server.

https://img-a.udemycdn.com/redactor/raw/2020-10-26_16-24-35-f4684e68f18b154a93473a10739cb25e.png?QzF5OtFK3V_SPDn-HjzskuE3gB9CyaNB3wca7rL136Ot6onMCWVcb-z10dOkReN4tI90YY6lTMTU45mtcPLZ8fsLMKrlKymNFSItR1dzmTzVNjLMTRXfH3AY32UNfEPnoAQKKjR7KwUfFPafnWokb5jt52gXKkgvbPoduNVkZW2hK92I


WSGI stands for Web Server Gateway Interface and it's described here: https://www.python.org/dev/peps/pep-3333/

It standardises the language and protocols between our Python Flask application and the host server.

Again, but in English: Normal web servers can't run Python applications, so a special type of server was created (WSGI) to run python applications.

There are many WSGIs to choose from, but we'll use the most popular - gunicorn.

So Heroku will call gunicorn to run our code and gunicorn will know how to speak to Heroku.



1. In PyCharm go to the Python Interpreter for your Project and install the gunicorn package:

Windows: Files -> Settings -> Project: blog-with-user -> Python Interpretor

Mac: PyCharm -> Preferences -> Project: blog-with-user -> Python Interpretor

https://img-a.udemycdn.com/redactor/raw/2020-10-26_17-10-17-3f3ac71f32d7729557264b82a7f783df.png?LyxHtcI9jvz03ZI1axe0JsOaHKaXJUy-Ghe5BqA--zyflOht2Bl6WvQs-qMGckptCkTggLMMqHYMB0xlQAS2mBFskiE204nORgE1Q1c-Mbnk2fRrv_w_ERrOr3E9xvPcO0tuU7S0lHjkEfml0nQJEQOwY6oONCAdrcZuLhyhLDFQiU3w

Note: Make a note of the version of gunicorn you installed e.g.

https://img-a.udemycdn.com/redactor/raw/2020-10-26_17-11-42-a77f776caf6fdb6fe46da289e3f2c81c.png?qzFmQUGsPO9mcf6zNg-cYK5xgqav9qW8TWeM4fTDrshJlQYHAgd3-GpWlYd92gxPlkr37jxNN_-rhWAeTUcnlBggFMLXIpanMWBil6Mx79CM4fU6gEZuI8G_DltliFFC9tQaDJVBJvAEffMx37oKBu75H0lrg6CBlCCpcuo17qDmqy6U


2. Add the package to the requirements.txt file on a new line:

gunicorn==<version number>

https://img-a.udemycdn.com/redactor/raw/2020-10-26_17-13-24-c8e203a7b635e201c33471458197cf01.png?yLPFIPcRD2FgP6Eg2j624SGYGb_5fntqGm7FSM8q9askZqFD0qj2vcaNSL13pnt02IbW_-xqa2Gso8fY8wobQ9bhtW07sTAH_ktICQcvUdPSMgMN10pZOxg8Lka_gbZKg97HGKxJ7yAgEtX-1jEvJ91l6FxhbUO7BT-T8IgTtjXHOXLe

NOTE: Your version number will be higher than mine because you are in the future.



Next, we need to tell Heroku about our gunicorn server and how to run our Flask app, we do that using a Procfile.



3. Create a new file in the project top-level folder called Procfile

NOTE: make sure you spell the name of the file exactly as you see above, with a capital P and no file extension.

Type the following into the Procfile:

web: gunicorn main:app
This will tell Heroku to create a web worker, one that is able to receive HTTP requests.

To use gunicorn to serve your web app

And the Flask app object is the main.py file.

NOTE: If your app is not inside a file called main.py then you should change main to your file name.


https://img-a.udemycdn.com/redactor/raw/2020-10-27_14-45-56-7e34477c7e07aa2595538ea1b3148794.png?9k0soD6bG4SAAJkiONyc5S35rJqbx2b3L3n616BcCI2eJSY8qTTwoZfPqDYOWni922WO3Bzy60sNhvBzNiC-Unr6FGiqJSmE-dHMFHoL2j8GjWKgYoDcfb_hVv9coynQhA-HHAMz21XW-Ef4i2O9NR34zWHS-2_1wWPjf4u6kUyXkdE7



4. Add the new Procfile/requirements.txt to git and commit the changes then push it to the remote.

https://img-a.udemycdn.com/redactor/raw/2020-10-27_14-49-16-7ccbdf444cb976fe03b46bce1d0533f6.png?EaEd0jgihCoURL4M2oqyiZRNbd_LlJtDXOAF1l2d2Dnr7QR0dLvlppB_n6npkno53jVTa6zReX-89Jjlms1ITLIPEgANiDbFMo_7NQeLEypI19ASt5Qy5oPAks81tcjw3ZHneVe_mbxK0nQSzHXVmUyOB6lD7EEHCxmwN7rA-rbTIqBJ

Note: If you forgot to "Commit and Push" and just clicked on "Commit" then just go to VSC -> Git -> Push



Because we enabled automatic re-deploys, if you go to your app's logs you should see it being re-built an re-deployed with the changes we have pushed to GitHub.

https://img-a.udemycdn.com/redactor/raw/2020-10-27_14-53-12-0ea781d05a519f3337775ca98c809ce1.png?IWoQa1RofGbd810wZJ9j45OEPN_kvfIz1nnQA6958N28THDCJltQhUq6AMZMvEg6OliSRmRuslIL60Kwf1BQncOkbcQM4KsSvc_eFgOp0tofvbxKUYHQH43otouC-SzI0V0xNmAPtoPEcpuMyV-VnFKKu22hx3YRFK5nXQIpZsy-ubwX


All going well, you should now be able to go to your app and see the blog up and running.

https://img-a.udemycdn.com/redactor/raw/2020-10-27_15-05-31-c2c650c2c82894137a9ccfc0ea1f5aac.gif?NDvDkrPxbmxXGExYxiUlXSReqiBrVYQcchw8A-CGNLOFW5SxT8ZDktVQ0Lb7smxYaVDmP5ud9pXu1KCi0rGkXG85f5jtiAWOg2lcN1D62xf6Q3cK7FF7sb-s0hAiJyuGeRHh9xnVFDKX9SQxZB-_yjz1CK-eQ2rf4SsUJGuUy4LChhjr