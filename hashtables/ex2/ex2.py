#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * (length - 1)

    """
    YOUR CODE HERE
    """
    # Insert tickets into hashtable
    for t in tickets:
        hash_table_insert(hashtable, t.source, t.destination)

    # Create ordered route
    for i in range(length):
        if i == 0:
            value = hash_table_retrieve(hashtable, "NONE")
            route[i] = value
        else:
            value = hash_table_retrieve(hashtable, route[i-1])
            if value == "NONE":
                return route
            else:
                route[i] = value

