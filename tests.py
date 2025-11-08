import pytest

class TestBooksCollector:

    # ---------- add_new_book ----------

    @pytest.mark.parametrize('name', ['', 'A' * 41])
    def test_add_new_book_invalid_name_not_added(self, collector, name):
        collector.add_new_book(name)
        assert collector.get_books_genre() == {}

    def test_add_new_book_same_book_not_duplicated(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Гарри Поттер')
        assert collector.get_books_genre() == {'Гарри Поттер': ''}

    # ---------- set_book_genre ----------

    def test_set_book_genre_valid_genre(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert collector.get_book_genre('Гарри Поттер') == 'Фантастика'

    def test_set_book_genre_invalid_genre_not_set(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Романтика')
        assert collector.get_book_genre('Гарри Поттер') == ''

    # ---------- get_books_with_specific_genre ----------

    def test_get_books_with_specific_genre_returns_correct_books(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Оно')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Гарри Поттер']

    # ---------- get_books_for_children ----------

    def test_get_books_for_children_excludes_adult_genres(self, collector):
        collector.add_new_book('Оно')
        collector.add_new_book('Шрек')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Шрек', 'Мультфильмы')
        result = collector.get_books_for_children()
        assert 'Оно' not in result
        assert 'Шрек' in result

    # ---------- add_book_in_favorites ----------

    def test_add_book_in_favorites_adds_once(self, collector):
        collector.add_new_book('Шрек')
        collector.add_book_in_favorites('Шрек')
        collector.add_book_in_favorites('Шрек')  # повторно не добавляется
        assert collector.get_list_of_favorites_books() == ['Шрек']

    def test_add_book_in_favorites_not_existing_not_added(self, collector):
        collector.add_book_in_favorites('Несуществующая книга')
        assert collector.get_list_of_favorites_books() == []

    # ---------- delete_book_from_favorites ----------

    def test_delete_book_from_favorites_removes_book(self, collector):

        collector.add_new_book('Шрек')
        collector.add_book_in_favorites('Шрек')
        collector.delete_book_from_favorites('Шрек')
        assert 'Шрек' not in collector.get_list_of_favorites_books()

    # ---------- get_list_of_favorites_books ----------

    def test_get_list_of_favorites_books_returns_correct_list(self, collector):
        collector.add_new_book('Шрек')
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Шрек')
        assert collector.get_list_of_favorites_books() == ['Шрек']

    # ---------- get_books_genre ----------

    def test_get_books_genre_returns_all_books(self, collector):
        collector.add_new_book('Шрек')
        collector.add_new_book('Гарри Поттер')
        expected = {'Шрек': '', 'Гарри Поттер': ''}
        assert collector.get_books_genre() == expected

    # ---------- get_book_genre ----------

    def test_get_book_genre_returns_correct_genre(self, collector):
        collector.add_new_book('Шрек')
        collector.set_book_genre('Шрек', 'Мультфильмы')
        assert collector.get_book_genre('Шрек') == 'Мультфильмы'
