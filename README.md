Markdown

# 📄 CV Scoring App

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.53.0-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-412991?style=for-the-badge&logo=openai&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**Интеллектуальная система оценки соответствия резюме требованиям вакансии**
---

</div>

## 📋 Содержание

- [О проекте](#-о-проекте)
- [Возможности](#-возможности)
- [Демонстрация](#-демонстрация)
- [Технологии](#️-технологии)
- [Структура проекта](#-структура-проекта)
- [Быстрый старт](#-быстрый-старт)
- [Локальная установка](#-локальная-установка)
- [Деплой на Streamlit Cloud](#-деплой-на-streamlit-cloud)
- [Использование](#-использование)
- [Конфигурация](#️-конфигурация)
- [API Reference](#-api-reference)
- [Решение проблем](#-решение-проблем)
- [Дорожная карта](#️-дорожная-карта)

---

## 🎯 О проекте

**CV Scoring App** — это веб-приложение на базе искусственного интеллекта, которое автоматически анализирует соответствие кандидата требованиям вакансии. Приложение парсит данные с сайта hh.ru и использует GPT-4o-mini для глубокого анализа.

### Зачем это нужно?

- ⏱️ **Экономия времени** — автоматический анализ вместо ручного сравнения
- 🎯 **Объективность** — стандартизированная оценка по единым критериям
- 📊 **Детальный анализ** — не просто оценка, а подробное обоснование
- 💡 **Оценка качества резюме** — понимание, насколько кандидат умеет презентовать себя

---

## ✨ Возможности

| Функция | Описание |
|---------|----------|
| 🔍 **Парсинг вакансий** | Автоматическое извлечение данных вакансии с hh.ru/hh.kz |
| 📋 **Парсинг резюме** | Извлечение информации о кандидате, опыте, навыках |
| 🤖 **AI-анализ** | Глубокий анализ соответствия с использованием GPT-4o-mini |
| 📊 **Скоринг** | Оценка кандидата по шкале от 1 до 10 |
| 📝 **Оценка резюме** | Анализ качества заполнения и самопрезентации |
| 🔒 **Безопасность** | API-ключи хранятся в защищённых переменных окружения |

---

## 🖥️ Демонстрация

### Интерфейс приложения
┌─────────────────────────────────────────────────────────────┐
│ 📄 CV Scoring App │
│ Автоматическая оценка соответствия резюме вакансии │
├─────────────────────────────────────────────────────────────┤
│ │
│ 🔗 Ссылка на вакансию (hh.ru): │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ https://hh.ru/vacancy/123456789 │ │
│ └─────────────────────────────────────────────────────┘ │
│ │
│ 🔗 Ссылка на резюме (hh.ru): │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ https://hh.ru/resume/abc123def456 │ │
│ └─────────────────────────────────────────────────────┘ │
│ │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ 🔍 Проанализировать соответствие │ │
│ └─────────────────────────────────────────────────────┘ │
│ │
├─────────────────────────────────────────────────────────────┤
│ ✅ Анализ завершён! │
│ │
│ 📊 Результат анализа: │
│ ───────────────────────────────────────────────────────── │
│ Кандидат имеет релевантный опыт в... │
│ Качество резюме: хорошо структурировано... │
│ │
│ Итоговая оценка: 8/10 │
└─────────────────────────────────────────────────────────────┘

text


---

## 🛠️ Технологии

<div align="center">

| Технология | Назначение | Версия |
|:----------:|:-----------|:------:|
| ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white) | Язык программирования | 3.9+ |
| ![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white) | Веб-фреймворк | 1.53.0 |
| ![OpenAI](https://img.shields.io/badge/-OpenAI-412991?style=flat-square&logo=openai&logoColor=white) | AI/ML API | 2.16.0+ |
| ![BeautifulSoup](https://img.shields.io/badge/-BeautifulSoup4-43B02A?style=flat-square&logo=python&logoColor=white) | Парсинг HTML | 4.11.0+ |
| ![Requests](https://img.shields.io/badge/-Requests-2496ED?style=flat-square&logo=python&logoColor=white) | HTTP-клиент | 2.28.0+ |

</div>

---

## 📁 Структура проекта
cv-scoring-app/
│
├── 📄 streamlit_app.py          # Главный файл приложения
│   ├── Конфигурация OpenAI
│   ├── Системный промпт для GPT
│   ├── Функции запросов к API
│   └── Пользовательский интерфейс
│
├── 📄 parse_hh.py               # Модуль парсинга hh.ru
│   ├── get_html()              # Получение HTML страницы
│   ├── extract_vacancy_data()  # Парсинг вакансий
│   └── extract_resume_data()   # Парсинг резюме
│
├── 📄 requirements.txt          # Зависимости Python
├── 📄 .gitignore               # Игнорируемые файлы Git
└── 📄 README.md                # Документация проекта

text


---

## ⚡ Быстрый старт

```bash
# Клонирование репозитория
git clone https://github.com/YOUR_USERNAME/cv-scoring-app.git
cd cv-scoring-app

# Установка зависимостей
pip install -r requirements.txt

# Настройка API ключа
export OPENAI_API_KEY="sk-your-api-key-here"

# Запуск приложения
streamlit run streamlit_app.py

```
## 💻 Локальная установка
```bash
Предварительные требования
Python 3.9 или выше
pip (менеджер пакетов Python)
API ключ OpenAI (получить здесь)
Пошаговая установка
1. Клонируйте репозиторий
Bash

git clone https://github.com/YOUR_USERNAME/cv-scoring-app.git
cd cv-scoring-app
2. Создайте виртуальное окружение
Bash

# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
3. Установите зависимости
Bash

pip install -r requirements.txt
4. Настройте API ключ
Вариант A: Переменная окружения

Bash

# Windows (CMD)
set OPENAI_API_KEY=sk-your-api-key-here

# Windows (PowerShell)
$env:OPENAI_API_KEY="sk-your-api-key-here"

# macOS/Linux
export OPENAI_API_KEY="sk-your-api-key-here"
Вариант B: Файл secrets.toml

Bash

# Создайте директорию и файл
mkdir .streamlit
Создайте файл .streamlit/secrets.toml:

toml

OPENAI_API_KEY = "sk-your-api-key-here"
5. Запустите приложение
Bash

streamlit run streamlit_app.py
Приложение откроется по адресу: http://localhost:8501
```
## ☁️ Деплой на Streamlit Cloud
```bash
Шаг 1: Подготовка репозитория
Убедитесь, что в репозитории есть все необходимые файлы:

✅ streamlit_app.py
✅ parse_hh.py
✅ requirements.txt
✅ .gitignore
Шаг 2: Деплой
Перейдите на share.streamlit.io
Войдите через GitHub
Нажмите "New app"
Выберите репозиторий cv-scoring-app
Укажите главный файл: streamlit_app.py
Шаг 3: Настройка Secrets
В разделе "Advanced settings" → "Secrets" добавьте:

toml

OPENAI_API_KEY = "sk-your-actual-api-key"
Шаг 4: Запуск
Нажмите "Deploy!" и дождитесь завершения сборки (1-3 минуты).
```
## 📖 Использование
```bash
Основной процесс
Откройте приложение в браузере

Вставьте ссылку на вакансию с hh.ru

text

https://hh.ru/vacancy/123456789
Вставьте ссылку на резюме с hh.ru

text

https://hh.ru/resume/abc123def456
Нажмите "Проанализировать соответствие"

Получите результат:

Детальный анализ соответствия
Оценка качества резюме
Итоговый балл от 1 до 10
Поддерживаемые ссылки
Тип	Формат
Вакансия	https://hh.ru/vacancy/XXXXXXXXX
Вакансия (kz)	https://hh.kz/vacancy/XXXXXXXXX
Резюме	https://hh.ru/resume/XXXXXXXXXXXXX
Резюме (kz)	https://hh.kz/resume/XXXXXXXXXXXXX
```
## ⚙️ Конфигурация
```bash
Переменные окружения
Переменная	Описание	Обязательно
OPENAI_API_KEY	API ключ OpenAI	✅
Настройки модели GPT
Настройки находятся в файле streamlit_app.py:

Python

response = client.chat.completions.create(
    model="gpt-4o-mini",   # Модель GPT
    max_tokens=1000,       # Максимальная длина ответа
    temperature=0,         # Детерминированность (0 = точный)
)
Системный промпт
Промпт можно изменить в переменной SYSTEM_PROMPT:

Python

SYSTEM_PROMPT = """
Проскорь кандидата, насколько он подходит для данной вакансии.
...
"""
```
## 📚 API Reference
```bash
 parse_hh.py
get_html(url: str) -> requests.Response
Получает HTML-страницу по URL.

Python

from parse_hh import get_html

response = get_html("https://hh.ru/vacancy/123456")
html_content = response.text
extract_vacancy_data(html: str) -> str
Извлекает данные вакансии в формате Markdown.

Python

from parse_hh import extract_vacancy_data

vacancy_markdown = extract_vacancy_data(html_content)
extract_resume_data(html: str) -> str
Извлекает данные резюме в формате Markdown.

Python

from parse_hh import extract_resume_data

resume_markdown = extract_resume_data(html_content)
streamlit_app.py
request_gpt(system_prompt: str, user_prompt: str) -> str
Отправляет запрос к OpenAI API.

Python

result = request_gpt(
    system_prompt="Ты HR-эксперт",
    user_prompt="Проанализируй кандидата..."
)
validate_url(url: str, expected_type: str) -> bool
Проверяет валидность URL.

Python

is_valid = validate_url("https://hh.ru/vacancy/123", "vacancy")  # True
```
## 🔧 Решение проблем
#### Частые ошибки
```bash
<details> <summary><b>❌ API ключ не найден</b></summary>
Проблема: API ключ OpenAI не найден!

Решение:
Проверьте, что ключ добавлен в Secrets (Streamlit Cloud) или в переменные окружения
Убедитесь в правильности формата: OPENAI_API_KEY = "sk-..."
Перезапустите приложение

</details><details> <summary><b>❌ Ошибка парсинга страницы</b></summary>
Проблема: Произошла ошибка при парсинге

Решение:
Проверьте, что страница доступна в браузере
Убедитесь, что резюме/вакансия публичны
Попробуйте другую ссылку


</details><details> <summary><b>❌ ModuleNotFoundError</b></summary>
Проблема: ModuleNotFoundError: No module named 'xxx'

Решение:
pip install -r requirements.txt


</details><details> <summary><b>❌ Rate Limit Exceeded</b></summary>
Проблема: Превышен лимит запросов к OpenAI

Решение:
Подождите несколько минут
Проверьте баланс на platform.openai.com
Используйте другой API ключ
</details>
```
## 🗺️ Дорожная карта
```bash
 Базовый функционал парсинга
 Интеграция с OpenAI GPT
 Веб-интерфейс на Streamlit
 Поддержка других job-сайтов (SuperJob, Работа.ру)
 Пакетная обработка нескольких резюме
 Экспорт результатов в PDF
 История анализов
 Сравнение нескольких кандидатов
```










