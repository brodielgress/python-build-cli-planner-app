from abc import ABCMeta, abstractmethod
from collections.abc import Iterable

@abstractmethod
class DeadlinedMetaReminder(Iterable, ABCMeta):
    def __init__(self):
        pass