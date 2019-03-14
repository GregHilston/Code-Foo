class HashTable():
    """A horribly simple HashTable implementation.

    """
    def get(self, key): 
        """Fetches the value of the given previous set key.
        
        Args:
            key (int or str or float): The key of the value of interest.

        Returns:
            any or None: The value that belongs to this key or None if not found.

        """
        raise NotImplementedError
    
    def put(self, key, value):
        """Stores the given value, relating it to the given key.
        
        Args:
            key (int or str or float): The key of the value of interest.
            value (any): The value to store for this key.

        """
        raise NotImplementedError