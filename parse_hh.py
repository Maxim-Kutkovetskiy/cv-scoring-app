"""
Модуль для парсинга данных с сайта hh.ru (вакансии и резюме).

Функции:
- get_html: Получение HTML-страницы по URL
- extract_vacancy_data: Извлечение данных вакансии
- extract_resume_data: Извлечение данных резюме
"""

import requests
from bs4 import BeautifulSoup
from typing import Optional

# =============================================================================
# КОНСТАНТЫ
# =============================================================================

# User-Agent для имитации браузера (обход базовой защиты от ботов)
DEFAULT_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
}

# Таймаут запроса в секундах
REQUEST_TIMEOUT = 10


# =============================================================================
# ФУНКЦИИ ПОЛУЧЕНИЯ HTML
# =============================================================================

def get_html(url: str) -> requests.Response:
    """
    Получает HTML-страницу по указанному URL.

    Args:
        url: URL страницы для загрузки

    Returns:
        Объект Response с HTML-содержимым

    Raises:
        requests.RequestException: При ошибках сетевого запроса
        requests.HTTPError: При HTTP-ошибках (4xx, 5xx)
    """
    response = requests.get(
        url,
        headers=DEFAULT_HEADERS,
        timeout=REQUEST_TIMEOUT
    )
    # Вызывает исключение при HTTP-ошибках
    response.raise_for_status()
    return response


# =============================================================================
# ПАРСИНГ ВАКАНСИЙ
# =============================================================================

def extract_vacancy_data(html: str) -> str:
    """
    Извлекает данные вакансии из HTML и форматирует в Markdown.

    Args:
        html: HTML-код страницы вакансии

    Returns:
        Отформатированная строка в формате Markdown с данными вакансии
    """
    soup = BeautifulSoup(html, 'html.parser')

    def safe_text(selector: str, attrs: Optional[dict] = None) -> str:
        """
        Безопасно извлекает текст из HTML-элемента.

        Args:
            selector: HTML-тег для поиска
            attrs: Словарь атрибутов для фильтрации

        Returns:
            Текст элемента или "Не найдено" если элемент отсутствует
        """
        element = soup.find(selector, attrs or {})
        return element.text.strip() if element else "Не найдено"

    # Извлекаем основные поля вакансии
    title = safe_text('h1', {'data-qa': 'vacancy-title'})
    salary = safe_text('span', {'data-qa': 'vacancy-salary-compensation-type-net'})

    # Альтернативный селектор для зарплаты (структура может отличаться)
    if salary == "Не найдено":
        salary = safe_text('span', {'data-qa': 'vacancy-salary'})

    company = safe_text('a', {'data-qa': 'vacancy-company-name'})

    # Извлекаем описание вакансии
    description_element = soup.find('div', {'data-qa': 'vacancy-description'})
    description_text = (
        description_element.get_text(separator="\n").strip()
        if description_element
        else "Описание не найдено"
    )

    # Извлекаем ключевые навыки (если есть)
    skills_section = soup.find('div', {'data-qa': 'skills-element'})
    skills = []
    if skills_section:
        skill_tags = skills_section.find_all('span', {'data-qa': 'bloko-tag__text'})
        skills = [tag.text.strip() for tag in skill_tags]

    # Формируем Markdown-документ
    markdown = f"# {title}\n\n"
    markdown += f"**Компания:** {company}\n\n"
    markdown += f"**Зарплата:** {salary}\n\n"

    if skills:
        markdown += f"**Ключевые навыки:** {', '.join(skills)}\n\n"

    markdown += f"## Описание\n\n{description_text}"

    return markdown.strip()


# =============================================================================
# ПАРСИНГ РЕЗЮМЕ
# =============================================================================

