from .product import Product
from .store_data_manager import DM
from .abstract_store import AbstractStore
import copy
from typing import List, Union

class Store(AbstractStore):
    def __init__(self):
        """
        - Tramite la property supplies, inizializzo la variabile di istanza self.__supplies con la lista dei prodotti salvati nel file.
          Ogni transazione aggiorna il file per non perdere informazioni a causa di interruzioni inaspettate
          non gestibili dal programma.
        - Inizializzo la variabile di istanza self.__queries con il dizionario contenete i comandi dell'utente.
        """
        self.supplies = DM.get_supplies_from_file()
        self.__queries = {
            "aggiungi": "aggiungi un prodotto al magazzino",
            "elenca": "elenca i prodotti in magazzino",
            "vendita": "registra una vendita effettuata",
            "profitti": "mostra i profitti totali",
            "aiuto": "mostra i comandi disponibili",
            "chiudi": "esci dal programma"
        }
    #region properties
    @property
    def supplies(self) -> List["Product"]:
        return self.__supplies
    @supplies.setter
    def supplies(self, products: List["Product"]) -> None:
        self.__supplies = products

    @property
    def queries(self) -> dict:
        return self.__queries
    #endregion properties

    #region inherited methods
    def add_query(self) -> None:
        """
        Implementazione:
        Ottengo nome e quantità del prodotto da inserire.
        Se il prodotto è già esistente incremento la disponibilità in magazzino.
        Se il prodotto non è presente nel magazzino ottengo anche i prezzi di acquisto e vendita e inserisco il prodotto in magazzino.
        Aggiorno il file.
        """
        name = self._get_product_input("name", "Nome del prodotto: ")
        product_index = self._get_product_index(name)
        quantity = self._get_product_input("quantity", "Quantità: ")
        if product_index == -1:
            purchase_price = self._get_product_input("purchase_price", "Prezzo di acquisto: ")
            selling_price = self._get_product_input("selling_price", "Prezzo di vendita: ")
            product = Product(name, quantity, selling_price, purchase_price)
            self.supplies.append(product)
        else:
            self.supplies[product_index].quantity += quantity
        print(f"AGGIUNTO: {quantity} X {name}")
        DM.save_file_supplies(self.supplies)

    def sell_query(self) -> None:
        """
        Implementazione:
        Se ci sono prodotti da vendere nel magazzino procedo con l'esecuzione del metodo.
        Ottengo nome e quantità del prodotto da vendere.
        Verifico l'esistenza del prodotto, se presente proseguo con la vendita.
        Se il magazzino dispone della quantità richiesta procedo con la vendita e aggiorno il file.
        Se la quantità eccede la disponibilità in magazzino annullo la vendita.
        Se il magazzino non ha più prodotti da vendere concludo le vendite, altrimenti chiedo all'utente se vuole continuare.
        Se l'utente vuole vendere un altro prodotto eseguo i passaggi precedenti, altrimenti mostro il totale delle vendite effettuate.
        Il totale delle vendite si riferisce alla sessione di vendita attuale, gestita tramite la lista sell_session[].
        """
        if len(self._get_available_products()) == 0:
            print("Non ci sono prodotti nel magazzino.")
            return
        sell_session = []
        while True:
            name = self._get_product_input("name", "Nome del prodotto: ")
            product_index = self._get_product_index(name)
            if product_index == -1:
                print("Il prodotto selezionato non è presente nel magazzino.")
            else:
                quantity = self._get_product_input("quantity", f"Quantità [max {self.supplies[product_index].quantity}]: ")
                diff = self.supplies[product_index].quantity - quantity
                if diff == 0:
                    self.supplies[product_index].status = "sold"
                    sell_session.append(self.supplies[product_index])
                    DM.save_file_supplies(self.supplies)
                elif diff > 0:
                    self.supplies[product_index].quantity -= quantity
                    sold_product = copy.copy(self.supplies[product_index])
                    sold_product.status = "sold"
                    sold_product.quantity = quantity
                    self.supplies.append(sold_product)
                    sell_session.append(sold_product)
                    DM.save_file_supplies(self.supplies)
                else:
                    print(f"Sono disponibili solo {self.supplies[product_index].quantity} unità per questo prodotto. Vendita annullata.")

            if len(self._get_available_products()) == 0:
                break
            keep_selling = ""
            while keep_selling not in ("si","no"):
                keep_selling = input("Aggiungere un altro prodotto? (si/no):").strip()
            if keep_selling == "no":
                break
        print("VENDITA REGISTRATA")
        if len(sell_session)==0:
            print("Nessuna vendita registrata")
        else:
            total = 0
            for i in sell_session:
                total += i.selling_price * i.quantity
                print(f"- {i.quantity} X {i.name}: €{i.selling_price:.2f}")
            print(f"Totale: €{total:.2f}")

    def list_query(self) -> None:
        """
        Implementazione:
        Mostro all'utente la lista dei prodotti disponibili in magazzino.
        """
        print(f"PRODOTTO\tQUANTITA'\tPREZZO")
        for i in self._get_available_products():
            print(f"{i.name}\t{i.quantity}\t€{i.selling_price}")

    def profit_query(self) -> None:
        """
        Implementazione:
        Dalla lista dei prodotti filtro tutti i prodotti in status "sold" e calcolo il profitto lordo e netto.
        """
        sell_sum = 0
        purchase_sum = 0
        for i in list(filter(lambda x: x.status == "sold",self.supplies)):
            sell_sum += i.selling_price * i.quantity
            purchase_sum += i.purchase_price * i.quantity
        print(f"Profitto: lordo=€{sell_sum:.2f} netto=€{(sell_sum-purchase_sum):.2f}")

    def help_query(self) -> None:
        """
        Implementazione:
        Scorro il dizionario dei comandi e costruisco il print con key (nome comando) -> value (descrizione comando)
        """
        print("\nI comandi disponibili sono i seguenti:")
        for i in list(self.queries.keys()):
            print(f"{i}: {self.queries[i]}")

    def _get_product_index(self, name: str) -> int:
        """
        Implementazione:
        Numero i componenti della lista dei prodotti per ottenere l'indice del prodotto richiesto se in status available.
        Se il prodotto non esiste restituisco -1.
        """
        for idx, i in enumerate(self.supplies):
            if i.name == name and i.status == "available":
                return idx
        return -1

    def _get_product_input(self, info: str, msg: str) -> Union[int, float, str]:
        """
        Implementazione:
        Tramite il parametro info ricevo l'informazione sul prodotto che devo richiedere all'utente.
        Info può essere solo "name", "quantity", "selling_price" e "purchase_price".
        Il metodo è privato quindi non c'è la possibilità che info non sia tra i valori elencati.
        E' comunque presente un assert per evitare bug in fase di sviluppo.
        La validazione dell'input è una logica che riguarda i campi del prodotto e in quanto tale viene gestita
        dalla classe Product con i suoi metodi statici.
        L'input viene richiesto fin quando non viene inserito un valore corretto.
        I metodi di validazione informano l'utente di eventuali errori, come ad esempio l'inserimento di un valore
        negativo per la quantità, o come l'inserimento di un valore non numerico per il prezzo.
        Il metodo restituisce il valore di input corretto e del giusto tipo (str, int o float).
        """
        assert(info in ("name", "quantity", "selling_price", "purchase_price")),"Valore di input richiesto non ammesso."
        while True:
            try:
                value = ""
                while value == "":
                    value = input(msg).strip()
                if info == "name":
                    return value #str
                elif info == "quantity":
                    return Product.validate_quantity(value) #int
                else: #info in ("selling_price", "purchase_price")
                    return Product.validate_price(value) #float
            except Exception as e:
                print(e)

    def _get_available_products(self) -> List["Product"]:
        """
        Il metodo filtra la lista dei prodotti restituendo solo quelli in stato "available"
        """
        return list(filter(lambda x: x.status == "available", self.supplies))
    #endregion inherited methods


