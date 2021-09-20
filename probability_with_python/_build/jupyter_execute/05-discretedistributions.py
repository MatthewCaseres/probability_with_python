#!/usr/bin/env python
# coding: utf-8

# # Common Discrete Distributions
# 
# ## Bernoulli Distribution
# 
# The Bernoulli distribution is appropriate when there are two outcomes. Success happens with probability $p$ and failure happens with probability $1-p$.
# 
# $$
# p(x) =
#     \left\{
#         \begin{array}{cc}
#                 p & \mathrm{for\ } x=1 \\
#                 1-p & \mathrm{for\ } x=0 \\
#         \end{array} 
#     \right.
# $$
# 
# ***
# **exercise:** Let $X$ be a Bernoulli random variable. Show that $E(X)=p$ and that $V(X)=p \cdot (1-p)$. 
# ***
# 
# The number of heads from a single coin flip is an example of a Bernoulli random variable. The event that the coin lands on heads is success, tails is failure. If the coin is fair, $p$ = .5.

# ## Binomial Distribution
# 
# ### Statement
# 
# If we have $n$ Bernoulli trials each with a probability of success of $p$. The random variable representing the total number of successes has the **binomial distribution** with parameters $n$ and $p$.
# 
# ***
# Let $X$ have the binomial distribution with parameters $n$ and $p$. We have:
# 
# $$p(k) = P(X=k) = {n \choose k}p^k(1-p)^{n-k}$$
# 
# ***
# 
# #### Example
# 
# We have an unfair coin with probability of heads $.6$. To calculate the probability of getting $3$ heads after flipping the coin $5$ times is ${5 \choose 3} .6^3 .4^2$. This is because each sequence that has $3$ (like HTHTH) heads occurs with probability $.6^3 .4^2$. There are ${5 \choose 3}$ ways to select $3$ heads coins out of $5$ coins. We add up the probabilities to get ${5 \choose 3}.6^3 .4^2$.
# 
# ### Mean and Variance of the Binomial Distribution
# 
# It has been given as an exercise to prove that if $X$ is Bernoulli with parameter $p$ then $E(X) = p$ and $V(X) = p(1-p)$. Formulas for the binomial distribution are very similar.
# 
# ***
# Let $X$ have the binomial distribution with parameters $n$ and $p$. We have:
# 
# $$E(X) = np$$
# 
# $$V(X) = np(1-p)$$
# 
# ***
# 
# So if we flip a fair coin 10 times we expect to get $E(X) = np = 10 \cdot .5 = 5$ heads, which makes sense. There is a not-pretty proof of this but let's wait to prove this in a pretty way.

