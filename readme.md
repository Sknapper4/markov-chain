# Advanced Problem 16
By Stephen Knapper, Cameron Palmer, and Colson

## Introduction
The goal of this problem was to set up a graph, traverse the graph, 
and determine how often, on average, that each vertex (node) is visited. 

## Our Process
1. We create a mapping of our graph and a matrix representation `M`
    where
    <pre>
   M = [
        [0, .5, 0, .5, 0, 0, 0, 0],
        [1/3, 0, 1/3, 0, 1/3, 0, 0, 0],
        [0, .5, 0, 0, 0, .5, 0, 0],
        [.5, 0, 0, 0, .5, 0, 0, 0],
        [0, .25, 0, .25, 0, .25, .25, 0],
        [0, 0, 1/3, 0, 1/3, 0, 0, 1/3],
        [0, 0, 0, 0, .5, 0, 0, .5],
        [0, 0, 0, 0, 0, .5, .5, 0]
    ]
    </pre>
2. We then create our Graph `graph` and define our map
    * First we take our map(dictionary) and create a node from 
        each value
    * Next we define which nodes are connected to that node
    * Lastly, we initiate the number of visits to 0
3. After defining the graphs layout, we `get_avg_visits` and 
    traverse the graph `num_iters` times
4. When traversing the graph, we start at node `a` and visit
    `nodes_to_visit` nodes each time the function is called
    * When we visit a node, we randomly (and proportionately) select 
        the next node to travel to and, upon visiting that node, we 
        increment the number of visits by 1
5. After we traverse the graph `num_iters` times, while still in 
    `get_avg_visits` we call `avg_out_visits`
     * Here were divide the total number of visits for each node
        by the total number of all visits
6. We then continue in `get_avg_visits` by dividing each nodes
    value by `num_iters` and round to 2 decimal places
7. These values are also stored in an vector(array) V where
    <pre>
   V = [0.1, 0.15, 0.1, 0.1, 0.2, 0.15, 0.1, 0.1]
    </pre>
8. After we finish computing our averages, we check to ensure that our 
    averages are also an Eigenvector of matrix `M`
    

## Our Results
As we explained above, 
<pre>
   V = [0.1, 0.15, 0.1, 0.1, 0.2, 0.15, 0.1, 0.1]
</pre>
These are the average visits of each vertex in the graph.\
As was explained above, we check by multiplying `V` and `M` and 
our resulting vector is  
<pre>
[0.1, 0.15, 0.1, 0.1, 0.2, 0.15, 0.1, 0.1]
</pre>
Notice, our Eigenvalue is 1 and the vector that was returned
equals `1 * V`. 

## Conclusion
Therefore, we have proven that the vector of averages we produced is
correct and, more importantly, is an Eigenvector of our matrix `M`.



#### Run the Code
To run this code
1. Ensure you have python3.7 installed on your machine.
    * A virtual environment is ideal but not necessarily required.
2. Run `pip install -r requirements.txt`
3. Run `python3.7 markov_chain.py`