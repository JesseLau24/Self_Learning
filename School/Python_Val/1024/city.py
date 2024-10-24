
'''
1. City


The city has a known population p0


A certain percentage of people join each year


Every year a certain number of delta also arrive (or leave)


We need to know when (if at all) the city will reach a population of p


Write a function get_city_year (p0, perc, delta, p) that returns the years (full) when p is reached.


If p cannot be reached, then we return -1


Example:


get_city_year (1000,2,50,1200) -> 3


1000 + 1000 * 0.02 + 50 => 1070 after the 1st year


1070 + 1070 * 0.02 + 50 => 1141 after the 2nd year


1141 + 1141 * 0.02 + 50 => 1213 after the 3rd year


PS. Note that we give perc as a percentage to be converted to a decimal number.


We check if it works with the following parameters:


get_city_year (1000, 2, -50, 5000) -> -1 # relatively current problem


get_city_year (1500, 5, 100, 5000) -> 15


get_city_year (1500000, 2.5, 10000, 2,000,000) -> 10

'''

def get_city_year(p0, perc, delta, p):
    years = 0
    while p0 < p:
        p0 += p0 * (perc / 100) + delta
        years += 1
        if p0 < 0:
            break
    if p0 >= p:
        return years
    else:
        return -1


print(get_city_year (1000, 2, -50, 5000))
print(get_city_year (1500, 5, 100, 5000))
print(get_city_year (1500000, 2.5, 10000, 2000000))