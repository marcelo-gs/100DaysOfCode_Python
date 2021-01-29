#Step 4 - Upgrade SQLite Database to PostgreSQL

Getting a website is not that easy huh?

You might be wondering what else we might possibly need to do after all that. There's just one last thing. When we were coding and testing our Flask website, it was nice to use a simple database like SQLite. But SQLite is a file-based database. This is its strength and weakness. It's a strength because while we're coding up our database and debugging, it's really useful to be able to open the SQLite file using DB Viewer and see how our data looks.

https://img-a.udemycdn.com/redactor/raw/2020-10-27_15-13-03-2e5d6a8a93057612885b4389439e16bd.png?hlxIEr2n-ZxLXEgjH3x_Rf8BJlkToEljeMn_aKadDCWD49X5XwpozL7BexjTod6IrxteHJZVWAR_x8Mkq6gxUootl0IYnKg8PMEUhse-A-NvNYNqRxmVKqz08thKG-mXpB-_6_AtiYxgrY7vgUvlqKmxTxz_EgbkDVgfZ1I2RG380BVv

But it's also a weakness because once it's deployed with Heroku the file locations are shifted around every 24 hours or so. This means that your database might just get wiped every day. That will mean some very unhappy users. Read more here.

So we've got to put on our big-boy/big-girl pants and upgrade our simple SQLite database to PosgreSQL, a database that can handle millions of data entries and reliably delivers data to users.

Luckily, because we used SQLAlchemy to create our Flask app, there's nothing we need to change in terms of code. We just need to set up the PostgreSQL database and tell Heroku about it.



1. Go to your app's dashboard on Heroku and go to the Resources tab. Then search for Heroku Postgres.

https://img-a.udemycdn.com/redactor/raw/2020-10-27_15-15-04-46bcd2c3d26ece72afe3aaaad2ee35c0.png?5HtrdeFFiXrf5xj6vS4pQ_NEfRDzPr2TC1lEaXbfop52KxYqO8YVYlduzR1oEMnMvEqY9HSt6Mv3hAbUyXiqVw19lBSXd5ywSliOhQ5PH64fAWDa4LYgc2MufUtEt41Giu00_ijL3AsiXeKSXdnyFIdrqiuY4X-sdQGQW7unX5bjoI4w

Next, you will see a popup, keep the free-tier and click Submit.

https://img-a.udemycdn.com/redactor/raw/2020-10-27_15-15-56-1a9f8acec44404d7ca78057b08bddf5a.png?_OIiO7Prizrxgvsn1PaW1L0szedvEz8riDEFZpKySkjr0Vwfya5HC2hFCyvBjxavJdgjnKZbbz0KZlw9FmU7Tc5OSA9k7dPhaqUtODstRK_4NZHmJihYTM7i35VJ-V58-Ur313XWEoMaY3jZSA22PMf83R9XxWkptJZ0zYXG7aABklQK

Next, we need to connect to this Heroku Postgres database instead of the local SQLite database.

2. Go to Settings -> Reveal Config Vars

https://img-a.udemycdn.com/redactor/raw/2020-10-27_15-17-52-aaef3aad6d1118f35f2e59683d8edbf4.png?jatAoEhNS0WggCCJ7OCDbP_FBNvXzxRsZ0iIG0hbL_2grghdc-fVSVw-FEwLER2AUcBS4hV8WmtbgyJ9pB-ofYqfa74DsewuZIjEPkcP0FqxVH5EIHmr-oMPHhSSnOsh1JjO-3NocD1hHFACjOhChytFkd6QE0XM38b8L3nbtSEVOixa


This is the same as our .env file, it's where you can put top secret stuff like API keys and passwords. Then you give it a variable name and you can tap into the value using os.environ.get("VAR_NAME") .

You'll see that we already have the Postgres database convifg var set up. We just need to connect to it from our code file.

https://img-a.udemycdn.com/redactor/raw/2020-10-27_15-21-21-f7eb3f417c2898ba600332447159e317.png?wtI_MH_Gm9sns9a8ikbk71OxSPahWoI-fJIOl77qdrBHRcvlB42_5ZExG9UUBzWTBlQhH2XYnxH9_ooJmkmMJ-ybEPhopcmfq-gzfy3SoQUVc6WwBu_EvV69Wo6XxNvaw62oBol34jVRw7s0rP5QwEFlkec8Q-sdkgkUpv1bI7bJS-gJ

3. Copy the name of the database config var (mine is DATABASE_URL) and add it to your main.py instead of the sqlite URL.

https://img-a.udemycdn.com/redactor/raw/2020-10-27_15-23-35-9dfef26ff778832bf066a4497817814a.png?Lgm8Oe9SDXN7YA44odLmtlAhy3FmDhKboVJVO_aqPJx_24W63ocYsCnkhZBXMWs1ZJ2-jYC8-4SlGL6Bb29sYGfy72iJjv9msAWFtNDvP5o3RKWnRbIidbiPQC-_O5ij-f6IPNQ_xzYogANunnlQx5KgjfavLiELRrlwJnL_zL5KDikK

4. Let's move our SECRET_KEY into the config var as well.

https://img-a.udemycdn.com/redactor/raw/2020-10-27_15-26-20-653579be44aba7d15d5badc36f6db15f.png?5wOdznvQmp5RYwqmYarD7g2ypD-Wv2Q1Vef3s6ESmKPSzg1gDF9-i4RfeQ2CLY8Dz8yoygLqElgyoCMeiKlvN2kpmSRe5bDrpa5Y_LRajOv9Ge7PDgbUa9lvbva9Q4LXrbgRF43GOB2YOyGJDsLQjq1QWEUc13GqYyK-jt1WL61Xq47X

5. SQLite is pre-installed for all Python projects, but if we are going to use Postgres, we'll need to install the psycopg2-binary packages as well. Note, you'll also need to add the package name and version to requirements.txt as well as commit and push the updates.

https://img-a.udemycdn.com/redactor/raw/2020-10-27_15-36-21-8ca9bb89ef76cb2fb2e6bf17f02c9ac5.gif?kDEzSifJXD6j1TZduQJrCHOXT4umxVKx5ctpRjeDg5o6Y3W3JFYHeR6bpfy22AuWEZiLOjFqzEnoJdPA6qzNEwoirMHc9Ayq3u3NutSJUpXqma_NoADFVgiKTc48dj__TGiK6IVdAWFmO91TwAsgBpdRkWidmdXqtjehb4OGGCwUvoNz

Important, make sure that you don't include any pipfile or pipfile.lock files in your GitHub repo (you can delete them and commit the changes). Heroku needs to know which packages they should install on their side



Because our main.py SQLAlchemy database is now pointing to an environment variable that is only avilable on Heroku, if you run the app right now locally, you will get some errors.

Instead, we want to provide SQLite as the alternative when we're developing the app locally.



5. Update the app config to use "DATABASE_URL" environment variable if provided, but if it's None (e.g. when running locally) then we can provide sqlite:///blog.db as the alternative.

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL",  "sqlite:///blog.db")

Finally, if you go to your heroku app, it should now be up and using a Postgres database.

Whoohoo! Congratulations if you got this far!



Also, check out my version:

https://angela-blog.herokuapp.com/
