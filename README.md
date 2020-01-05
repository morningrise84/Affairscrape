# Affairscrape

This solution helps you scraping user information from a popular German dating site for people interested in casual relationships and extramarital affairs. 

_(Not that I am interested: I just wanted to challenge myself with something a little bit trickier that would have required some automation)_

## Status

Currently (December 2019) this solution works like a charm. I will not maintain the code over time though. 

Should the site change, the scripts might need to be updated accordingly. Feel free step in as a maintainer.

## Prerequisites

This solution uses Selenium/Chromedriver to login, navigate around the profiles and parse their content. In both scripts you will need to provide:

- Your credentials to login
- Chromedriver's path (Chromedriver must be stored somewhere, locally)

## Usage
Please make sure the prerequisites are met before moving forward with the following steps: 
1) Run retrieveurls.py: this navigates to your search page and generates a list of the last 60 users that logged in your area (I started from the assumption one wants to interact with active users, not with someone who did not login for ages) - the URLs are exported into a .csv file
2) Run parseprofiles.py: this crawls the URLs and parse the user information from each profile

At this point you'll have the user details in a separate .csv file for you to analyse the data, load them into a target system or do whatever you feel like.

For each profile the following information will be stored (of course, if available in the profile):

- ID (for later reference; also useful to load profile information into a target system)
- Nickname
- Age
- Location
- Status (single, etc.)
- Match percentage (calculated based on the information you provided on your own profile)
- Height
- Weight
- Figure
- Smoker
- Desired height (of a potential partner)
- Desired age (of a potential partner)
- Link to the full profile

## Disclaimer

Of course, you cannot know if someone will ever come to your door to kick your ass after you shagged his wife. Hence, my recommendation would be to use such sites carefully. 

Should you have any troubles, well... Your problem! I only wanted to practice Selenium, I am not encouraging you to do stupid things you could potentially regret!

Said so, good luck! :-P
