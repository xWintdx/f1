# F1

Это проект, посвященный анализу конвертации поулов в победы в рамках Формулы 1

## Установка

### Склонировать репозиторий
```bash
git clone https://github.com/xWintdx/f1.git
```

### Сначала необходимо установить uv
Гайд:
https://docs.astral.sh/uv/getting-started/installation/


### Выполнить сихронизацию
```bash
uv sync
```

### Прогнать pytest
```bash
uv run pytest
```

### Подготовить файл .env
1) Скопировать существующий файл .env.template
2) Изменить имя (Удалить .template)
3) В файле указать своего креды для подключения к БД

### Выполнить команду
```bash
docker compose up -d
```
### Подключиться к БД и проверить данные
```psql
postgresql://пользователь:пароль@localhost:5432/база
```
```sql
select count(*) from orders; -- 830
select count(*) from customers; -- 91
select version(); -- Версия начинается с PostgreSQL 17
```
### Для сброса данных использовать 
```bash
docker compose down -v
```
