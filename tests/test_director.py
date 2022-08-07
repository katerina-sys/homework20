import pytest

from unittest.mock import MagicMock
from dao.director import DirectorDAO
from dao.model.director import Director
from service.director import DirectorService


@pytest.fixture()
def director_dao():
    director = DirectorDAO(None)

    john = Director(id=1, name='john')
    kate = Director(id=2, name='kate')
    max = Director(id=3, name='max')

    director.get_one = MagicMock(return_value=john)
    director.get_all = MagicMock(return_value=[john, kate, max])
    director.create = MagicMock(return_value=Director(id=3))
    director.delete = MagicMock()
    director.update = MagicMock()
    return director


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)

        assert director is not None
        assert director.id is not None

    def test_get_all(self):
        directors = self.director_service.get_all()

        assert len(directors) > 0

    def test_create(self):
        director_d = {
            "id": 4,
            "name": "Ivan",
        }

        director = self.director_service.create(director_d)

        assert director.id is not None

    def test_delete(self):
        self.director_service.delete(1)

    def test_update(self):
        director_d = {
            "id": 3,
            "name": "Ivan",
        }

        self.director_service.update(director_d)
