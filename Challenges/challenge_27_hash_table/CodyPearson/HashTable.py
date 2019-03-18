class HashTable:
    hashes = []
    values = []

    def calculate_hash(self, key):
        # A stupid hash algorithm using the sum of the byte values
        # Makes no real attempt to avoid collisions
        keyBytes = bytes(key, "utf8")
        return sum(keyBytes)

    def get(self, key):
        theHash = self.calculate_hash(key)
        try:
            index = self.hashes.index(theHash)
            return self.values[index]
        except ValueError:
            return False


    def set(self, key, value):
        theHash = self.calculate_hash(key)
        try:
            index = self.hashes.index(theHash)
            self.values[index] = value
        except ValueError:
            self.hashes.append(theHash)
            self.values.append(value)


myTable = HashTable()

# Basic usage
# Expected output: Hi!
myTable.set('ab', 'Hi!');
print(myTable.get('ab'))

# Retrieving non-existent value
# Expected output: False
print(myTable.get('not'))

# Intentional hash collision with ab
# Expected output: "Bye!"
myTable.set('xK', 'Bye!')
print(myTable.get('ab'))