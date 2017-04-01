from montecarlo import montecarlo
from random import randint


#This is the function to calculate the final points
#Generally 37 points is the survival minimum

def final_points(g):
    '''
    Pass a dictionary with the values needed for the simulation
    '''
    points=g['points']
    for n in range(0,g['games']):
        result=randint(1, 10)
        if result >= g['winpct']:
            points += 3
        elif result >= g['drawpct']:
            points += 1
    if points > 37:
        return True
    else:
        return False

#Setup the array for Middlebrough
def setup_vals_boro():
    return {'team':'Middlesbrough','points':25,'games':10,'winpct':9,'drawpct':4}

#Setup the array for Sunderland
def setup_vals_sund():
    return {'team':'Sunderland','points':23,'games':10,'winpct':8,'drawpct':2}


def output_result(success, iterations, final=False):
    if final:
        print("After {} Iterations chance of reaching 37 points {:3.2F}% ".format(iterations,montecarlo.probability(success, iterations)*100.0))
        
mc = montecarlo(final_points,setup=setup_vals_boro,output=output_result)
print("Calculating chances for Middlesbrough")
mc.run(iterations=50000,output_every=50000)

mc = montecarlo(final_points,setup=setup_vals_sund,output=output_result)
print("Calculating chances for Sunderland")
mc.run(iterations=50000,output_every=50000)



