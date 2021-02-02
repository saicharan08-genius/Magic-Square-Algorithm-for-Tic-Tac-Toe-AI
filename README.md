# Magic Square Algorithm for Tic Tac Toe AI

![Magic Square](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Magicsquareexample.svg/1200px-Magicsquareexample.svg.png)

# How Magic Square Algorithm works?

Say this is our Tic Tac Toe Board:

![Tic Tac Toe Board](https://innerpiecesgallery.com/wp-content/uploads/Tic-Tac-Toe-Grid-Numbers.jpg)(There are numbers in the shell just for the sake of simplicity while explaining the algorithm)

My algorithm corresponds each shell in the Tic Tac Toe to that on the Magic Square. For example Shell 1 corresponds to integer values 2 and shell 2 corresponds to integer value 7.
Let us say human chooses shell number 1 and the AI chooses shell 5. Human next chooses shell number 2 in an attempt to finish the first row. Then the AI will see the corresponding values for each shell. In this example, we know this:

```
valueOf(shell 1) + valueOf(shell 2) + valueOf(shell 3) = 15
```
