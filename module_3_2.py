def send_email(message, recipient, sender = "university.help@gmail.com"):
    if ("@" not in recipient and "@" not in sender or
            (not recipient.endswith('.com') and not recipient.endswith('.ru') and not recipient.endswith('.net')) or
            (not sender.endswith('.com') and not sender.endswith('.ru') and not sender.endswith('.net'))):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
        return
    elif sender == 'university.help@gmail.com':
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}!")
        return
    print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')