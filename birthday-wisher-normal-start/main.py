import smtplib
import random
import pandas
import datetime as dt

my_email = "kunj1766@gmail.com"
password = "1234"

today = dt.datetime.now()

today_tuple = (today.month, today.day)

data = pandas.read_csv("birthday.csv")
data.to_dict(orient="records")

birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_tempelate/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents.remove("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email, to_addrs=birthday_person["email"], msg=f"Subject:Greetings\n\n{contents}")
