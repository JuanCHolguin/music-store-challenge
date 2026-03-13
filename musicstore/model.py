from datetime import datetime
from sys import set_int_max_str_digits

class Transaction:
    SELL: int = 1
    SUPPLY: int = 2
    def __init__(self, type: int, copies: int):
        self.type: int = type
        self.copies: int = copies
        self.date: datetime = datetime.now()

class Disc:
    def __init__(self, sid: str, title: str, artist: str, sale_price: float, purchase_price: float, quantity: int):
        self.sid: str = sid
        self.title: str = title
        self.artist: str = artist
        self.sale_price: float = sale_price
        self.purchase_price: float = purchase_price
        self.quantity: int = quantity
        self.transactions: list[Transaction] = []
        self.song_list: list[str] = []

    def add_song(self, song: str):
        self.song_list.append(song)

    def sell (self, copies: int) -> bool:

        if copies > self.quantity:
            return False
        else:
            self.quantity -= copies
            transaction = Transaction(Transaction.SELL, copies)
            self.transactions.append(Transaction(Transaction.SELL, copies))
        return True

    def supply(self, copies: int):

        self.quantity += copies
        self.transactions.append(Transaction(Transaction.SUPPLY, copies))

    def copies_sold (self) -> int:
        copias_vendidas = 0
        copias_vendidas = sum([x.copies for x in self.transactions if x.type == Transaction.SELL])
        return copias_vendidas

        '''for transaction in self.transactions:
              if transaction.type == Transaction.SELL:
                    copies_sum += transaction.copies_sold()'''

    def __str__(self)-> str:

        canciones = ", ".join(self.song_list)
        return f"SID: {self.sid}\nTitle: {self.title}\nArtist: {self.artist}\nSong List: {canciones}"

class MusicStore:
    def __init__(self) -> None:
        self.discs: dict[str, Disc] = {}

    def add_disc (self, sid: str, title: str, artist: str, sale_price: float, purchase_price: float, quantity: int):

        if sid not in self.discs:
            disc = Disc(sid, title, artist, sale_price, purchase_price, quantity)
            self.discs[sid] = disc

    def search_by_sid (self, sid: str) -> Disc | None:

        if sid not in self.discs:
            return None
        else:
            return self.discs[sid]
    def search_by_artist (self, artist: str) -> list[Disc]:
        ''''''

        resultado = [x for x in self.discs.values() if x.artist == artist]
        return resultado

    def sell_disc(self, sid: str, copies: int) -> bool:
        disc = self.search_by_sid(sid)
        if disc is None:
            return False

        return disc.sell(copies)

    def supply_disc(self, sid: str, copies: int) -> bool:
        disc = self.search_by_sid(sid)
        if disc is None:
            return False

        disc.supply(copies)
        return True

    def worst_selling_disc(self) -> Disc | None:

        if not self.discs:
            return None

        peor = None

        for disc in self.discs.values():

            if peor is None:
                peor = disc

            elif disc.copies_sold() < peor.copies_sold():
                peor = disc

        return peor
    '''  copies_sold_by_disc = {}
         for disc in self.discs.values():
            for t in self.transactions:
                if t.type == Transaction.SELL:
                    copies_sold_by_disc[disc] += t.copies
         
         return min(copies_sold_by_disc, key=copies_sold_by_disc.get) '''







