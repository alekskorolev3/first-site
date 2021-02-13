from instapy import InstaPy
from instapy import smart_run
my_username="artiri_by"
my_password="564340karp1"
session = InstaPy(username=my_username, password=my_password, headless_browser=False)
session.login()
with smart_run(session):
    session.set_user_interact(amount=3, randomize=True, percentage=100, media='Photo')
    session.set_do_like(enabled=True, percentage=100)
    session.set_do_follow(enabled=True, percentage=100)
    session.interact_user_followers(["by_custom", "art_dashalisenkova", "supershopper.by", "derova.art", "bymorgonpig",
                                     "totebags.by", "inkis_by_", "shopper_by_", "shocking_studio",
                                     "milenanoda", "onegogh.handmade", "poisonstreetweardesign"], amount=1000, randomize=True)
    session.unfollow_users(amount)
session.end()