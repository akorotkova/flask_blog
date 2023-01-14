import os
import secrets
import smtplib
from flask import url_for, current_app
from PIL import Image


def save_picture(form_picture):

    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_filename = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/img', picture_filename)

    output_size_file = (125, 125)
    result_image = Image.open(form_picture)
    result_image.thumbnail(output_size_file)
    result_image.save(picture_path)

    return picture_filename


def send_reset_email(user):

    token = user.get_reset_token()
    
    sender = current_app.config['MAIL_USERNAME']
    password = current_app.config['MAIL_PASSWORD']
    server = current_app.config['MAIL_SERVER']
    port = current_app.config['MAIL_PORT']
    subject = 'Запрос на сброс пароля'
    recipient = user.email
    charset = 'Content-Type: text/plain; charset=utf-8'
    mime = 'MIME-Version: 1.0'

    text = f'''Для сброса пароля перейдите по следующей ссылке:
    {url_for('users.reset_token', token=token, _external=True)}
    Если Вы не делали запрос на сброс пароля, проигнорируйте это письмо.'''

    message = '\n'.join((f'From: {sender}', f'To: {recipient}', f'Subject: {subject}', mime, charset, '', text))

    try:
        smtp = smtplib.SMTP(server, port)
        smtp.starttls()
        smtp.ehlo()
        smtp.login(sender, password)
        smtp.sendmail(sender, recipient, message.encode('utf-8'))
    except smtplib.SMTPException as err:
        print('Что-то пошло не так...')
        raise err
    finally:
        smtp.quit()