# ## Hypergeometric Distribution
# 
# ### Rocks in bags example
# 
# We have $15$ rocks in a bag. $7$ rocks are red and $8$ are black. We select $5$ rocks. What is the probability of selecting exactly $2$ red rocks and $3$ black rocks.
# 
# Any selection of rocks is equally likely. We can use our formula for the probability when all events are equally likely.
# 
# $$\frac{\text{Number of Selected Outcomes}}{\text{Total Possible Outcomes}}$$
#   
# For the denominator we need to find how many ways there are to draw $5$ rocks from a set of $15$. This is $15 \choose 5$.
# 
# For the numerator we need to select $2$ red rocks from a set of $7$. This can be done in $7 \choose 2$ ways. We can select $3$ blue rocks from $8$ in $8 \choose 3$ ways. There are then ${7 \choose 2}{8 \choose 3}$ ways to select the rocks.
# 
# The answer is then:
# 
# $$\large \frac{{7 \choose 2}{8 \choose 3}}{{15 \choose 5}}$$
# 
# ### Playing cards example
# 
# We have a deck of $40$ cards. $30$ cards are red and $10$ are black. We draw a hand of $5$ cards. Show that the probability of drawing $3$ black cards is:
# 
# $$\large{\frac{{30 \choose 2}{10 \choose 3}}{{40 \choose 5}}}$$
# 
# ### The formula
# 
# We randomly select $n$ items from a population of $N$ items. Let $r$ represent the number of items from the population classified as a success, and $k$ be the number of items in the selection classified as successes. Let $X$ be the random variable representing the number of items in our selection considered successes. 
# 
# $$P(X=k) = \large{\frac{{{N-r}\choose{n-k}}{{r}\choose{k}}}{{N \choose n}}}$$
# 
# For our previous examples we did not need this formula. It is worth understanding how this formula works, so that you can understand it instead of memorizing it.
# 
# ### Hypergeometric vs. Binomial
# 
# The hypergeometric distribution is closely related to the binomial distribution. We have a group of $600$ cowboys and $400$ astronauts. We select $4$ people randomly from the $1000$ to win a prize, what is probability that $3$ people are cowboys and $1$ is an astronaut?
# 
# $$\large \frac{{600 \choose 3}{400 \choose 1}}{{1000 \choose 4}} = 0.3459$$
# 
# The hypergeometric distribution is different than the binomial distribution because it samples **without replacement**. Let's change the problem and allow someone to win a prize multiple times. $4$ names are drawn from a hat. Each time a name is drawn a prize is given and the name is put back in the hat (this is sampling **with replacement**). Since $600$ of the $1000$ people are cowboys, any time we make a selection to win a prize there is a probability of $.6$ that the person is an cowboy. We select $4$ people, so the distribution of prizes given to cowboys is binomial with parameters $n = 4$, $p = .6$. The probability of $3$ cowboys winning prizes and $1$ astronaut winning a prize is:
# 
# $${4 \choose 3} \cdot .6^3 \cdot .4 = .3456$$
# 
# The hypergeometric distribution (without replacement) gives $.3459$ and the binomial distribution (with replacement) gives $.3456$. Consider that if we draw a single cowboy from the hat, the probability of the next draw being a cowboy is $.6$ if we sample with replacement and $\frac{599}{999} \approx.6$ without replacement. This is why our answers are similar. This approximation works best when the population is much larger than the total number of items drawn in the hypergeometric distribution, i.e. $N$ is large compared to $n$.
# 

# ## Poisson Distribution
# 
# ### Intuition
# 
# A Poisson distribution is appropriate when we are counting the number of times something happens in an hour or some unit of time. How many texts do I get in an hour? How often does a car accident happen on interstate 35? These are things that happen at some frequency.
# 
# If you see the phrase **"the average rate"** you should consider that the question might be related to the Poisson distribution.
# 
# Often they give you the rate per hour and you need to convert it to the rate per $2$ hours, or the daily rate, or the rate per minute.
# 
# ***
# The average rate of people spilling their coffee in the office is $2$ per hour. Generally this rate is called $\lambda$, so $\lambda = 2$. The rate of people spilling coffee per minute is $\frac{\lambda}{60} = \frac{1}{30}$. The rate of people spilling their coffee every day is $24 \lambda = 48$.
# ***
# 
# In the Poisson model it is assumed that the rate is constant throughout the day and that the events being counted are independent. So our coffee spilling example might not be a Poisson process if the rate of coffee spills are much higher in the morning. Also, if someone spilling their coffee makes other people more likely to spill coffee, the spills are not independent.
# 
# ### Formula
# 
# Let $X$ have a Poisson distribution with parameter $\lambda$. The probability of $k$ occurences of something happening is:
# 
# $$P(X=k) = \frac{e^{-\lambda}\lambda^k}{k!}$$
# 
# Let's verify that the sum of all probabilities is 1.
# 
# $$
# \begin{align*}
# \sum_{n=0}^{\infty} P(X=k) &= \displaystyle\sum_{k=0}^{\infty}\frac{e^{-\lambda}\lambda^k}{k!} \\
# &=  e^{-\lambda} \displaystyle\sum_{k=0}^{\infty} \frac{\lambda^k}{k!} \\
# &= e^{-\lambda}e^\lambda=1
# \end{align*}
# $$
# 
# We use a fact from Calculus 2 that $e^\lambda = \sum_{k=0}^{\infty} \frac{\lambda^k}{k!}$
# 
# 
# 
# ### Example
# 
# Assume a Poisson model. The average rate of people spilling their coffee in the office throughout the work day is $2.5$ spills per hour. What is the probability that $2$ people spill their coffee between $8$ A.M. and $9$ A.M., and $6$ people spill their coffee between $11$ A.M. and $1$ P.M.?
#   
# Because the number of spills across time intervals is independent:
# 
# $$P(\text{2 spills from 8-9 A.M. and 6 spills from 11 A.M.-1 P.M.}) = \\
# P(\text{2 spills from 8-9 A.M.}) \cdot P(\text{6 spills from 11 A.M.-1 P.M.})$$
#   
# For the calculation from $\text{8-9 A.M.}$ we use $\lambda = 2.5$ since the time interval is $1$ hour. 
# 
# $$ P(\text{2 spills from 8-9}) =\frac{e^{-2.5}2.5^2}{2!}$$
#   
# For the calculation from $\text{11 A.M.- 1 P.M.}$ we use $\lambda = \lambda_\text{1 hour} \cdot t = 2.5 \cdot 2 =  5$ since the time interval is $2$ hours. 
# 
# $$P(\text{6 spills from 11 A.M.-1 P.M.}) =\frac{e^{-5}5^6}{6!}$$
#   
# We multiply these quantities to get the answer:
# 
# $$\frac{e^{-2.5}2.5^2}{2!} \cdot \frac{e^{-5}5^6}{6!} = .03751$$
# 
# 

