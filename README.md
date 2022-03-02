# twitter-whitelist
A Twitter Bot for performing various interactions with a tweet


## Step 1 - Get a Twitter Developer Account
1. Log-in to Twitter and verify your email address and phone number.
2. Go sign up at [developer.twitter.com](https://developer.twitter.com/en/portal/petition/essential/basic-info.html) with your basic name, location and use case details.
3. Review and accept the developer agreement.
4. You should now have access to the Developer Portal to create a new App and Project with Essential access.


## Step 2 - Make a Twitter "Project"
To create a Project, click on “New Project” in your [dashboard](https://developer.twitter.com/en/portal/dashboard) or the [Projects & Apps](https://developer.twitter.com/en/portal/projects-and-apps) page within the developer portal. You’ll only be able to see this option if you haven’t already created a Project. You will be prompted to create a Project name, description, and use case. You will also be asked to create a new App or connect an existing standalone App.

Make the App put in whatever details (maybe PRODUCTION environment at the first step is needed I think)


## Step 2.5 - Save your "Consumer Keys"
There are a bunch of different access keys and tokens.
You will need the ```API Key and Secret```

Put them and and your username, email, password into the ```config.py``` file.


## Step 3 - Get this repo
Open a terminal, navigate to some reasonable directory and run
```
cd ~/Documents/
git clone https://github.com/natbutter/twitter-whitelist.git
```

## Step 4 - Set up your Python environment
Open a terminal window and run
```
conda create -n twitter pip
conda activate twitter
pip install selenium==4.1 webdriver-manager==3.5 requests-oauthlib==1.3
```

## Step 5 - Edit bot.py

Set your userid, the tweetid, and which options you want at the top of the script


## Step 6 - Run bot.py
Open a terminal window. 
Launch your conda environemnt.
Change directories to where the code is.
And run.
```
conda activate twitter
cd ~/Documents/twitter-whitelist
python bot.py
```

If all goes well you should get a bunch of GOOD codes returned. Plus you can check on twitter to see if your account has performed the things needed. 