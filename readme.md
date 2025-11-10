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

### Avoid encoding

if a variable or constant might be seen or used in multiple places in a body of code, it is imperative to give it a `search-friendly name`.

### Do not add member prefixes

```cpp
    m_dsc = name; // this is a member function.
```

### Avoid naming interfaces and implementations old fashioned

```java
// Interface
public interface ShapeFactory {
    Circle createCircle();
    Rectangle createRectangle();
}

// Concrete implementation
public class ShapeFactoryImpl implements ShapeFactory {
    @Override
    public Circle createCircle() { ... }

    @Override
    public Rectangle createRectangle() { ... }
}
```

### Avoid mental mapping

readers should not mentally translate your names into other names they already know.

this problem arises from a choice to use neither problem domain terms nor solution domain terms.

traditionally we use i,j,k for loop counters if its scope is very small. if they don't conflict with anything, this kinda naming is a good choice.


### Class names

class and object names should have noun or noun phrase names like `Customer`, `WikiPage`, `Acconut` and `AddressParser`.

a class name should `not` be a `verb`.

### Method names

method names should be `verbs`.

accessors, mutators and predicates should be named for their value and prefixed with `get`, `set` and `is`.

when constructor are overloaded use static factory methods with names that describe the argument like `Complex.FromRealNumber(23.0);`.

### Don't be cute white guy.

your sense of humor is trash, don't try to act funny.

### Pick one word per concept.

don't try to have `fetch`, `retrieve` and `get` as equivalent methods for different classes.

### Don't pun.

do not use the same word for two concepts.

if you have multiple classes and they all have an `add` method, as long as the parameter lists and return values of the various `add` methods are semantically equivalent, all is well.

### Use solution domain names

your audience are mainly programmers so using cs terms, algorithms or pattern names is an okay thing. like a `JobQueue`.

### Use problem domain names

when there is no programmer for what you do, use names from problem domain. at least the programmer could ask a domain expert what it means.

### Add meaningful context

if you see `state` would you know its for an `Address`?
no, so instead of `state` use `addrState`.


### Final Rambles.

hardest thing about choosing good names is that it reuires good descriptive skills and a shared cultural background.

# Chapter 3 : Functions

first rule, they should be `small`.

### Blocks and Intending

blocks within `if`, `else`, `while` and so on should be 1 line long, that line should probably be a function call.

the indent level of a function should not be greater than 1 or 2.
functions should do one thing. they should do it well. they should do it only.

if the function contains steps at many different levels of abstraction, it is not doing one thing.

another way to know that a function is doing more than `one` thing, is if you can extract another function from it with a name that is not merely a restatement of its implementation.

### Sections within functions

if a function contains, declaration, initialization and sieve, or something of this fabric, it is doing more than one thing.

### One level of abstraction per function

we need to make sure that the statements within our function are all at the same level of abstraction.

an example : `getHtml();` high level, `PathParser.render(pagePath)` intermediate level, `.append('\n')` is a low level of abstraction.

once `details` are mixed with essential concepts, more and more details tend to appear within the function.

### The stepdown rule

we want the code to read like a top-down narrative.

we want every function to be followed by those at the next level of abstraction so that we can read the program, descending one level of abstraction at a time as we read down the list of functions.

it is hard to write functions that stay at a single level of abstraction.

### Switch statement

we cannot avoid `switch` statements, but we can make sure that each `switch` statement is buried in a low-level class and is never repeated.

### Use descriptive names

you know you are working with clean code when each routine turns out to be pretty much what you expected.

the smaller and more focused a function is, the easier it is to choose a descriptive name.

a long descriptive name is better than a long descriptive comment.

### Function arguments

the ideal number of arguments for a function is `zero`. then `one`, closely `two`.

you should avoid using `three` argument functions.

we do not expect the information going `out` of a function through `argument`, but by `result`.

`Flag arguments` are terrible.

two arguments for a function like `Point` is perfectly reasonable, because pay attention `these two arguments are ordered components of a single value`.

how the hell do we transform two argument functions into one argument function?

if lets say our function accepts an argument like `outputStream`, this argument could be passed to the function, via making that function a method of a class and that `outputStream` is a member of this class.

### Argument objects

when a function seems to need more than two or three arguments, it is likely that some of those arguments need to be wrapped into a class of their own.

```cpp
Circle makeCircle(double x, double y, double radius);
Circle makeCircle(Point center, double radius);
```

`x` and `y` are a part of a concept that deserves a name of its own.

### Argument list

if some of arguments are treated identically, they are equivalent to a single argument of type `List`.

### Verbs and keywords

for monad(1 argument) functions -> verb/noun pair. `WriteField(name);`

using good names for functions, removes the fact that we have to remember the order of the arguments.

### Have no side effect

your function promised to do one thing, and it shouldn't hiddenly do other things.

if your function says `CheckPassword`, but it hiddenly also initializes the session by calling a function called `initSession`, someone who doesn't know this, and just read the function's name, now accidentaly initialized a session as well!!!

this creates temporal coupling -> calling `CheckPassword` is only safe to call when it is okay to initialize a session.

the name should be `CheckPasswordAndInitializeSession`.

### Output arguments

`appendFooter(s)` s is an output argument rather than input argument.

is s the footer? is something added to s?

this makes to `double-check` meaning that you have to at least the functions signature.

nowadays, the purpose of object oriented keyword `this` is actually an output argument.
so do this.

`report.appendFooter()`.

### Command query seperation

a function either should do something, or answer something, not both.

`set('username','unclebob')`.

the author used the verb set to be a verb, but in the context of the `if` statement it feels like an adjective.

if the `username` was previously set to `unclebob` and not set the `username` attribute to `unclebob` and if that worked then ... .

the function could be named `setAndCheckIfExists`, this still doesnt help the readablity of the `if` statement. the real solution is to seperate `command` from `query`.

### Exceptions over error codes

when you return the error code, you make caller forced to deal with the error immediately.

### Extract try/catch blocks

try/catch blocks mix error processing with normal processing.

it is better to extract the bodies of the `try` and `catch` blocks out into functions of their own.

```cpp
 public void delete(Page page) {
 try {
 deletePageAndAllReferences(page);
 }
 catch (Exception e) {
 logError(e);
 }
 }
```

this function is all about `error processing`.

the function `deletePageAndAllReferences` is all about deleting a page.error handling can be ignored. this provides a nice seperation that makes the code easier to understand and modify.

### Error handling is one thing

functions should do one thing, error handling is one thing. fucking remember.

### Don't repeat yourself

duplication may be the root of all evil in a software.

### Structured programming

the man himself, greatest of all time, the reason i failed algorithms, mother of all routing problems, dijkstra the great, had a rule for structured programming. every function, every block within a function, should have one entry and one exit. following these rules means that there should only be one `return` statement in a function, no `break` or `continue` statement in a loop, and never, ever, ever, everrrrrrr, the trashy `goto` statement nobody likes.(boooooooooooo)

this rule is actually for big functions, chunky ones. but if your functions are small, the occasional multiple `return`, `break`, or `continue` does not harm a fly.

### How to write these functions?

like writting an essay, you write your functions at first, then write some unittest.then you start massaging(pause) the code, refining it, changing names, splitting functions and so on, while keeping the tests passed.

at the end you have functions with clean code rules.

### Final rambles of this chapter

every system built is from a domain-specific language designed by the programmers to describe that system.

functions are the verb of that language, classes are the nouns.

### the art of programming is actually the art of designing a language.

systems are stories to be told rather than programs to be written.