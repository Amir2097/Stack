import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Email:
    """
    Класс для работы с Email
    """
    def __init__(self, login_email, password_email):
        self.login_email = login_email
        self.password_email = password_email

    def send_message(self, server_smtp_email, recipients, subject, message):
        """
        Метод отправки сообщения
        :param server_smtp_email: Сервер исходящих сообщений
        :param recipients: Почта принимающих сообщений
        :param subject: Тема сообщения
        :param message: Сообщение
        :return: Сообщение отправлено
        """
        msg = MIMEMultipart()
        msg['From'] = self.login_email
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))

        mail_sender = smtplib.SMTP(server_smtp_email, 587)
        mail_sender.ehlo()
        mail_sender.starttls()
        mail_sender.ehlo()
        mail_sender.login(self.login_email, self.password_email)
        mail_sender.sendmail(self.login_email, recipients, msg.as_string())
        mail_sender.quit()

        return 'Cообщение отправлено'

    def recieve_message(self, server_imap_email, header):
        """
        Метод принятия сообщений
        :param server_imap_email: Сервер входящих сообщений
        :param header: Заголовки
        :return: Сообщение
        """
        mail_recieve = imaplib.IMAP4_SSL(server_imap_email)
        mail_recieve.login(self.login_email, self.password_email)
        mail_recieve.list()
        mail_recieve.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail_recieve.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail_recieve.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail_recieve.logout()

        return email_message


if __name__ == '__main__':
    GMAIL_SMTP = "smtp.gmail.com"
    GMAIL_IMAP = "imap.gmail.com"

    login_email = 'login@gmail.com'
    password_email = 'qwerty'
    subject = 'Subject'
    recipients = ['vasya@dir_email.com', 'petya@dir_email.com']
    message = 'Message'
    header = None
    new_mail = Email(login_email, password_email)
    new_mail.send_message(GMAIL_SMTP, recipients, subject, message)
    new_mail.recieve_message(GMAIL_IMAP, header)
