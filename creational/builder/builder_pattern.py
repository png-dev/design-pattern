from abc import ABC, abstractmethod


class Card(ABC):

    @abstractmethod
    def add_chip(self):
        pass

    @abstractmethod
    def get_card(self):
        pass


class PaymentCard(Card):

    def add_chip(self):
        return 'Payment Card Add Chip'

    def get_card(self):
        return self
