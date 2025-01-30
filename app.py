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

def potential_divider(v_supply, resistors):
    r_tot = 0
    for r in resistors:
        r_tot += r
        r += 1

    tot_current = v_supply / r_tot

    for x in resistors:
        v_drop = tot_current * x
        print(f"{v_drop:.2f}v")
        

potential_divider(9, [3000, 1000])


