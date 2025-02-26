# TODO написать нормальный ридми

Трансфер из SOURCE в DESTINATION в виде библиотеки

SOURCE:

- csv (наш случай)
- slack
- discord
- tg
- ...

DESTINATION:

- postgesql (наш случай)
- clickhouse
- mongodb
- ...

SOURCE --> DESTINATION

P.S. для простой загрузки данных из csv в postges эта прога -- **overengineering**!!!!

## Команды для работы:

- Запуск окружения и установка библиотек:

```shell
python3.10 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

- Развернуть базу данных в докер-компоузе:

```shell
make start-db
make migrate-postrgress  # Создать таблицу 
```

На линухе утилиту make уже стоит, а вот про другие системы не знаю. Мб надо будет устанавливать

- Запустить скрипт:

```shell
make run-script
```

- Зайти в базу данных и посмотреть таблицу

```shell
docker-compose exec postgres psql --user admin --dbname user_data
```

и внутри написать:

```sql
SELECT * FROM user_info;

-- Чтобы выйти:
exit
```

- Остановить базу данных

```shell
make remove-db
```



