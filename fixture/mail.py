
import poplib
import email
import time

class MailHelper:

    def __init__(self, app):
        self.app = app

    def get_mail(self, username, password, subject):
        for i in range(5):
            pop = poplib.POP3(self.app.config['james']['host'])
            pop.user(username)
            pop.pass_(password)
            number_of_letters = pop.stat()[0]                #возвращаем информацию о том, что сейчас имеется в почтовом ящике, первый элемент кортежа - это количество писем
            if number_of_letters > 0:
                for n in range(number_of_letters):
                    msg_lines = pop.retr(n+1)[1]             #возвращаем кортеж с тестом письма, который находится в первом элементе кортежа
                    msg_text = '\n'.join(map(lambda x: x.decode('utf-8'), msg_lines))         #msg_lines это список байтовых строк, поэтому джоиним их, потом перекодируем их в utf-8
                    msg = email.message_from_string(msg_text)
                    if msg.get('Return-Path') == subject:
                        pop.dele(n+1)                        # помечаем это письмо на удаление
                        pop.close()
                        return msg.get_payload()
            pop.close()
            time.sleep(3)
        return None