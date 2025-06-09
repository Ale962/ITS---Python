# Exercise 6

'''
Unione di Intervalli Sovrapposti
Data una lista di intervalli chiusi rappresentati come liste di due elementi [start, end],
scrivi una funzione merge_intervals(intervals) che restituisce una nuova lista di
intervalli in cui tutti quelli sovrapposti sono stati fusi. Ogni intervallo soddisfa start <=
end. La lista risultante deve essere ordinata per inizio intervallo e non devono esserci
sovrapposizioni.
Requisiti:
● Input: una lista di liste, ad esempio [[1, 4], [2, 6], [8, 10], [15, 18]].
● Se due intervalli si sovrappongono o si toccano (es. [1,4] e [4,5]), unirli in
[1,5].
● Restituisci una lista di intervalli fusi, ordinata per il valore di inizio.
● Casi limite:
○ Se l’input è vuoto, restituisci una lista vuota.
○ Se è presente un solo intervallo, restituiscilo così com’è.
Esempi:
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
merge_intervals(intervals) # restituisce [[1, 6], [8, 10], [15,
18]]
intervals = [[1, 4], [4, 5]]
merge_intervals(intervals) # restituisce [[1, 5]]

'''

def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    list_merged_intervals: list[list[int]] = []
    for interval in intervals:
        if not list_merged_intervals:
            list_merged_intervals.append(interval)
        if list_merged_intervals:
            x, y = interval
            merged = False
            for i in list_merged_intervals:
                z, w = i
                if x <= w and y >= z:
                    new_interval = [min(x, z), max(y, w)]
                    list_merged_intervals.remove(i)
                    list_merged_intervals.append(new_interval)
                    merged = True
                    break
            if not merged:
                list_merged_intervals.append(interval)

    list_merged_intervals_sorted = sorted(list_merged_intervals)
    return list_merged_intervals_sorted

if __name__ == '__main__':
    Intervals = [
        [[1, 3], [2, 6], [8, 10], [15, 18]],
        [[1, 4], [4, 5]],
        [[1, 2], [3, 4], [5, 6]],           
        [[1, 10], [2, 3], [4, 5]],           
        [[5, 6], [1, 2], [2, 4]],            
        [],                                  
        [[1, 5]],                            
        [[1, 4], [0, 2]],                    
        [[1, 4], [2, 3], [6, 8], [7, 10]], 
    ]
    for i in Intervals:
        print(merge_intervals(i))