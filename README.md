THE IDEA

In this simple model, we have 3 different substrates [a,b,c] in a certain solution. 
Each of these substrates can combine with another with a certain probability [pab,pac,pbc], creating a compound. 
The "ac" compound is toxic (you can pick another).
The entire solution will become toxic if the content of compound “ac” exceeds 10% of the total solution (“toxicity limit” can be modeled).

ASSUMPTIONS

The probability of forming compounds made of more (or less) than 2 substrates equals 0. 
The probability of forming compounds made of the same substrates also equals 0.
Only one compound can be made in one unit of time (iteration).
There is a t_max, after which no more reaction will take place in the solution and no new compounds will be formed, no matter how many substrates remain. ("t_max" can be modeled).

HOW IT WORKS

In each iteration the model draws a natural number from the interval <1,3> twice, where each number stands for a substrate. 
The model then adds up the drawn numbers. An action is assigned to each result.

The formation of each compound is subject to some probability. 
Therefore, the model needs a condition for the formation of this compound. The condition is simple. 
The model draws a real number from the interval <0,1>. 
If the drawn number is less than or equal to the probability of forming the compound, the compound will be formed. Otherwise, nothing will happen.

There can be 3 results:
  1. The toxicity limit has been reached (the solution is toxic now, so it's useless for us);
  2. The substrate has been exhausted (we know, that with this amount of substrates the solution did not become toxic);
  3. The time in which the reaction can take place is over (we know, that with this amount of substrates the solution will not become toxic, because the max time for the reactions is constant);

Depending on what you want to know, you can change the values of the input parameters, such as the amount of substrates, the time at which reactions can take place in this solution, or the probabilities with which each compound is formed.

At the end of the code, the simulation is run multiple times to see some statistics (how many times with the selected input parameters the solution became toxic, and how many times was the t_max reached before the solution became toxic. Shown in % of simulations. There are 1000 simulations by default.).

WHEN CHOOSING INPUT PARAMETERS, PLEASE REMEMBER THAT THE SUM OF THE PROBABILITIES OF ALL INCIDENTS SHOULD BE EQUAL TO 1 !
