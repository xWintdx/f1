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

### Переименовать  файл .env.template в env 
В файле указать своего креды для подключения к БД

### Выполнить команду
```bash
docker compose up -d
```
### Подключиться к БД и проверить данные
```bash
select count(*) from orders # 830
select count(*) from customers # 91
select version() # Версия начинается с PostgreSQL 17
```
