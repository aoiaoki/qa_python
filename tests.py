from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    from main import BooksCollector

    class TestBooksCollector:

        # ---------- add_new_book ----------

        def test_add_new_book_invalid_name_not_added(self):
            collector = BooksCollector()
            collector.add_new_book('')  # пустое имя не добавится
            collector.add_new_book('A' * 41)  # слишком длинное имя не добавится

            assert len(collector.get_books_genre()) == 0

        def test_add_new_book_same_book_not_duplicated(self):
            collector = BooksCollector()
            collector.add_new_book('Гарри Поттер')
            collector.add_new_book('Гарри Поттер')

            assert len(collector.get_books_genre()) == 1

        # ---------- set_book_genre ----------

        def test_set_book_genre_valid_genre(self):
            collector = BooksCollector()
            collector.add_new_book('Гарри Поттер')
            collector.set_book_genre('Гарри Поттер', 'Фантастика')

            assert collector.get_book_genre('Гарри Поттер') == 'Фантастика'

        def test_set_book_genre_invalid_genre_not_set(self):
            collector = BooksCollector()
            collector.add_new_book('Гарри Поттер')
            collector.set_book_genre('Гарри Поттер', 'Романтика')

            assert collector.get_book_genre('Гарри Поттер') == ''

        # ---------- get_books_with_specific_genre ----------

        def test_get_books_with_specific_genre_returns_correct_books(self):
            collector = BooksCollector()
            collector.add_new_book('Гарри Поттер')
            collector.add_new_book('Оно')
            collector.set_book_genre('Гарри Поттер', 'Фантастика')
            collector.set_book_genre('Оно', 'Ужасы')

            result = collector.get_books_with_specific_genre('Фантастика')
            assert result == ['Гарри Поттер']

        # ---------- get_books_for_children ----------

        def test_get_books_for_children_excludes_adult_genres(self):
            collector = BooksCollector()
            collector.add_new_book('Оно')
            collector.add_new_book('Шрек')
            collector.set_book_genre('Оно', 'Ужасы')
            collector.set_book_genre('Шрек', 'Мультфильмы')

            result = collector.get_books_for_children()
            assert 'Оно' not in result
            assert 'Шрек' in result

        # ---------- add_book_in_favorites ----------

        def test_add_book_in_favorites_adds_once(self):
            collector = BooksCollector()
            collector.add_new_book('Шрек')
            collector.add_book_in_favorites('Шрек')
            collector.add_book_in_favorites('Шрек')  # повторно не добавляется

            assert collector.get_list_of_favorites_books() == ['Шрек']

        def test_add_book_in_favorites_not_existing_not_added(self):
            collector = BooksCollector()
            collector.add_book_in_favorites('Несуществующая книга')
            assert collector.get_list_of_favorites_books() == []

        # ---------- delete_book_from_favorites ----------

        def test_delete_book_from_favorites_removes_book(self):
            collector = BooksCollector()
            collector.add_new_book('Шрек')
            collector.add_book_in_favorites('Шрек')
            collector.delete_book_from_favorites('Шрек')

            assert 'Шрек' not in collector.get_list_of_favorites_books()
