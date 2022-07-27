numbers = [1,2,3,4,5,6]
# wynik = [(1,2)...]

def windows(n,numbers = numbers):  # argument domyślny, czyli taki podstawowy który zawsze
    output_list = []
    window_size = n - 1
    for index,x in enumerate(numbers):  # funkcja enumarate, zwracajaca krotke  -> (indeks,element)
        if index < (len(numbers)-window_size):
            output_list.append((x,numbers[index:n]))  # do kazdego elelemntu od 0 do 5, dopisz elementy 1,6
    return output_list

def window(sequence, n):
    """Return list of tuples of items in given list and next n-1 items."""
    items = []
    for i in range(len(sequence)): # dla cyfr w przedziale o długości listy (6)
        if i+n <= len(sequence): # jesli  cyfra + n  <= dlugosc sekwencji
            items.append(tuple(sequence[i:i+n]))  # dodaj do listy wyjsciowej, cyfry od i do i+n ZRZUTOWANE (casting) DO TUPLE (krotka)
    return items
print(window(numbers,2))

# Rzutowanie typów, casting.
cyfra = 1.5
print(type(cyfra),cyfra)
cyfra = int(cyfra)
print(type(cyfra),cyfra)