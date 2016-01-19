__author__ = 'KoicsD'


class Order:
    @classmethod
    def parse(cls, csv_row: str):
        pass

    def persist(self, cursor_obj):
        pass

    def to_csv(self):
        pass

    @classmethod
    def select(cls):
        pass
