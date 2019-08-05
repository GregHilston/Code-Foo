class LRU
{
    constructor(capacity)
    {
        this.capacity = capacity;
        this.contents = {};
        this.cacheSize = 0;
        this.accessCounter = 0;
    }

    updateAccess(key)
    {
        if (this.contents.hasOwnProperty(key)) {
            this.accessCounter++;
            this.contents[key].lastAccess = this.accessCounter;
        }
    }

    makeRoom()
    {
        if (this.cacheSize >= this.capacity) {

            delete this.contents[oldestKey];
            this.cacheSize--;
        }
    }

    get(key)
    {
        if (this.contents.hasOwnProperty(key)) {
            this.updateAccess(key);
            return this.contents[key].value;
        } else {
            return null;
        }
    }

    put(key, value)
    {
        this.makeRoom();
        this.contents[key] = {value: value};
        this.cacheSize++;
        this.updateAccess(key);
    }
}