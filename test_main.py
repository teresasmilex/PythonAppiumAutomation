import pytest


class MainClass:
    __class_number = 20
    __class_string = "Hello, world"

    def get_class_number(self) -> int:
        return self.__class_number

    def get_class_string(self) -> str:
        return self.__class_string

    @staticmethod
    def get_local_number() -> int:
        return 14


class TestMainClass(MainClass):
    def test_get_local_number(self):
        assert self.get_local_number() == 14, "Local number is not 14"

    def test_get_class_number(self):
        if self.get_class_number() > 45:
            pass
        elif self.get_class_number() == 45:
            raise Exception("Class number is 45")
        elif self.get_class_number() < 45:
            raise Exception("Class number is less than 45")

    def test_get_class_string(self):
        assert "hello" in self.get_class_string() or \
               "Hello" in self.get_class_string(),\
            "String doesn't contain a greeting"

