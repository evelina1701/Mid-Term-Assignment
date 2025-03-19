# Geikina Evelīna PD1

import numpy as np

# Algoritma avots: https://www.geeksforgeeks.org/maximum-difference-between-two-elements/

# Algoritms nosaka maksimālo starpību starp diviem masīva elementiem,
# kur mazākais elements tiek atrasts iterācijas laikā.
# Tiek saglabāta lielākā starpība (max_diff) un mazākais atrastais skaitlis (min_elem).
# Funkcija pieņem masīvu ar vismaz diviem elementiem.
# Ja masīvs ir sakārtots dilstoši, rezultāts būs negatīvs.
# Ja visi elementi ir vienādi, funkcija atgriež 0.


# Paskaidrojums par Algorithm Complexity:
# Algorithm Complexity = O(n)
# Sākotnējo mainīgo iestatīšana aizņem O(1) laiku
# Kad cikls iet cauri masīvam, tas izpildās n-1 reizes, jo skaitīšana sākas ar 1 un beidzas ar array_size-1
# Katrā iterācijā notiek tikai divas salīdzināšanas operācijas un iespējama vērtību piešķiršana, kas aizņem O(1) laiku
# Tā kā šīs operācijas tiek veiktas visām n masīva vērtībām, izņemot pirmo, kopējā sarežģītība ir O(n)

# Algoritmam nav cita Algorithm Complexity, jo nav iekšējā cikla (tāpēc arī nav O(n^2))
# Tāpat kodā nav arī šķirošanas vai meklēšanas algoritma, kas palielinātu Algorithm Complexity līdz O(log n) vai O(n log n)

def MaxDifference(array, array_size):
    # Funkcija sākotnēji pieņem, ka maksimālā starpība ir pirmo divu elementu starpība.
    max_diff = array[1] - array[0]

    # min_elem saglabā mazāko līdz šim atrasto skaitli,
    # sākotnēji iestatītu kā pirmo elementu.
    min_elem = array[0]

    # Algoritms pārbauda katra elementa starpību ar līdz šim mazāko atrasto skaitli
    # un saglabā lielāko atrasto starpību.
    for i in range(1, array_size):
        if (array[i] - min_elem > max_diff):
            max_diff = array[i] - min_elem

        # Ja pašreizējais elements ir mazāks nekā iepriekš atrastais min_elem, to atjaunina.
        if (array[i] < min_elem):
            min_elem = array[i]

    # Funkcija atgriež aprēķināto maksimālo starpību.
    return max_diff


arr = []

# Avots faila lasīšanai: https://www.geeksforgeeks.org/python-read-text-file-into-list-or-array/
# Dati tiek nolasīti no faila kā teksta virknes un saglabāti NumPy masīvā.
arr = np.loadtxt('ints_10M.txt', dtype=str)

# Avots virkņu konvertēšanai par veseliem skaitļiem: https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/
# Pārveidot masīva elementus no teksta uz veseliem skaitļiem, izmantojot map() funkciju.
arr_int = list(map(int, arr))

# Masīva lielums tiek noteikts, lai izmantotu funkcijā.
size = len(arr_int)

# Funkcija izsauc MaxDifference(), aprēķina maksimālo starpību un izdrukā rezultātu.
print("Maksimālā starpība ir", MaxDifference(arr_int, size))
