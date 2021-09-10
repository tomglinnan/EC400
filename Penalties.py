#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

PENALTY SHOOTOUT EXTENSION

"""

"""

In the in-person class, we talked about an extension to the penalty shootout question

How penalties work: each team takes 5. If one team has scored strictly more than the other, that team wins.
If it's a draw, then we have sudden death - teams take one penalty each. If both score or both miss, they go on.
Otherwise the team that scores wins and the other loses. The original question was about sudden death only
but what about the whole match?

If team 1 has probability of scoring p and team 2 has probability q, what's the probability team 1 win?
We didn't do it fully because the addition required is annoying, but fortunately we can get Python to count for us

In the case considered in class,
[Brazil] p = 0.8
[Italy] q = 0.75
[Standard Fooball / Soccer Rules] n = 5

To try out, write prob(p,q,n) in the console with the assosciated p,q,n you're interested in
You need scipy installed on your computer (eg if you have anaconda you'll be fine)

* Result afer 5 rounds: *
Probability Brazil win without sudden death is 42.2%
Probability Italy win without sudden death is 27.9%
Probability of going to sudden death is 29.8%

Note that the probability of Brazil winning conditional on going to sudden death was 4/7 = 57.1%
Intuitively: in sudden death there's no prospect of a draw. But it's actually relatively easier for the 
weaker team to win in sudden death than in the 5 shootouts at the start.

Total probability of Brazil winning = 0.422 + (0.298*0.571) = 59.2%, so Italy probability 40.8%

Does the conclusions work for general p,q,n? Try yourself if you're interested!

"""

from scipy.special import comb

def prob_draw(p,q,n):
    Team_1_pdf =  [comb(n,x)*(p**x)*((1-p)**(n-x)) for x in range(n+1)]
    Team_2_pdf =  [comb(n,x)*(q**x)*((1-q)**(n-x)) for x in range(n+1)]
    
    prob = 0
    
    for i in range(n+1):
        prob = prob + Team_1_pdf[i]*Team_2_pdf[i]
    
    print('Probability of a draw after', n, 'rounds is', round(prob,4)*100, '%')
    
def prob_win(p,q,n):
    Team_1_pdf =  [comb(n,x)*(p**x)*((1-p)**(n-x)) for x in range(n+1)]
    Team_2_pdf =  [comb(n,x)*(q**x)*((1-q)**(n-x)) for x in range(n+1)]
    
    prob = 0

    for i in range(n+1):
        for j in range(i):
            prob = prob + Team_1_pdf[i]*Team_2_pdf[j]
            
    print('Probability of a team 1 winning after', n, 'rounds is', round(prob,4)*100, '%')
    
def prob(p,q,n=5):
    prob_win(p,q,n)
    prob_draw(p,q,n)
    
    Team_1_pdf =  [comb(n,x)*(p**x)*((1-p)**(n-x)) for x in range(n+1)]
    Team_2_pdf =  [comb(n,x)*(q**x)*((1-q)**(n-x)) for x in range(n+1)]
    
    prob = 0

    for i in range(n+1):
        for j in range(i):
            prob = prob + Team_1_pdf[j]*Team_2_pdf[i]
    
    print('Probability of a team 2 winning after', n, 'rounds is', round(prob,4)*100, '%')