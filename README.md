Для запуска необходимо:
1.	Скопировать репозиторий.
2.	Установить docker, если еще не установлен.
3.	Собрать контейнеры командой docker-compose build (в Linux возможно придется добавить sudo перед командой).
4.	Запустить контейнеры docker-compose up.

Приложение работает по адресу http://0.0.0.0:8080/. Для расчета числа фибоначчи в конец строки добавить целое число, например, http://0.0.0.1:8080/10.
