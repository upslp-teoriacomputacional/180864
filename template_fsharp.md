## Python Program to Illustrate Different Set Operations

  <li>1. In this example, we have defined two set variables and we have performed different set operations: union, intersection, difference and symmetric difference.,  </li>
  <li>2. To understand this example, you should have the knowledge of the following Python programming topics:  </li>
  <li>3.Python Sets  </li>
  <li>4. Python Input, Output and Import  </li>
  <li>Python offers a datatype called set whose elements must be unique. It can be used to perform different set operations like union, intersection, difference and symmetric difference. </li>
  <li>Is the Quadratic Allocation Problem NP-complete or is it in P? Either give a reduction to show it is NP-complete or give a polytime algorithm to solve it. </li>

 
</ol>
Aside: This problem arose during some consulting I was doing, where the integers represented the sizes of different software jobs, and the quadratic term is there because the cost of implementing software goes up faster than linearly with the size of the job. 
<p></p>

## Source Code example 
(https://dotnet.microsoft.com/learn/languages/fsharp-hello-world-tutorial/intro)

#### Hello World Program in F#
##### Purpose
Install .NET and create your first application written in the F# programming language.

##### Prerequisites
None.

##### Time to Complete
10 minutes

##### Scenario
A simple application written in F# that prints Hello, World! to the console.

Hello World! program in every programming language gives the beginner programmer a leap in proceeding further in the new language. The basic Hello world program just gives the output by printing ” Hello World!” on the screen. In Perl, a basic program consists of the following steps of execution,

##### Step 1: Transfer the file to F# Compiler:
Create your app
In your command prompt, run the following commands:

```F#
dotnet new console -lang F# -o myFSharpApp
cd myFSharpApp
```

##### Step 2: Pragma in Perl:
The dotnet command creates a new application of type console for you. The -lang parameter specifies the F# programming language and -o creates a directory named myFSharpApp where your app is stored, and populates it with the required files. The cd myFSharpApp command puts you into the newly created app directory.

The main file in the myFSharpApp folder is Program.fs. By default, it already contains the necessary code to write "Hello World from F#!" to the Console.

```f#
open System

[<EntryPoint>]
let main argv =
    printfn "Hello World from F#!"
    0 // return an integer exit code

```
#### Step 3: Run your app:
In your command prompt, run the following command:

```powershell
dotnet run
```

## Help - ?

In this program, we take two different sets and perform different set operations on them. This can equivalently done by using set methods.
<small> <a href="" target="\_blank">@</a> for this feature!</small>


Visit <a href="https://github.com/upslp-teoriacomputacional/180864/" target="\_blank"> (Programming set in Python).

<small>@jc-gi<a href="https://github.com/jc-gi" target="\_blank"></a> for the language support! </small>

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