# ## Geometric Distribution
# 
# Let $X$ be the number of tries it takes to land heads when flipping an unfair coin if the probability of heads is $p=.6$. The geometric distribution is when you take independent bernoulli trials until the first success. Each coin flip is an independent bernoulli trial with the same probability of success.
# 
# The probability of success on the first attempt is $.6$. The probability of success on the second attempt is $.4 \cdot .6$, the sequence $TH$. Success on the third attempt happens with the sequence $TTH$ with probability $.4 \cdot .4 \cdot .6$.
# 
# ### PDF
# 
# We perform independent Bernoulli trials, each having a probability of success $p$ and probability of failure $q$. Let $X$ represent the trial on which the first success occurs. 
# 
# $$P(X=k) = q^{k-1}p$$
# 
# ### E[X] and Var[X]
# 
# Let $X$ be a geometric random variable with parameter p.
# 
# $$E(X) = \frac{1}{p}$$
# $$V(X) = \frac{1-p}{p^2}$$
# 
# ### Forms of the geometric distribution
# 
# So far we have been counting the number of trials until success. Another way to do this is to count the number of failures before success. I like first way, because $E(X) = \frac{1}{p}$ which I think is pretty. 

# ## Negative Binomial Distribution
# 
# The geometric distribution has a parameter $p$ and the value of the random variable is the first successful attempt. The negative binomial distribution has two parameters, $p$ and $r$. The negative binomial distribution counts the attempt on which the $r^{th}$ success occurs.
# 
# We flip an unfair coin with a probability of $.6$ for heads and $.4$ for tails. Let $X$ be the trial on which we get the $3rd$ head. We wish to know $P(X=5)$. Let's first consider that the $5th$ flip must be a head. Of the first $4$ flips, $2$ of them are heads. We get $2$ heads in the first four flips with probability:
# 
# $${4 \choose 2}.6^2.4^2$$
# 
# We need the fifth flip to be heads so we multiply this probability by $.6$ to get our answer of:
# 
# $${4 \choose 2}.6^3.4^2$$
# 
# Our formula is then $P(X=x) = {{x-1} \choose {r-1}}p^r(1-p)^{x-r}$.
# 
# ### More common formulation
# 
# A more common way of representing this is to count the number of failures until the $r^{th}$ success. 
# 
# ***
# Let $Y$ be the number of failures until the $rth$ success. We calculate the p.d.f. of $Y$.
# 
# $$P(Y=y)={{r+y-1} \choose y}p^r(1-p)^y$$
# 
# ***
# 
# If $X$ is the R.V. representing the attempt on which the $rth$ success occurs and $Y$ is the R.V. representing the number of failures before the $rth$ success, then $Y = X - r$ because $\text{failures = attempts - successes}$. Regardless of if the question asks you to count failures or attempts, the prepared student should be able to deduce the probability using first principles.
# 
# We give formulas for the expectation and variance for this formulation of the negative binomial distribution.
# 
# 
# ***
# 
# Let $Y$ be the number of failures until the $rth$ success.
# 
# $$E(Y) = \frac{r(1-p)}{p}$$
# 
# $$V(Y) = \frac{r(1-p)}{p^2}$$
# 
# ***
