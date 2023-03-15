# This Python file uses the following encoding: utf-8
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from platform import python_version
from os import getenv
from dotenv import load_dotenv


from gui_tools.gui_checkbox_choice import choice_address


def make_subject(recipient):
    return f" для {list(recipient.keys())[0]}"


def create_recipients(recipient):
    return ['oldman@kommersant.ru', 'dobrovolskiy_i@kommersant.ru', 'almargolin@yandex.ru',
            'x79046309437@gmail.com'] + list(recipient.values())


def main_module():
    load_dotenv()

    server = 'smtp.mail.ru'
    user = getenv('MAILUSER')
    password = getenv('MAILPASS')

    print(user)

    print("Введи ID фотографии ")
    # print(user,password)
    photo_id = str()

    n = input()
    if n[:3] != "KSP":
        print("NOT VALID ID NUMBER START AGAIN")
    else:
        while n != "":
            photo_id = photo_id + '\n' + n
            n = input()

        recipient = choice_address()

        recipients = create_recipients(recipient)
        sender = 'pavlenko-e@mail.ru'
        subject = make_subject(recipient)
        text = photo_id
        # html = '<html><head></head><body><p>' + text + '</p></body></html>'

        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = 'Evgeniy Pavlenko <' + sender + '>'

        msg['To'] = ', '.join(recipients)
        msg['Reply-To'] = 'pavlenko.evgeniy@gmail.com'
        msg['Return-Path'] = 'pavlenko.evgeniy@gmail.com'
        msg['X-Mailer'] = 'Python/' + (python_version())

        part_text = MIMEText(text, 'plain')
        # part_html = MIMEText(html, 'html')

        msg.attach(part_text)
        # msg.attach(part_html)

        mail = smtplib.SMTP_SSL(server)
        mail.login(user, password)
        mail.sendmail(sender, recipients, msg.as_string())
        mail.quit()


if __name__ == '__main__':
    # print(create_recipients({'Кауровой': 'kaurova@kommersant.ru'}))
    # print(make_subject({'Кауровой': 'kaurova@kommersant.ru'}))
    main_module()
