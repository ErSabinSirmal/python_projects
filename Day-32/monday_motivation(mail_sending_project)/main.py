# import smtplib
import random
import smtplib


# my_email = "yahsisabin@gmail.com"
# password = "umjalgqxumatnvwd"
#
# connection = smtplib.SMTP("smtp.gmail.com",587)
# connection.starttls()
# connection.login(user=my_email,password=password)
# connection.sendmail(
#     from_addr=my_email,
#     to_addrs="alysiasabin@yahoo.com",
#     msg="Subject:Hello\n\nThis is the body of my email.")
# connection.close()
def send_mail(quote):
    my_email = "yahsisabin@gmail.com"
    password = "umjalgqxumatnvwd"
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="alysiasabin@yahoo.com",
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )



import datetime as dt #importing datetime module
now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
# print(day_of_week)
if day_of_week == 1:
    # Opening the file
    with open("quotes.txt") as quotes:
        my_quotes = quotes.readlines()
        # print(my_quotes)
    monday_quote = random.choice(my_quotes)
    send_mail(monday_quote)
# creating the datetime object to store the date of birth of the person
date_of_birth = dt.datetime(year= 2003, month= 5, day= 23)
print(date_of_birth)