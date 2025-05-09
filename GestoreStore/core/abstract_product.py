from abc import ABC, abstractmethod

class AbstractProduct(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        """
        Property get di name.
        :return: nome del prodotto
        :rtype: str
        """
        pass

    @name.setter
    @abstractmethod
    def name(self, name: str):
        """
        Property set di name.
        :param name: str
        :return: None
        :rtype: None
        """
        pass

    @property
    @abstractmethod
    def quantity(self) -> int:
        """
        Property get di quantity.
        :return: quantità del prodotto
        :rtype: int
        """
        pass

    @quantity.setter
    @abstractmethod
    def quantity(self, quantity: str):
        """
        Property set di quantity.
        :param quantity: str
        :return: None
        :rtype: None
        """
        pass

    @property
    @abstractmethod
    def selling_price(self) -> float:
        """
        Property get di selling_price
        :return: prezzo di vendita del prodotto
        :rtype: float
        """
        pass

    @selling_price.setter
    @abstractmethod
    def selling_price(self, selling_price: str):
        """
        Property set di selling_price.
        :param selling_price: str
        :return: None
        :rtype: None
        """
        pass

    @property
    @abstractmethod
    def purchase_price(self) -> float:
        """
        Property get di purchase_price.
        :return: prezzo di acquisto del prodotto
        :rtype: float
        """
        pass

    @purchase_price.setter
    @abstractmethod
    def purchase_price(self, purchase_price: str):
        """
        Property set di purchase_price.
        :param purchase_price: str
        :return: None
        :rtype: None
        """
        pass

    @property
    @abstractmethod
    def status(self) -> str:
        """
        Property get di status.
        :return: stato del prodotto, "available" se presente in magazzino, "sold" se rappresenta una vendita
        :rtype: str
        """
        pass

    @status.setter
    @abstractmethod
    def status(self, status: str):
        """
        Property set di status.
        :param status: str
        :return: None
        :rtype: None
        """
        pass

    @staticmethod
    @abstractmethod
    def validate_price(value: str) -> float:
        """
        Metodo per la convalida del valore di input del prezzo di vendita o del prezzo di acquisto.
        :param value: str
        :return: valore convertito da str a float
        :rtype: float
        """
        pass

    @staticmethod
    @abstractmethod
    def validate_quantity(value: str) -> int:
        """
        Metodo per la convalida del valore di input della quantità del prodotto.
        :param value: str
        :return: valore convertito da str a int
        :rtype: int
        """
        pass

    @staticmethod
    @abstractmethod
    def validate_name(name: str) -> str:
        """
        Metodo per la convalida del valore di input del nome del prodotto.
        :param name: str
        :return: nome del prodotto
        :rtype: str
        """
        pass
