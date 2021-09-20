#!/usr/bin/env python
# coding: utf-8

# # An Introduction to Set Theory
# 
# ## Sets and elements
# 
# Sets are collections of objects. In math we wrap the set in curly braces and separate elements with commas, here is a set with three numbers $\{1,2,4\}$. We often name sets with a capital letter like $A=\{1,2,4\}$. 
# 
# Things in the set are called **elements** of the set. The symbol $\in$ means "is an element of the set". So $1 \in \{1,2,4\}$. We put a slash through the symbol if it isn't an element of the set, so $3 \not\in \{1,2,4\}$. Let's see how this works in Python.

# In[1]:


# Make a set A = {1,2}
A = {1,2}
# The strings are formatted using "f-strings"
print(f"Our set is {A}")
print(f"1 is in A? {1 in A}")
print(f"3 is in A? {3 in A}")
# We can also construct sets from other "iterables" like lists using the set() function
print(set([1,2]))


# ### Set-builder notation
# 
# Sometimes we want to specify an infinite set like the even numbers. We might write this as $\{2,4,6,8,...\}$ and most people will understand. **Set-builder notation** writes it as $\{x | x \text{ is   an   even number}\}$. This is pronounced "the set of x where x is an even number".
# 
# We could say $\{x|x \text{ is a solution to } x^3 - 5x^2 - 2x + 10 = 0\}$ if we are having trouble finding the solutions of $x^3 - 5x^2 - 2x + 10 = 0$. The solutions are $\{-\sqrt{2},\sqrt{2},5\}$, so 
# 
# $$\{-\sqrt{2},\sqrt{2},5\} =\{x|x \text{ is a solution to } x^3 - 5x^2 - 2x + 10 = 0\}$$
# 
# But what does it mean for sets to be equal?

# ## Set equality and subsets
# 
# ### Equality
# 
# Sets are equal when they have the same elements, **order doesn't matter**. 
# 
# $$\{1,2\} = \{2,1\}$$
# 
# Also $\{1,1,2\} = \{1,2\}$, but since duplicate elements are redundant we say that **sets don't have duplicate elements**.

# In[2]:


print({1,2} == {2,1})
print({1,1,2} == {1,2})


# ### Subsets
# 
# $A \subseteq B$ is pronounced "A is a **subset** of B" and it means that everything in A is also in B. For example $\{1,2\} \subseteq \{1,2,3\}$. Sets are considered subsets of themselves so $\{1,2\} \subseteq \{1,2\}$.
# 
# $\{1,2,3\} \supseteq \{1,2\}$ is pronounced "$B$ is a **superset** of $A$".
# 
# If sets are subsets of eachother, they are equal. More formally, if $A \subseteq B$ and $B \subseteq A$ then $A = B$. Consider why this is true. This technique is commonly used in proofs of set equality.

# In[3]:


A = {1,2}
B = {1,2,3}
print(f"A is a subset of B? {A.issubset(B)}")
print(f"B is a subset of A? {B.issubset(A)}")
print(f"B is a subset of A? {B.issuperset(A)}")


# ## Venn Diagrams and Set Operations
# 
# Let's define some sets before we talk about how to visualize them with **venn diagrams** and combine them with **set operations**.

# In[4]:


S = {1,2,3,4,5,6,7,8,9,10}
A = {1,3,5,7}
B = {2,3,4,5}


# 
# ### Venn Diagrams
# 
# In a Venn Diagram each set is represented by a circle. The set $S$ is represented by a black box, think of it as the universe containing all things.
# 
# ![](./images/01-sets/Venn.png)
# 
# ### Union
# 
# $A \cup B$ is "$A$ union $B$". The union of two sets is the set of all elements that are in either set (or in both sets).
# 
# ![](./images/01-sets/AUB.PNG)

# In[5]:


A.union(B)


# ### Intersection
# 
# $A \cap B$ is "$A$ intersect $B$". Elements in the intersection must belong to both sets $A$ and $B$.
# 
# ![](./images/01-sets/AcapB.PNG)

# In[6]:


A.intersection(B)


# ### Difference
# 
# $A-B$ is the difference of $A$ and $B$ and is set of all elements that are in $A$ but not in $B$. It can also be written $A \backslash B$.
# 
# ![](./images/01-sets/A-B.PNG)

# In[7]:


# The complement of set A
A.difference(B)


# ### Complement
# $A^C$ is "the complement of $A$". The complement of a set is all elements that are not in the set. This is relative to our "universe" of possible elements $S$.
# 
# ![](./images/01-sets/AC.PNG)

# In[8]:


# Python doesn't have a "complement" function on sets. You just take the "universal set" S and subtract A from it.
S.difference(A)


# ## Sample Space and Empty Set
# 
# The **sample space** $S$ is the set of all possible elements. In probability there are different outcomes to experiments, and the sample space typically represents all possible outcomes. So when flipping coins the sample space is $\{H,T\}$. There are some identities for the sample space.
# 
# $$A \cup S = S$$
# $$A \cap S = A$$

# In[9]:


print(f"{S} == {A.union(S)}")
print(f"{A} == {A.intersection(S)}")


# ## De Morgan's Laws
# 
# De Morgan's laws are formulas for the complement of a union or intersection of sets.
# 
# $$(A \cap B)^C = A^C \cup B^C \\
# (A \cup B)^C = A^C \cap B^C$$
# 
# One way of memorizing these formulas is that you bring the complement inside the parentheses to both sets and flip the union or intersection upside down.
# 
# Let's see if these laws make any sense. Let $T$ be the set of tennis players and $H$ be the set of hockey players. $(T \cap H)^C$ is the set of people that don't play both tennis and hockey. $T^C \cup H^C$ is people that don't play tennis or they don't play hockey. If I don't play both sports then I either don't play tennis or I don't play hockey, so $(T \cap H)^C \subseteq T^C \cup H^C$. If I don't play tennis or I don't play hockey then it is true that I don't play both sports, so $T^C \cup H^C \subseteq (T \cap H)^C$. This means that the sets are equal, ponder this for some time. A similar argument can be made for the complement of the union. If this is not convincing spend some time with a Venn diagram and see if you can get it to make sense.

# ## 3 or More Sets
# 
# ### Associativity
# You can take the intersection or union of more than two sets.
# 
# $$\{1,2\} \cap \{2,3\} \cap \{3,4\} = \emptyset$$ 
# 
# There are no elements in the intersection of these three sets because no number appears in all three sets, so this is the empty set. 
# 
# Intersections are associative, meaning it doesn't matter what order you take them in. This is also true of unions.
# 
# $$(A \cap B) \cap C= A \cap (B \cap C)$$ 
# $$(A \cup B) \cup C= A \cup (B \cup C)$$
# 
# ### Distributive Property
# 
# If you mix together unions and intersections in an expression it isn't associative.
# 
# $$A \cap (B \cup C) \not= (A \cap B) \cup C$$ 
# 
# But the distributive property is true of intersections and unions. 
# 
# $$A \cap (B \cup C) = (A \cap B) \cup (A \cap C) \\
#  A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$$ 
# 
# It is easier to remember these distributive formulas by comparing them to the way multiplication distributes over addition. $a(b+c)=ab+ac$. Just pretend that the multiplication is an intersection and the addition is a union.
# 
# ### Messy Venn Diagrams
# You can draw a Venn diagram for three sets with three circles. It gets a little complicated. I wouldn't bother drawing a Venn diagram for 4 sets.
# 
# ![](./images/01-sets/Venn3.PNG)
# ![](./images/01-sets/Venn4.PNG)
