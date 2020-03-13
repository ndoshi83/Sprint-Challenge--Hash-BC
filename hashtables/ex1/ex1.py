#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    if length < 2:
        Answer = None
        return Answer

    elif length == 2:
        Answer = (1, 0)
        return Answer

    else:
        # Insert weights and list index values into hash table
        for i in range(length - 1):
            hash_table_insert(ht, weights[i], i)

        # Search hash table for pair matching limit weight
        for i in range(length - 1):
            check = limit - weights[i]
            value = hash_table_retrieve(ht, check)
            if value != None:
                Answer = (i, value)
                Answer = (max(Answer), min(Answer))
                return Answer



def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
