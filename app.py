total_resistance = 0
resistors = ([330, 1000, 2200]) 

def parallel(resistance): 
    total_resistance = 0
    for x in resistance:
        total_resistance += 1/x
        x += 1
    actual_tot = total_resistance ** -1
    return actual_tot

temp = parallel(resistors)

print(f"{temp:.3f} ohms")

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

def temperature_check(temperature, cel_fah):
    if cel_fah == "F":
        temperature = (temperature - 32) * 5/9

    if 36.1 <= temperature <= 37.2:
        print(f"The patient's temp is {temperature:.2f}°C, The patient's temp is normal")
    elif temperature < 36.1:
        print(f"The patient's temp is {temperature:.2f}°C, The patient is hypothermic")
    else:
        print(f"The patient's temp is {temperature:.2f}°C, The patient is hyperthemic")

temperature_check(14, "C")

temperature_check(37, "C")

temperature_check(37, "F")


