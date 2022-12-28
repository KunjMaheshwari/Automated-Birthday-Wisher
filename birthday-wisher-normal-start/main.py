import smtplib
import datetime as dt
import pandas
import random

my_email = "kunj1766@gmail.com"
password = "1234"

# creating a tuple
today = (dt.datetime.now().month, dt.datetime.now().day)

# reading the birthday csv
data = pandas.read_csv("birthdays.csv")
data.to_dict(orient="records")

new_dict = {(data_row["month"], (data_row["day"]))
             : data_row for (index, data_row) in data.iterrows()}

if today in new_dict:
    birthday_person = new_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter:
        contents = letter.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday\n\n{contents}")
