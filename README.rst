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

    from TempMailz import TempMailz
    
    TempMailz.getDomainList()

Создание нового ящика со случайным адресом::

    from TempMailz import TempMailz

    tm = TempMailz()

Создание нового ящика с настраeваемым адресом::

    from TempMailz import TempMailz

    tm = TempMailz(login="cotulars", domain="1secmail.com")