def extract_resume_data(html: str) -> str:
    """
    Извлекает данные резюме из HTML и форматирует в Markdown.

    Args:
        html: HTML-код страницы резюме

    Returns:
        Отформатированная строка в формате Markdown с данными резюме
    """
    soup = BeautifulSoup(html, 'html.parser')

    def safe_text(selector: str, **kwargs) -> str:
        """
        Безопасно извлекает текст из HTML-элемента с произвольными атрибутами.

        Args:
            selector: HTML-тег для поиска
            **kwargs: Атрибуты для фильтрации (например, data_qa='value')

        Returns:
            Текст элемента или "Не найдено" если элемент отсутствует
        """
        # Преобразуем data_qa в data-qa для корректного поиска
        attrs = {k.replace('_', '-'): v for k, v in kwargs.items()}
        element = soup.find(selector, attrs)
        return element.text.strip() if element else "Не найдено"

    # Извлекаем основную информацию о кандидате
    name = safe_text('h2', data_qa='bloko-header-1')

    # Альтернативный поиск имени
    if name == "Не найдено":
        name_element = soup.find('h2', {'data-qa': 'bloko-header-1'})
        if name_element:
            name = name_element.text.strip()

    gender_age = safe_text('p')
    location = safe_text('span', data_qa='resume-personal-address')
    job_title = safe_text('span', data_qa='resume-block-title-position')
    job_status = safe_text('span', data_qa='job-search-status')

    # Извлекаем опыт работы
    experiences = []
    experience_section = soup.find('div', {'data-qa': 'resume-block-experience'})

    if experience_section:
        # Находим все блоки с опытом работы
        experience_items = experience_section.find_all(
            'div',
            class_='resume-block-item-gap'
        )

        for item in experience_items:
            try:
                # Период работы
                period_element = item.find('div', class_='bloko-column_s-2')
                period = period_element.text.strip() if period_element else "Период не указан"

                # Длительность
                duration_element = item.find('div', class_='bloko-text')
                if duration_element:
                    duration = duration_element.text.strip()
                    period = period.replace(duration, f" ({duration})")

                # Название компании
                company_element = item.find('div', class_='bloko-text_strong')
                company = company_element.text.strip() if company_element else "Компания не указана"

                # Должность
                position_element = item.find(
                    'div',
                    {'data-qa': 'resume-block-experience-position'}
                )
                position = position_element.text.strip() if position_element else "Должность не указана"

                # Описание обязанностей
                desc_element = item.find(
                    'div',
                    {'data-qa': 'resume-block-experience-description'}
                )
                description = desc_element.text.strip() if desc_element else "Описание отсутствует"

                # Формируем блок опыта
                exp_block = f"**{period}**\n\n"
                exp_block += f"*{company}*\n\n"
                exp_block += f"**{position}**\n\n"
                exp_block += f"{description}\n"

                experiences.append(exp_block)

            except Exception:
                # Пропускаем элементы, которые не удалось распарсить
                continue

    # Извлекаем ключевые навыки
    skills = []
    skills_section = soup.find('div', {'data-qa': 'skills-table'})

    if skills_section:
        skill_tags = skills_section.find_all('span', {'data-qa': 'bloko-tag__text'})
        skills = [tag.text.strip() for tag in skill_tags]

    # Извлекаем образование (опционально)
    education = []
    education_section = soup.find('div', {'data-qa': 'resume-block-education'})

    if education_section:
        edu_items = education_section.find_all('div', class_='resume-block-item-gap')
        for item in edu_items:
            try:
                edu_text = item.get_text(separator=" ").strip()
                if edu_text:
                    education.append(edu_text)
            except Exception:
                continue

    # Формируем Markdown-документ
    markdown = f"# {name}\n\n"
    markdown += f"**{gender_age}**\n\n"
    markdown += f"**Местоположение:** {location}\n\n"
    markdown += f"**Желаемая должность:** {job_title}\n\n"
    markdown += f"**Статус:** {job_status}\n\n"

    # Опыт работы
    markdown += "## Опыт работы\n\n"
    if experiences:
        markdown += "\n---\n".join(experiences)
    else:
        markdown += "Опыт работы не найден.\n"

    # Ключевые навыки
    markdown += "\n## Ключевые навыки\n\n"
    if skills:
        markdown += ", ".join(skills)
    else:
        markdown += "Навыки не указаны."

    # Образование (если есть)
    if education:
        markdown += "\n\n## Образование\n\n"
        markdown += "\n".join(education)

    return markdown.strip()