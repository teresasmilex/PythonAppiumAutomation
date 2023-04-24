import pytest


class MainClass:
    @staticmethod
    def get_local_number() -> int:
        return 14


class TestMainClass(MainClass):
    def test_get_local_number(self):
        assert self.get_local_number() == 14, "Local number is not 14"
