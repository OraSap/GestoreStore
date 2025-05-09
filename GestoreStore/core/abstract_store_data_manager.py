from abc import ABC, abstractmethod
from typing import List

class AbstractStoreDataManager(ABC):
    @staticmethod
    def validate_path() -> None:
        """
        Metodo per garantire l'esistenza del file di salvataggio nel percorso "data/store_supplies.txt".
        :return: None
        :rtype: None
        """
    @staticmethod
    @abstractmethod
    def get_supplies_from_file() -> List["Product"]:
        """
        Metodo per leggere il file dati "store_supplies.txt", e trasformarne il contenuto in una lista di Product
        :return: restituisce una lista di prodotti
        :rtype: List["Product"]
        """
        pass

    @staticmethod
    @abstractmethod
    def save_file_supplies(supplies: List["Product"]):
        """
        Metodo per il salvataggio della lista dei prodotti nel file dati "store_supplies.txt"
        :param supplies: List["Product"]
        :return: None
        :rtype: None
        """
        pass
