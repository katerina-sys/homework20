import pytest
from unittest.mock import MagicMock
from dao.movie import MovieDAO
from dao.model.movie import Movie
from service.movie import MovieService


@pytest.fixture()
def movie_dao():
    movie = MovieDAO(None)

    movie_1 = Movie(id=1, title='comedy', description='test', trailer='test', year=2000, rating=4.5,
                    genre_id=1, director_id=1)
    movie_2 = Movie(id=2, title='adventure', description='test1', trailer='test1', year=2001, rating=4.5,
                    genre_id=2, director_id=2)

    movie.get_one = MagicMock(return_value=movie_1)
    movie.get_all = MagicMock(return_value=[movie_1, movie_2])
    movie.create = MagicMock(return_value=Movie(id=2))
    movie.delete = MagicMock()
    movie.update = MagicMock()
    return movie


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(movie_dao)

    def test_get_one(self):
        assert self.movie_service.get_one(1) is not None
        assert self.movie_service.get_one(1).title == 'comedy'

    def test_get_all(self):
        movies = self.movie_service.get_all()

        assert len(movies) > 0

    def test_create(self):
        movie_d = {
            "id": 3,
            "title": "drama",
            "description": "tests",
            "trailer": "tests1",
            "year": 2003,
            "rating": 5.0,
            "genre_id": 3,
            "director_id": 3,
        }

        movie = self.movie_service.create(movie_d)

        assert movie.id is not None

    def test_delete(self):
        self.movie_service.delete(1)

    def test_update(self):
        movie_d = {
            "id": 2,
            "title": "drama",
        }

        self.movie_service.update(movie_d)
