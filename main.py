import pandas, smtplib, random, os
from pathlib import Path
import datetime as dt
from io import StringIO

# ====================== CONSTANTS ====================== #

FOLDER_PATH = Path("./letter_templates")
BIRTHDAY_CSV = "./birthdays.csv"

MY_EMAIL = "myemail@gmail.com"
TO_EMAIL = "to_email@gmail.com"
MY_PASSWORD = "mysecretpassword"
MY_EMAIL = os.environ.get("MY_EMAIL")
TO_EMAIL = os.environ.get("TO_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

birthdays_csv = os.environ["BIRTHDAYS_CSV"]

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day

# ====================== READ BIRTHDAYS ====================== #

birthday_list = pandas.DataFrame(pandas.read_csv(SringIO(Birthdays_csv)
birthday_list = birthday_list.to_dict("records")

# ====================== RANDOM LETTER ====================== #

txt_files = list(FOLDER_PATH.glob("*.txt"))
random_txt_file = random.choice(txt_files)

# ====================== SEND EMAIL + CHECK BIRTHDAY ====================== #

for person in birthday_list:
    if person["month"] == month:
        if person["day"] == day:
            with open(random_txt_file, "r") as file:
                contents = file.read()
            updated_contents = contents.replace("[NAME]", person["name"])

            with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=TO_EMAIL,
                    msg=f"Subject:Reminder: {person["name"]}'s Birthday!\n\n"
                        f"Hey! Don't forget, today is {person["name"]}'s Birthday!\n"
                        f"{person["name"]}'s Email: {person["email"]}\n"
                        f"{person["name"]}'s New Age: {year - person['year']}\n"
                        f"{person["name"]}'s Birthday: {month}/{day}/{year}\n"
                )

