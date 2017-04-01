#Monte Carlo Simulation

I was looking to try and predict the chance of two football teams in the UK Premier league reaching **37 points** which is the normal level that teams need to reach to avoid being relegated. 

#Why Monte Carlo ?

Well, with 10 games to go - it is possible that a team will win all 10 games, but not likely.

What I want to do is run the statistical model, and decide if it was a success of a failure. Then repeat this a number of times (i.e. 1 Million) - now taking the average, I should have a better approximation as to the real chance of the result.


#Scenario

There are 10 games left, and 2 teams have 25 and 23 points respectfully. 

Each team performs (rather badly I am afraid to say) with different success.

Team 1, on average wins 15% of their games, and draws 40%.
Team 2, on average wins 40% of their games, and draws 20%.

##Scoring

In Football (US readers, convert that to soccer), the game is scored as 

  - win, 3 points
  - draw, 1 point
  - loose, 0 points

#How will they fare ?

What are the chances of each team reaching 37 points ?

In order to calculate this, I need to develop a function which will run through the remaining 10 matches, use the percentages, and return a True/False answer as to have we reached 37 points.


##Simulator function

The simulator function requires a dictionary - I create this using a specific method.

```python
#Setup the array for Middlebrough
def setup_vals_boro():
    return {'team':'Middlesbrough','points':25,'games':10,'winpct':0.3,'drawpct':0.6}
```

This dictionary is passed into the final_points (see below) method.


```python
def final_points(g):
    '''
    Pass a dictionary with the values needed for the simulation
    '''
    points=g['points']
    for n in range(0,g['games']):
        result=random()
        if result <= g['winpct']:
            points += 3
        elif result <= g['drawpct']+g['winpct']:
            points += 1
    if points > 37:
        return True
    else:
        return False
```


The rest of the code is general plumbing.


#Code listing

```python
from montecarlo import montecarlo
from random import random


#This is the function to calculate the final points
#Generally 37 points is the survival minimum

def final_points(g):
    '''
    Pass a dictionary with the values needed for the simulation
    '''
    points=g['points']
    for n in range(0,g['games']):
        result=random()
        if result <= g['winpct']:
            points += 3
        elif result <= g['drawpct']+g['winpct']:
            points += 1
    if points > 37:
        return True
    else:
        return False

#Setup the array for Middlebrough

def setup_vals_boro():
    return {'team':'Middlesbrough','points':25,'games':10,'winpct':0.15,'drawpct':0.4}

#Setup the array for Sunderland
def setup_vals_sund():
    return {'team':'Sunderland','points':23,'games':10,'winpct':0.4,'drawpct':0.2}

def output_result(success, iterations, final=False):
    if final:
        print("After {} Iterations chance of reaching 37 points {:3.2F}% ".format(iterations,montecarlo.probability(success, iterations)*100.0))
        
mc = montecarlo(final_points,setup=setup_vals_boro,output=output_result)
print("Calculating chances for Middlesbrough")
mc.run(iterations=50000,output_every=50000)

mc = montecarlo(final_points,setup=setup_vals_sund,output=output_result)
print("Calculating chances for Sunderland")
mc.run(iterations=50000,output_every=50000)

```

The output should be close to this....

```text
Calculating chances for Middlesbrough
After 50000 Iterations chance of reaching 37 points 76.94% 
Calculating chances for Sunderland
After 50000 Iterations chance of reaching 37 points 76.22% 

```

#Summary

Monte Carlo simulation is an interesting way to test simulation theories, and I hope this will give you the confidence to have a go yourself.

The main simulator function is obviously too simplistic - but getting that to be more accurate will require much more data, and more complexity.  
