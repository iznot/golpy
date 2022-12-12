# Part #


# Title
## Heading 2
### Heading 3

**bold**
*italic*


Markua help: https://leanpub.com/markua/read 





| Key              | Command                      |
| :--------------- | :--------------------------- |
| Ctrl + B         | Toggle bold                  |
| Ctrl + I         | Toggle italic                |
| Ctrl + Shift + [ | Toggle heading (downlevel)   |
| Ctrl + M         | Toggle math environment      |
| Alt + C          | Check/Uncheck task list item |
| Ctrl + Shift + V | Toggle preview               |

# Lists

1. numbered list
	- bla
3. dumbered list
	- bli
	- blo
4. schu

- bulleted list
	- list second level
- bull shitted list
+++
- [ ] task number 1
- [x] task number 2

## Table


<!-- 
Table: 
1. create with tabs
2. Ctrl+Shift+P: Convert TSV to table
3. Shift+Alt+F: Format all tables

-->

| Header_One | Header_Two |
| :--------- | :--------- |
| Item_One   | Item_Two   |

## Foot- and end-notes

### Footnote

Footnotes are placed somewhere in the text [^footnote-1].

[^footnote-1]: This is the content of the footnote. It will be placed at the end.

Right, you can have multiple references to the same footnote [^footnote-1].

[^^endnote-1]: Here's the end note content.

Then, in the document, you can refer to the [^^endnote-1].


## Cite / Quote

> Schön, sagte der tiefgründige Mauermarder!
> 
> *-- Gluri*




## Code Block


	Starting a line with a tab will display as a block.
	You can use it for code or similar.

An alternative way to define a code block is this:

```
Here is my code.
```

You can also use monospaced font in line like so: `code`.

{caption: "Hello World in Ruby"}
```
Here is my code.
```

## Note
Comments do not print.
<!-- This is a comment -->

This is because markdown understands html.





## Manual Break
End a line with two spaces.  
It will break without indent.  
in iA Writer, you can achieve the same thing with `Shift+Enter`  

For a manual page break, use +++.
+++
Right, this is after the break. Also note that there is no indent after the manual break.

Else, there usually is.

## Image

{width: "100%"}
![Hello World in Ruby](800_agile_caca.png)

## Formulas

This is a formula. 

More info: https://latex-tutorial.com/tutorials/amsmath/
Online editor: https://latex.codecogs.com/eqneditor/editor.php

{id: equation-1} 
```$
x_{3}
```

This is an inline formula `\frac{3}{x_{3}}`$. It formats in line.


## Definition List

Bild
: eine Abbildung
: *fig.* eine Interpretation

Foto
: eine fotografische Abbildung



{#crosslinks-chptr}
## Crosslinks

In Markua, I can tag{#my-tag} a word, or [I can reference]{#my-span} a span.

I can then [reference the tag](#my-tag) or [my span](#my-span) later. 

Or I can reference [Chapter on crosslinks](#crosslinks-chptr).

Or, I can reference an [equation](#equation-1)

### Figures

A figure is any ressource with a title.

For example:

{title: "My code", id: my-code}
```R
x <- "bla"
```

I can then later refer to it like [R code](#my-code).

### Bibliographical Reference

The book [Pwrp - the book]{#pwrp} is really good.

- **Pwrp**{#pwrp}: Pwrp - the best bk!

## Asides

{aside}
This is for long boxes that can break over pages
{/aside}

### Discussion

D> This is a discussion blurb.

E> This is an error blurb.

### Information

I> This is an information blurb.

### Question

Q> This is a question blurb.

### Tip

T> This is a tip blurb.

### Warning

W> This is a warning blurb.

### Exercise

X> This is an exercise blurb.

Leanpub adds an icon attribute to blurbs. Markua does not specify that a blurb must support an icon attribute, or what it would mean if it did. However, Leanpub understands an icon attribute to reference an icon from Font Awesome. The value of this attribute is assumed to be the name of an icon in Font Awesome, without the fa- prefix. So, in Leanpub, you can do this:

{icon: airplane}
B> You can't spell carbon without it!

{icon: leanpub}
B> Yes, we're in Font Awesome!

{icon: github}
B> So is GitHub, of course. Unicorns.


## Horizontal Rule
To separate between two paragraphs, use * * *
* * *
Right, that prints as a line.