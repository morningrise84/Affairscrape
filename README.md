# Affairscrape

This helps you scraping users from a popular German dating site for people interested in casual relationships and extramarital adventures. Not that I am interested: I just wanted to challenge myself with something a little bit trickier that would have required automation.


## Status

Compared to other repositories I published on [GitHub](https://github.com/mpomar), this is more elaborated. 
On the other hand, I am not happy with the quality of the scraped information (read: it is possible to scrape MORE data). 

As I am not fully satisfied with the final result, I might decide to refine this further in the future. 
I always appreciate an helping hand, so do not hesitate to reach out for collaboration.

In the long run I am not planning to maintain these scripts though. Feel free to step in as a maintainer if this solution is particularly close to your heart (not to mention other body parts lol)!


## Description

You will need to run the following scripts in this order:
1) retrieveurls.py: this generates a list of the last 60 users that logged in (ideally we would prefer to interact with people who actively use the platform, not with someone who did not login for ages)
2) parseprofiles.py: this crawls the URLs listed by retrieveurls.py and parse some information from each profile

Both scripts require credentials to login and chromedriver (I used Selenium for the automation).

For each user you are going to store the following information:

- Username
- Age
- Height
- Status (single, married, etc.)
- Match percentage (based on the inputs you provided in your own profile)

## License

[MIT](https://choosealicense.com/licenses/mit/)
