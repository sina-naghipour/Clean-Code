# Goal.
in the process of reading this book i will find a piece of bad good, and in each chapter i will improve the said topics.

# Chapter 1 : Clean Code


why should we learn to code? shitty idea in my opinion, ai models are doing a better job. most of the code is generated rather than written.

we have specifications, and ai models can generate code based on those. but this idea is wrong.

specifying requirements in such detail that a machine can execute them is programming, such a specification is code.

even humans can't understand vague feelings of other humans. how could computers do such a thing?

so there will always be code, there cannot be a computer that understands our vague needs and specifications.

### **code** is the language in which we ultimately express the requirements.

**code** will never be eliminated.

messy code makes the productivity of the code to asymptotically approach zero. after productivity decreases in order to increase it, management decides to recruit new members. **but that new member does not know the difference between a change that matches the design, or a change that tangles the design.**

![alt text](image.png)

eventually, bad code, leads to another team redesigning the current working but no so efficiently system, and this is not cost-friendly and this battle of to two teams competing to build a system can last forever.

### good code rots into bad code, rather quickly.


### Programming Conundrum

prorgammers face a conundrum of basic values, they all know bad code, slows them down. yet, still under the pressure of deadlines they feel the need of making a mess.

it's no good to write clean code without knowing what clean code is.

### What is `Clean Code` like?

a good metaphor is that, a building with broken windows looks like nobody cares about it. so other people stop caring. they allow more windows to become broken. eventually they actively break them. they despoil the facade with graffiti and allow garbage to colect. one broken window starts the process toward decay.

paying attention to details in programming is `error handling`, `memory leaks`, `race condition`.

clean code does one thing well.

clean code is `focused`. each function each class each module exposes a single-minded attitude that remains entirely undistracted and unpolluted, by surrounding details.

clean code is straightforward lines of control.

##### here the book rambles about different perspectives of programming languages creators on clean code, i couldn't be arsed to read it, soooo :))))

### Who are we? `@authors`

@authors remembers us that we are authors, what do authors have? `readers`. so next time writing a line of code remember that you are an author, writing for readers who will judge your effort.

`why bother?` old editors like Emacs used to keep track of every keystroke. you could play it back. most of this time went to scrolling and navigating to other modules.

### ratio of time spent reading to time spent writing is 10:1

even if writing clean code makes writing harder, it eases the reading part. so fucking write clean code.

### The Boy Scout Rule

#### Leave the campground cleaner than you fonud it.

if we all checked-in our code a little cleaner than when we checked it out the code simply could not rot. the cleanup doesnt have to be something big. change a variable name for the better, break up one function that's a little too large, eliminate one small bit of duplication, clean up one composite if statement.

the final shithousery of this chapter is the fact that it tells you, books on art don't promise to make you an artist. all they can do is give you some of the tools, techniques and thought processes that other artists have used.

### In this book, we learn the thought process of good programmersand the tricks, techniques, and tools that they use.

# Chapter 2 : Meaningful Names

it is easy to say that names should reveal intent. what we want to impress upon you is that we are `serious` about this.

take time with your names and change them when you find better ones. everyone who reads your code will be happier if you do so(even you).

the name of a variable, function or class should answer all the big questions.

it should tell you:
- **why it exists.**
- **what it does.**
- **how it is used.**

if a name needs a comment, it does not reveal its intent.

```c++
int d; // elapsed time in days
```

this variable does not evoke any sense of elapsed time, nor days.

### we should choose a name that specifies what is being measured and the unit of that measurement.

```c++
int elapsedTimeInDays;
int daysSinceCreation;
int daysSinceModification;
int fileAgeInDays;
```

choosing names that reveal intent, makes understanding and changing code much easier.

### Example of a simple yet hard to understand code.
```cpp
public List<int[]> getThem() {
    List<int[]> list1 = new ArrayList<int[]>();
    for (int[] x : theList)
        if (x[0] == 4)
            list1.add(x);
    return list1;
}
```

### Previous example but with good variable name choices.

```cpp
public List<int[]> getFlaggedCells() {
    List<int[]> flaggedCells = new ArrayList<int[]>();
    for (int[] cell : gameBoard)
        if (cell[STATUS_VALUE] == FLAGGED)
            flaggedCells.add(cell);
    return flaggedCells;
}
```

the simplicity of the code has not been changed but the code became more `explicit`.

even more, we can create a class for cells instead of using an array of `int's` and that could include an intention revealing function (call it `isFlagged`) to hide the magic numbers.

```cpp
public List<Cell> getFlaggedCells() {
    List<Cell> flaggedCells = new ArrayList<Cell>();
    for (Cell cell : gameBoard)
        if (cell.isFlagged())
            flaggedCells.add(cell);
    return flaggedCells;
}
```

### Avoid Disinformation

programmers must avoid leaving false clues that obscure the meaning of code.

variables like `hp`, `aix` and `sco` are not good because they are variants of Unix platforms or variants.

**do not refer to a grouping of accounts as an `accountList` unless it's actually a `List`.**

if it's not a list refer to it as `accountGroup` or `bunchOfAccounts` or just `Accounts`.

**Beware of using names which vary in small ways.**

### why should we make names, `obviously` different.

```cpp
getActiveAccount ();
getActiveAccounts();
getActiveAccountInfo();
```

**how is a programmer able to acknowledge which function to call?**

**in the absence of specific conventions** the variable `moneyAmount` is indistinguishable from `money`, `customerInfo` from `customer`.

### Use Pronounceable names

make names pronounceable so that your code could be quote on quote `spoken`.

why does it matter? **programming is a social activity.**

### Use Searchable names

single letter variables cannot be searched.

single letter variables can `ONLY` be used as local variables inside short methods.

### the length of a name should correspond to the size of its scope.

