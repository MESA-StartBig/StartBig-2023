# `March_28th_PR4C71C4L_1N7R0DUC710N`

Greetings coder!

**Hands-on sessions are here**. Today, we will be reviewing the **fundamental data structures** commonly used in coding interviews. From arrays to linked lists and hash tables, we will briefly examine the properties of a structure, and see how it can be applied to solve problems efficiently. Using LeetCode exercises as a guide, we will practice implementing these data structures and using them to train our minds.

Get ready to sharpen your **problem-solving skills**!

## How to solve a coding interview question

### 1. Visualise the problem -> Draw it out!
---

Ever wondered why coding interviews are traditionally done on whiteboards and videos explaining answers to coding questions tend to use diagrams? Whiteboards make it easy to draw diagrams which helps with problem solving! A huge part of coding is **understanding how the internal state of a program changes** and diagrams are super useful tools for representing the internal data structures state. If you are having a hard time understanding how the solution is obtained, come up with a visual representation of the problem and if necessary, the internal states at each step.

This technique is **especially useful** if the input involves *trees*, *graphs*, *matrices*, *linked lists*.

**Example**: if we're asked to return the elements of a matrix in a spiral order, the best thing that we can do to understand how to build the algorithm is by drawing out the matrix and try to find the pattern (the steps) to retrieve the elements of the matrix in that order. 

### 2. Think about how you would solve the problem by hand​
---
Solving the problem by hand is about **solving the problem without writing any code**, like how a non-programmer would. This already happens naturally most of the time when you are trying to understand the example given to you.

What some people don't realize is that sometimes **a working solution is simply a code version of the manual approach**. If you can come up with a concrete set of rules around the approach that works for every example, you can write the code for it. While you might not arrive at the most efficient solution by doing this, it's a **start which will give you some credit**.

Remember that during a coding interview **time is limited**, and the objective is not getting to the best solution. They want to see and **test your ability to reason around the problem and work out a solution**. An approach so could be the one of trying an implementing **first a working solution** and from that trying to think on possible **optimisations and improvements**.

**Example**: How do you **validate** if a tree is a **valid Binary Search Tree** without writing any code? You first check if the left subtree contains only values less than the root, then check that the right subtree contains only values bigger than the root, then repeat for each node. This process seems feasible. Now you just have to turn this process into code.

