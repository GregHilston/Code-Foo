from typing import Hashable, Any

class HashTable:
    """A horribly simple HashTable implementation.
    
    """
     # Where we store our HashTable's keys -> value mapping
    storage = [] # type: [int, List[(Hashable, Any)]]

    def __init__(self, starting_storage_size = 10):
        self.storage = [None] * starting_storage_size # ensuring our storage is of the correct size

    def hash(self):
        return self.__attrs % 42

    def __getitem__(self, key_to_look_up: Hashable) -> Any:
        """Some text about the function

        """
        if key_to_look_up.__hash__() in self.storage:
            for key, value in self.storage[key_to_look_up.__hash__()].items():
                if key == key_to_look_up:
                    return value

    def __setitem__(self, key_to_store: Hashable, value: Any):
        """Some text about the function

        """
        key_to_store.
    
        if key_to_store.__hash__() not in self.storage:
            self.storage[key_to_store.__hash__()] = dict()
            self.storage[key_to_store.__hash__()][key_to_store] = [value]
        else:
            self.storage[key_to_store.__hash__()][key_to_store].append(value)