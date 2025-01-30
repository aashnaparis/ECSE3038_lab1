total_resistance = 0
resistors = ([330, 1000, 2200]) 

def parallel(resistance): 
    total_resistance = 0
    for x in resistance:
        total_resistance += 1/x
        x += 1
    return total_resistance

temp = parallel(resistors)
actual_tot = temp ** -1

print(f"{actual_tot:.3f} ohms")