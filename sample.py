from src.fortunes.get_quotes_by_author import parse_fortune_file, get_quotes_by_author
from fortune_package import get_quotes_by_author
from fortune_package import get_fortune_cookie
from fortune_package import send_fortune_email
from fortune_package import getMultipleFortunes


quotes_dict = parse_fortune_file()
author_quotes = get_quotes_by_author(quotes_dict)

multiple_fortunes = getMultipleFortunes(3)
print("\nMultiple Fortunes:")
for fortune in multiple_fortunes:
    print(fortune)

random_fortune = get_fortune_cookie()
print("\nRandom Fortune:")
print(random_fortune)

recipient = "test@example.com"
send_fortune_email(recipient, author_quotes)