**Curiosity**: the very famous [**A\***](https://en.wikipedia.org/wiki/A*_search_algorithm) algorithm, which can be considered an improvement of the [**Dijkstra algorithm**](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm), is based on the *simple intuition* on how we search for the shortest path in a map between two places. Not by exploring the entire map, but by considering more paths that are along the line of the air distance between two cities. 

### 3. Come up with more examples
---

Coming up with more examples is something useful you can do regardless of whether you are stuck or not. It helps you to **reinforce your understanding of the question**, prevents you from prematurely jumping into coding, helps you to **identify a pattern** which can be generalized to any input, which is the solution! 
Lastly, the multiple examples can be used as **test cases** at the end when verifying your solution.

### 4. Break the question into smaller (independent) parts
---

If the problem is large, start with a **high-level function** and **break it down into smaller constituting functions**, solving each one separately. This prevents you from getting overwhelmed with the details of doing everything at once and keeps your thinking structured.

Doing so also **makes it clear** to the interviewer that you **have an approach**, even if you don't manage to finish coding all of the smaller functions.

### 5. Apply common data structures and algorithms at the problem
---

Unlike real-world software engineering where the problems are usually open-ended and might not have clear solutions, **coding interview problems** tend to be smaller in nature and are **designed to be solvable within the duration of the interview**. You can also expect that the knowledge required to solve the problem is not out of this world and they would have been taught during college. Thankfully, the **number of common data structures and algorithms is finite** and a hacky approach which works from my experience is to try **going through all the common data structures** and applying them to the problem.

These are the data structures to keep in mind and try, in order of frequency they appear in coding interview questions:

* **Hash Maps**: Useful for making lookup efficient. This is the most common data structure used in interviews and you are guaranteed to have to use it.
* **Graphs**: If the data is presented to you as associations between entities, you might be able to model the question as a graph and use some common graph algorithm to solve the problem.
* **Stack and Queue**: If you need to parse a string with nested properties (such as a mathematical equation), you will almost definitely need to use stacks.
* **Heap**: Question involves scheduling/ordering based on some priority. Also useful for finding the max K/min K/median elements in a set.
* **Tree/Trie**: Do you need to store strings in a space-efficient manner and look for the existence of strings (or at least part of them) very quickly?

**Routines** i.e. algorithms and approaches that are pretty common

* [Sorting](https://www.geeksforgeeks.org/sorting-algorithms/)
* [Binary search](https://www.geeksforgeeks.org/binary-search/): Useful if the input array is sorted and you need to do faster than O(n) searches
* [Sliding window](https://www.geeksforgeeks.org/window-sliding-technique/)
* [Two pointers](https://www.geeksforgeeks.org/two-pointers-technique/)
* [Union find](https://www.geeksforgeeks.org/introduction-to-disjoint-set-data-structure-or-union-find-algorithm/)
* [Breadth First Search (BFS)](https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/) (topic of the second practical session of StartBig!)
* [Depth First Search (DFS)](https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/) (topic of the second practical session of StartBig!)
* [Topological Sorting](https://www.geeksforgeeks.org/topological-sorting/)

Other common algorithms commonly asked in coding interviews can be found [here](https://www.geeksforgeeks.org/algorithms-for-interviews/).

## How to optimize your approach or solution

After you've come up with an **initial solution** to the coding interview problem, your interviewer would most likely prompt you to optimize the solution by asking **"Can we do better?"**.
In order to determine so we have to analyse the **time complexity** and the **space complexity** our algorithm and understand what is the **minimum complexity** of the problem. 

### How to optimize time complexity
---

### 1. Identify the Best Theoretical Time Complexity of the solution​
---

The **Best Theoretical Time Complexity**(from now on, BTTC) of a solution is a **time complexity you know that you cannot beat**.

Some simplified examples:

* The BTTC of finding the sum of numbers in array is O(n) because you have to look at every value in the array at least once
* The BTTC of finding the number of groups of anagrams is O(nk) where n is the number of words and k is the maximum number of letters in a word because you have to look at each word at least once and look at each character in each word at least once
* The BTTC of finding the number of islands in a matrix is O(nm) where n is the number of rows and m is the number of columns because you have to look at each cell in the matrix at least once

*Why is it important to know the BTTC?* 
So that you **don't go down the rabbit hole** of trying to find a **solution that is faster than the BTTC**. The fastest practical solution can only ever be as fast as the BTTC, not faster than the BTTC. The BTTC is **not necessarily achievable in practice** (hence theoretical), it just means you can **never find a real solution that is faster than it**. 

If your **initial solution is slower than the BTTC**, there could be opportunities to **improve** such that you can attain the BTTC (but not always the case). It wouldn't hurt to **mention the BTTC** to your interviewer, which will be taken as a **positive signal** and also to remind yourself that you should not try to come up with something faster than the BTTC.

Some people might think that the BTTC is simply the **total number of elements in a data structure**, because you need to go through each element once. **This is not always true**. 
The most **famous example** would be finding a number in a sorted array of numbers. The sorted property changes things a whole lot:

* Finding a number would be O(log(n)) because you can use a binary search.
* Finding the largest number would be O(1) because it is the last value in the array.

This is why it is important to **pay attention to every detail given about the question**. **Be careful not to determine the incorrect BTTC** due to lack of attention to the question details!

With the correct BTTC determined, you now know the **time complexity** of the **optimal solution** lies between your **initial solution** and the BTTC and can work your way towards it. 

If your solution already has the BTTC and the **interviewer is asking you to optimize furthe**r, there are usually two things they are looking out for:

* Do even less work. Your solution could be O(n) but making **two passes of the array** and the interviewer is looking for the solution that uses a **single pass**.
* Use less space. Refer to the section below on optimizing **space complexity**.

### 2. Identify overlapping and repeated computation
---

A naive/brute force solution often **executes the same operation over and over again**. When the code is doing an expensive operation that has been done before, take a moment to step back and consider if you can **reuse results** from previous computations. **Dynamic programming (DP)** (topic of the third practical session of StartBig!) is the most obvious type of questions you can entirely leverage past computations. There are **non-DP questions** that can leverage this technique too, although **not as straightforward** and might **require a preprocessing** step.

### 3. Try different data structures
---

**Choice of data structures is key to coding interviews**. It can help you to reach a solution for the problem, it can also help you to optimize your existing solution. Sometimes it's worth going through the exercise of **iterating through the data structures you know** once again.

*Is lookup time slowing your algorithm down?* 
In general, most lookup operations should be O(1) with the **help of a hash table**. If the lookup operation in your solution is the bottleneck to your solution's time complexity, more often than not, you can **use a hash table to optimize** the lookup.

### 4. Identify redundant work
---

Here are a **few examples of code which is doing redundant work**. Although making these mistakes might not change the overall time complexity of your code, you are also **evaluated on coding abilities**, so it is important to write as efficient code as possible.

#### Don't check conditions unnecessarily​

These are Python examples where the second check is redundant.

* `if not arr and len(arr) == 0` - the first check already ensures that the array is empty so there is no need for the second check.
* `x < 5 and x < 10` - the second check is a subcondition of the first check.

#### Mind the order of checks​

* `if slow() or fast()` - There are two operations in this check, of varying durations. As long as one of the operations evaluates to `true`, the condition will evaluate to `true`. Most computers execute operations in order from left to right, hence it is more efficient to put the `fast()` on the left.
* `if likely() and unlikely()` - This example uses a similar argument as above. If we execute `unlikely()` first and it is `false`, we don't have to execute `likely()`.

#### Don't invoke methods unnecessarily​

If you have to **refer to a property multiple times** in your function and that property has to be **derived from a function call**, **cache the result as a variable** if the value doesn't change throughout the lifetime of the function. The **length of the input array** is the most common example. Most of the time, the length of the input array doesn't change, declare a variable at the start called `length = len(array)` and use `length` in your function instead of calling `len(array)` every time you need it.

#### Early termination

Early termination. **Stop after you already have the answer**, return the answer immediately. Here's an example of leveraging early termination. 
Consider this basic question *"Determine if an array of strings contain a string regardless of case sensitivity"*. The code for it:

```
def contains_string(search_term, strings):
  result = False
  for string in strings:
    if string.lower() == search_term.lower():
      result = True
  return result
```

Does this code work? Definitely. Is this code as efficient as it can be? **Nope**. We only need to know if the **search term** exists in the array of strings. We can stop iterating as soon as we know that there exists the value.

```
def contains_string(search_term, strings):
  for string in strings:
    if string.lower() == search_term.lower():
      return True # Stop comparing the rest of the array/list because the result won't change.
  return False
```

Most people already know this and already do this outside of an interview. However, in a stressful interview environment, people tend to forget the most obvious things. **Terminate early from loops where you can**.

#### Minimize work inside loops​

Let's further improve on the example above to solve the question *"Determine if an array of strings contain a string regardless of case sensitivity"*.

```
def contains_string(search_term, strings):
  for string in strings:
    if string.lower() == search_term.lower():
      return True
  return False
```

Note that you are calling `search_term.lower()` once per loop of the for loop! **It's a waste** because the `search_term` **doesn't change throughout the lifecycle** of the function.

```
def contains_string(search_term, strings):
  search_term_lowercase = search_term.lower()
  for string in strings:
    if string.lower() == search_term_lowercase:
      return True
  return False
```

Minimize work inside loops and **don't redo work you have already done if it doesn't change**.

#### Be lazy

Lazy evaluation is an evaluation strategy which **delays the evaluation of an expression until its value is needed**. Let's use the same example as above. We could technically improve it a little bit:

```
def contains_string(search_term, strings):
  if len(strings) == 0:
    return False
  # Don't have to change the search term to lower case if there are no strings at all.
  search_term_lowercase = search_term.lower()
  for string in strings:
    if string.lower() == search_term_lowercase:
      return True
  return False
```

This is considered a **micro-optimization** and most of the time, strings won't be empty, but I'm using it to **illustrate the example** where you don't have to do certain computations if they aren't needed. This also applies to **initialization of objects** that you will need in your code (usually hash tables). If the **input is empty**, there's **no need to initialize any variables**!

### How to optimize space complexity
--- 

Most of the time, **time complexity is more important** than space complexity. But when you have already reached the optimal time complexity, the interviewer might ask you to **optimize the space your solution** is using (if it is using extra space). Here are some techniques you can use to improve the space complexity of your code.

### 1. Changing data in-place/overwriting input data
---

If your solution **contains code to create new data structures to do intermediate processing/caching**, memory space is being allocated and can sometimes be seen as a negative. A trick to get around this is by **overwriting values in the original input array** so that you are not allocating any new space in your code. However, be careful not to destroy the input data in irreversible ways if you need to use it in subsequent parts of your code.

A possible way which works (but you should never use outside of coding interviews) is to **mutate the original array and use it as a hash table** to store intermediate data.

Note that in Software Engineering, **mutating input data is generally frowned upon** and makes your code harder to read and maintain, so changing data in-place is mostly something you should do **only in coding interviews**.

### 2. Change a data structure
---

*Data structures again!?* 
Yes, data structures again! **Data structures are so fundamental to coding interviews** and mastery of it makes or breaks your interview performance. Are you using the best data structure possible for the problem?

**Example**​
You're given a list of strings and want to find how many of these strings start with a certain prefix. What's an efficient way to store the strings so that you can compute your answer quickly? A Trie is a tree-like data structure that is very efficient for storing strings and also allows you to quickly compute how many strings start with a prefix.

## LeetCode introduction


Leetcode is famous for being a perfect platform for **practicing coding problems** and to master coding interviews. This platform might scare a bit newbies so we will go through some basic best practices to get us started and prepare together at best for the coding interviews!

### Problem difficulty
---

Solving problems in right order is very important, trying to solve an hard question before ever trying to solve a easy question might get you frustrated and discouraged before even solving a question.
Try to have a **step by step** process with an increasing level of difficulty, like a videogame. 

### General suggestions when doing coding exercises
---

* When trying to solve a question, try to **provide a solution even if not efficient**. During the coding interview you'll be evaluated on your ability to provide one that works. Then you could move on trying to optimise it, but the first this is finding a solution. 

* A lot like the *Algoritmi e Principi dell'Informatica* Course in Politecnico di Milano, try to solve the questions first on your own, and **don't look at solutions straight away**. You will "waste" that problem if you directly look at the solution, without learning the process behind solving an interview question. 

* Also it's crucial to start to learn data structures and use them in context **without knowing** the exercise can be solved with that **specific data structure**! We won't have this hint in a coding interview.

* **Continue practing** over time. Much like a video game, **practice makes perfect**. Your abilites will improve and you'll be able to solve many more problems at first sight. 

* Take every fail, every **error as a learning opportunity**. Each one of us might have a lack-cluster knowledge of algorithms and data structures. Don't feel bad if you don't remember a particular trick. Try to improve on it a get it the next time

* **It's more fun to play with friends**. Try to create a group of people working with you to improve each other programming skills, creating competitions or partecipating to ones. Here's a list of the most famous ones:
    
    * [Google](https://codingcompetitions.withgoogle.com)
    * [Meta](https://www.facebook.com/codingcompetitions/)
    * [Microsoft](https://imaginecup.microsoft.com/en-us/Events)
    * [LeetCode](https://leetcode.com/contest/)
    * [Kaggle](https://www.kaggle.com/competitions)
    * [GeeksForGeeks](https://www.geeksforgeeks.org/contests/)
    * [CodeForces](https://codeforces.com/contests )
    * [CodeChef](https://www.codechef.com/contests)
    * [TopCoder](https://www.topcoder.com/thrive/tracks?track=Competitive%20Programming)
    * [AtCoder](https://atcoder.jp)
    * [HackerEarth](https://www.hackerearth.com/challenges/)
    * [HackerRank](https://www.hackerrank.com/contests)

    An interesting competition, a bit different from the others, cool to do during the month of December is the [Advent of Code](https://adventofcode.com): a coding challenge with increasing levels of difficulty for each day of the month of december. 


## Exercises for this session

| Problem               |                Topic                 | LeetCode tag |                              Hyperlink                               |
| :-------------------- | :----------------------------------: | :----------: | :------------------------------------------------------------------: |
| `0N3`                 |           Two sum, arrays            |     Easy     |         [`CLICK_ME`](https://leetcode.com/problems/two-sum/)         |
| `TW0`                 | Merge two sorted lists, linked lists |     Easy     | [`CLICK_ME`](https://leetcode.com/problems/merge-two-sorted-lists/)  |
| `THR3E`               |  Top K frequent elements, _hidden_   |    Medium    | [`CLICK_ME`](https://leetcode.com/problems/top-k-frequent-elements/) |
| `F0UR` (DIW homework) |        Valid sudoku, matrixes        |    Medium    |      [`CLICK_ME`](https://leetcode.com/problems/valid-sudoku/)       |
| `F1V3` (DIW homework) |    Trapping rain water, _hidden_     |     Hard     |   [`CLICK_ME`](https://leetcode.com/problems/trapping-rain-water/)   |


## Sources

The guide about how to answer to coding interview questions can be found [here](https://www.techinterviewhandbook.org/coding-interview-techniques/). 
Other resources about coding interviews and preparation can be found [here](https://wiki.superherovalley.fun/link_utili/coding/).