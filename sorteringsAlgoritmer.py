import random, copy

def bogoSort(items):
    # Kopier den liste, vi har modtaget som parameter, så vi ikke ændrer den originale!!
    items = items.copy()
    isSorted = None # Boolean til markering af, om listen er sorteret
    attempts = 0 # Tællevariabel til at holde styr på antal af forsøg
    while not isSorted:
        attempts += 1
        if attempts > len(items) * 5000: # Check for at stoppe tendensen mod uendeligt
            print('Giver op på grund af for mange forsøg ({}) og bruger TimSort'.format(attempts))
            items.sort()
            return items
        random.shuffle(items) # Bland alle elementer helt tilfældigt
        isSorted = True # Vi går ud fra at listen tilfældigvis er sorteret,
        # ...og prøver i denne løkke at bevise det modsatte
        for index in range(len(items)-1):
            if items[index] > items[index+1]:
                isSorted = False
                break # Bryd løkken hvis et eneste element er forkert sorteret
    print('Sorteret efter {} forsøg'.format(attempts))
    return items


# Optimized Bubble sort in Python
""""""
def bubbleSort(array):
    # loop through each element of array
    for i in range(len(array)):

        # keep track of swapping
        swapped = False

        # loop to compare array elements
        for j in range(0, len(array) - i - 1):

            # compare two adjacent elements
            # change > to < to sort in descending order
            if array[j] > array[j + 1]:
                # swapping occurs if elements
                # are not in the intended order
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

                swapped = True

        # no swapping means the array is already sorted
        # so no need for further comparison
        if not swapped:
            break



#Insertion sort

def insertionSort(items):
    for i in range(1,len(items)-1):
        J = i
        while J>0 and items [J] < items [J-1]:
            items[J],items[J+1] = items[J+1], items[J]
            J-=1
    return items


if __name__ == '__main__':
    l = list(range(0, 500))
    lb = l.copy()
    for i in range(1):
        random.shuffle(lb)
        ## Kald den funktion, du vil teste
        ls = insertionSort(l)
        ## Kald den funktion, du vil teste
        if ls != l:
            print('Fejl! Algoritmen kan ikke sortere.')
            break
    print('Succes! Algoritmen sorterer korrekt.')
    print('blandet: ', lb)
    print('sorteret:', ls)



