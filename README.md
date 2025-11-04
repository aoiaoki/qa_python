# qa_python
# Тестирование класса BooksCollector

## Реализованные тесты

| Метод | Проверка |
|--------|-----------|
| `add_new_book` | Добавление книги, ограничение длины названия, уникальность |
| `set_book_genre` | Присвоение жанра и проверка валидности |
| `get_book_genre` | Возврат установленного жанра |
| `get_books_with_specific_genre` | Фильтрация по жанру |
| `get_books_genre` | Получение полного списка книг с жанрами |
| `get_books_for_children` | Исключение жанров с возрастным рейтингом |
| `add_book_in_favorites` | Добавление без повторов |
| `delete_book_from_favorites` | Удаление из избранного |
| `get_list_of_favorites_books` | Получение списка избранных книг |

## Как запустить тесты

```bash
pytest -v tests.py
