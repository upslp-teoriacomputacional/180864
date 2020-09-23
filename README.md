# Instructions
1. Program in the assigned programming language (F #, Perl, Rust)
2. The programs are located in the (source_code) folder.
3. The code must be compiled on any operating system.
4. The code is uploaded at https://github.com/upslp-teoriacomputacional/matricula
5. Example. 00180864_sets. go
6. The program will be evaluated according to the rubric attached.
7. The evidence of the developed program is the template of the commented source code.
8. You can also show the operation of the programs in the beginning or term of class before the deadline.

## Rubric
---
#### Functionality:
The program works correctly and all the input variables are validated.
#### Logic reasoning:
It is a very refined compact code.
#### Code structuring:
If you use indentation, spaces and line spacing that gives greater clarity.
#### Documentation:
The presentation includes the name, surname, major, name of the specialty professor, name of the institution and enrollment, well-defined objectives documented and parts of the well-documented code.
---

### Help -?
#### <li><em>Programming Languages doc comments.</em>

##### <a href = "https://fsharp.org/learn/">writing F# comments</a>.


##### <a href = "https://perldoc.perl.org/perl.html"> writing Perl comments</a>.


##### <a href = "https://www.rust-lang.org/learn"> writing Rust comments</a>.



### Writing Clear Code

The overarching goal when writing code is to make it easy to read and to understand. Well-written programs are easier to debug, easier to maintain, and have 
fewer errors. Writing a program is a lot like writing an essay. When writing an essay, your message is more convincing when it is accompanied by proper grammar and punctuation. When writing computer programs, you should follow the same principle. It is even more important when programming since someone may be assigned to maintain and support your code for long periods of time. You will appreciate the importance of good style when it is your task to understand and maintain someone else's code!

#### Commenting

Example
<table>
<TR><TD><pre>
/*---------------------------------------------------------
 *  Here is a block comment that draws attention
 *  to itself.
 *---------------------------------------------------------*/
</pre></td></tr>
</table>

<table>
<TR><TD><pre>
/* *****************************************************************************
 *  Name:    Alan Turing
 *  NetID:   aturing
 *  Precept: P00
 *
 *  Description:  Prints 'Hello, World' to the terminal window.
 *                By tradition, this is everyone's first program.
 *                Prof. Brian Kernighan initiated this tradition in 1974.
 *
 *  Written:       5/03/1997
 *  Last updated:  8/22/2018
 *
 *  % python 3 HelloWorld.python
 *  % pyton HelloWorld
 *  Hello, World
 *
 **************************************************************************** */
</pre></td></tr>
</table>


<p><li> Comment every important variable name (including 
all instance variables).


<table>
<TR><TD><pre>
private double rx, ry;    //  position
private double q;         //  charge
</pre></td></tr>
</table>

If you prefer, you may use
<a href = "https://en.wikipedia.org/wiki/Structured_programming">doc comments</a>.


<table>
<TR><TD><pre>
public static void main(String[] args) { 
   boolean nesting = true;
   /* /* */ nesting = false; // */ 
   System.out.println(nesting);
} 
</pre></td></tr>
</table>


<table>
<TR><TD><pre>
a*x + b
</pre></td></tr>
</table>


<table>
<TR><TD><pre>
for(int i=0;i&lt;n;i++)    vs.      for (int i = 0; i < n; i++)
</pre></td></tr>
</table>


<table>
<TR><TD><pre>
    //This comment has no space           //  This comment has two 
    //after the delimiter and is          //  spaces after the delimiter
    //difficult to read.                  //  and is easier to read.
</pre></td></tr>
</table>


<table>
<TR><TD><pre>
int n      = Integer.parseInt(args[0]);      //  size of population
int trials = Integer.parseInt(args[1]);      //  number of trials
</pre></td></tr>
</table>


<table>
<TR><TD><pre>
//  K&R style indenting                   
public static void  main(String[] args) {
    System.out.println("Hello, World");
}

//  BSD-Allman style indenting
public static void main(String[] args)
{
    System.out.println("Hello, World");
}
</pre></td></tr>
</table>


#### References
<p><b>A.</b> <a href = "http://www.cs.princeton.edu/~bwk/tpop.webpage">The Practice
of Programming</a> by Brian W. Kernighan and Rob Pike is a classic.


<p><b>A.</b><a href = "http://checkstyle.sourceforge.net/">Checkstyle</a>.
If you followed our Windows, Mac OS X, or Linux instructions, <em>IntelliJ</em> is configured
to run Checkstyle automatically while you are editing.


<p><b>A.</b><a href = "http://mindprod.com/jgloss/unmain.html">unmaintainable code</a>
and here's <a href = "http://archive.is/Pn5hH">another</a>.


<p></p>
Don't be afraid of email harvesting, write your email properly and the page will perform programming obfuscation.

<a href="" target="\_blank">@</a> 
</small>
</body>