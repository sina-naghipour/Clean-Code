| Chapter 2 | Note |
| --- | --- |
|  | the name of a variable, function or class should answer all the big questions. it should tell you `1. why it exists`, `2. what it does`, `3. how it is used.` |
|  | do not refer to a grouping of accounts as an `accountList` unless it's actually a `List`. |
|  | Beware of using names which vary in small ways. like `XYZControllerForEfficientHandlingOfStrings` and `XYZControllerForEfficientStorageOfStrings`. |
|  | Programmers create problems for themselves when they write code solely to satisfy a compiler or interpreter. |
|  | it is not sufficient to add number series or noise words, even though the compiler is satisfied. if names `must` be different, then they should also `mean` something different. |
|  | do not use noise words, if you have a class called `Product`, and another one which is different, do not name it `ProductInfo` or `ProductData`. |
|  | Noise words are redundant. the word `variable` should not appear in a variable name. the word `table` should never appear in a table name. How is `NameString` better than `Name`? |
|  | the `length` of a variable should correspond to the size of its `scope`. |
|  | use `searchable` and `pronouncable` names. |
|  | avoid `encoding` names, because if a new employee has the pain to understand the complexity of the code, it is a pain in the ass to learn `encoding language` as well. |
|  | naming loop counters `i,j,k` is traditional. if the scope is small, `okay` to use. |
|  | `clarity` is `king`. |
|  | a class name should `not` be a `verb`. |
|  | `class` and `object` names should be `nouns`. |
|  | `method` names should be `verb`. |
|  | accessors, mutators and predicates should be named for their value and prefixed with `get`, `set` and `is`.|
|  | when constructor are overloaded use static factory methods with names that describe the argument like `Complex.FromRealNumber(23.0);`.|
|  | Pick one word per concept. don't be like `fetch`, `retrieve`, `get`. |
|  | do not use the same word for two concepts. |
|  | where there is programmer to read, use `solution domain names` like algorithms and etc. when there is none, use `problem domain names`. |

