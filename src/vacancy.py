from abc import ABC, abstractmethod


class BaseJsonVacancy(ABC):

    @abstractmethod
    def dict_form(self):
        pass

    @abstractmethod
    def dict_to_json(self):
        pass

