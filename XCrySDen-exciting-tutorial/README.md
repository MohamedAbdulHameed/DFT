# How to use XCrySDen to visualize exciting input files

`exciting` is a DFT code that is based on the LAPW method and only available on Linux.

Read [F. Finocchi's excellent lecture notes](http://www.attaccalite.com/wp-content/uploads/2017/04/pdf_DFT4beginners.pdf) on DFT if you are into functional calculus, or read G.J. Lee's [Computational Materials Science: An Introduction](https://www.routledge.com/Computational-Materials-Science-An-Introduction-Second-Edition/Lee/p/book/9781498749732) if you want a gentle, though comprehensive, introduction.

Download `exciting nitrogen 14` [here](http://exciting-code.org/nitrogen-14).

Follow the installation instructions found [here](http://exciting-code.org/nitrogen-download-and-compile-exciting).

Follow [these instructions](http://exciting-code.org/nitrogen-tutorial-scripts-and-environment-variables) to add `exciting` to your [`PATH` environment variables](https://en.wikipedia.org/wiki/Environment_variable).

`exciting` uses Python 2.7, and runs on Linux which uses Python 3.x as the official version, while using Python 2.7 for some tasks. While Linux knows which version should be assigned some task, third-party programs, e.g., `exciting` don't, and this often leads to errors like `SyntaxError` and `ImportError`. A common `ImportError` is faced with the `lxml` package which can be installed for Python 3 but not for Python 2.

In my experience, the best solution is to define a [`conda` Python 2 environment](https://docs.anaconda.com/anaconda/user-guide/tasks/switch-environment/), do all your `exciting` calculations there, and then deactivate it when you are done. In principle, this can also be done using [Python virtual environments](https://docs.python.org/3/tutorial/venv.html), but this is far more complex and I don't recommend it.

It is assumed that you already have Anaconda installed on your machine. Here is how to [download](https://www.anaconda.com/products/individual) and [install](https://docs.anaconda.com/anaconda/install/) Anaconda if you don't have it.

Enough prerequisites, and now to the main topic of this tutorial: Using [XCrySDen](http://www.xcrysden.org/XCrySDen.html) to visualize `exciting` input files.

[Steps found in the documentation](http://exciting-code.org/xcrysdenexcitingsetup) won't work for you because they are incomptable with the current (and any future) version of XCrySDen, so follow the steps in this tutorial instead. The dollar sign, `$`, only clarifies things you should write in the terminal. Don't paste it.

* Install XCrySDen:
```
$ sudo apt install xcrysden
```
* Go to your home directory:
```
$ cd
```
* Create the hidden folder `.xcrysden` and move inside it:
```
$ mkdir .xcrysden
```
In Linux, the dot before a folder or file's name indicates that it is hidden.
* Use your preferred text editor to create and open the file `custom-definitions`:
```
$ xed .xcrysden/custom-definitions
```
I used `xed`, but `nano` or `gedit` or any text editor would do.
* Paste the following lines of code into `custom-definitions`:
```
addOption --exciting  $env(EXCITINGTOOLS)/ex2xsf {
  load structure from exciting input.xml format
}
```
`EXCITINGTOOLS` is one of the `PATH` environment variables you defined, and `ex2xsf` is a program that transforms `XML` files to `XSF` files readable by XCrySDen.
* You are now ready to visualize your input. Just go to the folder where your input is and type the following in the terminal:
```
$ xcrysden --exciting input.xml &
```
Congratulations.
