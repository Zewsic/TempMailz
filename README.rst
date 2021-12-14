TempMailz
=========

Модуль для Python для работы с временной почтой.

Требования
------------

`requests <https://crate.io/packages/requests/>`_ - обязателен.

Установка
------------

Установка через PIP::

    $ pip install TempMailz

Использование
-----

Получить список доступных доменов::

    from TempMailz import TempMailz as tmz
    
    tmz.TempMailz.getDomainList()

Создание нового ящика со случайным адресом::

    from TempMailz import TempMailz as tmz

    tm = tmz.TempMailz()

Создание нового ящика с настраeваемым адресом::

    from TempMailz import TempMailz as tmz

    tm = tmz.TempMailz(login="cotulars", domain="1secmail.com")

Получить список сообщений с почтового ящика::

    from TempMailz import TempMailz as tmz

    tm = tmz.TempMailz()
    inbox = tm.get_inbox()

Получить информацию о сообщении с почтового ящика::

    from TempMailz import TempMailz as tmz

    tm = tmz.TempMailz()
    msg = tm.get_msg(347165998)
    
Получать информацию о сообщениях при их поступлении:

    from TempMailz import TempMailz as tmz

    tm = tmz.TempMailz()
    
    for msg in tm.listen(): print(msg)
    
