##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import datetime as dt
import pandas
# To pick the random letter template from the letter template folder
import os
import random
import smtplib
MY_EMAIL = "yahsisabin@gmail.com"
PASSWORD = "umjalgqxumatnvwd"
data = pandas.read_csv("birthdays.csv")
today = dt.datetime.now()
today_month = today.month
today_day = today.day

#iterate through the rows and compare month and day
for index,row in data.iterrows():
    if row['month'] == today_month and row['day'] == today_day:
        birthday_person = row['name']
        file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
        # opening the txt file
        with open(file_path) as letter_file:
            contents = letter_file.read()
            contents = contents.replace("[NAME]",birthday_person)
        with smtplib.SMTP("smtp.gmail.com",587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL,PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=row["email"],
                                msg=f"Subject:Happy Birthday!\n\n{contents}")






