# mail-sender
## Mail Sender: платформа организации рассылок

### Использованные технологии:
- python==2.7.18
- celery==4.4.7
- Django==1.11.29
- redis==3.5.3

### Устновка:
```python
git clone https://github.com/Viva-Fidel/mail-sender.git
pip install -r requirements.txt
```
В файле <b>mail-sender/config.py</b> необходимо ввести секретный ключ Django и данные SMTP сервера

### Функционал:
Добавление подписчика:  
![Screenshot from 2023-07-16 16-36-02](https://github.com/Viva-Fidel/mail-sender/assets/98227548/c2fad978-d4d5-47f2-884f-b2681290a999)

Создание рассылок, в том числе с отображением в реальном времени того, как выглядит шаблон.  
Также позволяет организовывать отложенные рассылки - для этого необходимо нажать на поле "Дата отправки", чтобы выбрать дату и нажать на иконку часов, чтобы выбрать часы и минуты.
![Screenshot from 2023-07-16 16-36-38](https://github.com/Viva-Fidel/mail-sender/assets/98227548/8d25d9e1-407c-4a44-98bb-6ab6fa13f65f)
#### Для того, чтобы создать персонализированную рассылку, в письмо необходимо вставить следующие тэги:
- Имя: {{ first_name }}
- Фамилия: {{ last_name }}
- Дата рождения: {{ date_of_birth }}

Получение статистики по рассылкам. Проверка открытия письма осуществляется через вставку ссылки в письмо, либо через вставку белого пикселя:
![Screenshot from 2023-07-16 16-36-55](https://github.com/Viva-Fidel/mail-sender/assets/98227548/9c7f1d72-2798-4bba-b3f0-5753b0ef9251)

### Дополнительный функционал:
Валидирует формы, на наличие ошибок, либо сообщает, что всё прошло успешно.
![Screenshot from 2023-07-16 16-45-34](https://github.com/Viva-Fidel/mail-sender/assets/98227548/24d6c668-a707-4aa4-94da-bc106142a25a)
![Screenshot from 2023-07-16 16-45-53](https://github.com/Viva-Fidel/mail-sender/assets/98227548/670bb046-1ead-4126-8b80-7d55b473af0c)



