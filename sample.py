from fortunes.get_quotes_by_author import parse_fortune_file, get_quotes_by_author
from fortunes.get_quotes_by_author import get_quotes_by_author
from fortunes.random_fortune import get_fortune_cookie
from fortunes.send_email import send_fortune_email
from fortunes.getMultipleFortunes import getMultipleFortunes


quotes_dict = parse_fortune_file()
author_quotes = get_quotes_by_author(quotes_dict)

multiple_fortunes = getMultipleFortunes(3)
print("\nMultiple Fortunes:")
for fortune in multiple_fortunes:
    print(fortune)

random_fortune = get_fortune_cookie()
print("\nRandom Fortune:")
print(random_fortune)

recipient = "qy765@nyu.edu"
send_fortune_email(recipient, author_quotes)