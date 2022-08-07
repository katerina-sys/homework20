import pytest
from unittest.mock import MagicMock
from dao.genre import GenreDAO
from dao.model.genre import Genre
from service.genre import GenreService


@pytest.fixture()
def genre_dao():
    genre = GenreDAO(None)

    comedy = Genre(id=1, name='comedy')
    adventure = Genre(id=2, name='adventure')

    genre.get_one = MagicMock(return_value=comedy)
    genre.get_all = MagicMock(return_value=[comedy, adventure])
    genre.create = MagicMock(return_value=Genre(id=2))
    genre.delete = MagicMock()
    genre.update = MagicMock()
    return genre


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)

        assert genre is not None
        assert genre.id is not None

    def test_get_all(self):
        genres = self.genre_service.get_all()

        assert len(genres) > 0

    def test_create(self):
        genre_d = {
            "id": 3,
            "name": "drama",
        }

        genre = self.genre_service.create(genre_d)

        assert genre.id is not None

    def test_delete(self):
        self.genre_service.delete(1)

    def test_update(self):
        genre_d = {
            "id": 2,
            "name": "drama",
        }

        self.genre_service.update(genre_d)
