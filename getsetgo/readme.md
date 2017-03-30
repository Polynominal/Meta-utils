
# Get Set Go!

Get Set Go, is a small utility for writting get/set methods to your existing classes. It is written so it can easily be adapted to the C langauge family
including Java, C++ and other languages.

The script is written with focus on Java, however it can easily be rewritten for other languages due to its abstraction for language specific tools
such as different notations of comments and different ways of defining a function body.
Currently the existing definitions are simply text.


# Usage

## Input

```java
public class Bean
{
    private String taste;
    private int protein;
    public Bean()
    {
        //do something
    }
}
```

## Output

```java
public class Bean
{
    private String taste;
    private int protein;
    public Bean()
    {
        //do something
    }
	/**
	* 
	* @param String taste sets the appropriate String to the variable taste
	* 
	*/
	public void setTaste(String taste)
	{
		this.taste = taste;
	}
	/**
	* 
	* @param int protein sets the appropriate int to the variable protein
	* 
	*/
	public void setProtein(int protein)
	{
		this.protein = protein;
	}
	/**
	* 
	* @return String taste returns the variable taste with type String
	* 
	*/
	public String getTaste()
	{
		return taste;
	}
	/**
	* 
	* @return int protein returns the variable protein with type int
	* 
	*/
	public int getProtein()
	{
		return protein;
	}
}
```

Either download a release or run the python script using python.

There are two modes of usage:
- Directory
- File

Directory task will load a directory of your choosing and will then parse all of the files within that directory using the file task.
File task will load a file of your choosing and only work on that file specificaly and leave other files alone.

It will procede to analyse the script and to update it with get/sets. Please follow the prompts. You can simply press Enter (Return) for the default option.
Generic comments will be written for each of the methods as their default option, these comments will include the type of the variable and some hocus pocus to keep the reader distracted.

## Get

Get is a accessor for a specific variable, the script is designed so that it will fetch all of the written fields in the available
file and then parse them into their respective gets/sets. 

## Set

Set is a mutator for a specific variable, the script will pick all available fields and then parse them, optionaly prompting you to input properties required.
If it finds that the paramter name is the same as the inner variable name it will use it alongside "this" instead.


## Go

To finalize the file the script will add it to the class body and clean up after itself making sure that it complies with the rules of scoping.

## Advanced usage

If you wish to use the script externaly, please set EXECUTABLE to False at the start of the script, this will prevent the script from acting as an executable.

Some basic functions:
##note on semantics

all StartingWithCapital, functions and classes are designed to be used by the end user.
all camelCase functions and classes are designed to be used internaly.
ReadFile - Reads file from the current location and parses it.
AskForFile - Presents the user a file dialog to request file. including prompts.
WriteFile - Writes to file.
Variable - Class for containing a variable, generaly functions as a struct.


## Prompts in code

You may notice that user input is overridden by UserInput function, this is done so that you can interpret the prompts. However state is not translated to that function.
So if you want to answer the prompts you will need to decompose the message using string.
As most of the work in this code is done proceduraly, because after-all it is a script and not an infrastructure, translating the state to the UserInput function is tedious and not worth it.
This will be fixed if I decide to build a macro system for meta stuff.

# TODO
- [ ] Change the string signifiers to lambdas.
- [ ] Add GUI (to merge possibly.)
- [ ] whitespace == Whitespace... it needs to be replaced.
- [ ] Add code diagnosis and error checking pre upload. Allow only specific files to be loaded
- [ ] Add ability to deal with errors correctly, including file format mismatch.
- [ ] Syntax detector. (from parent possibly)
- [ ] Write randomized comments to make it appear more "human" (optional)
- [ ] Read appropriate whitespace from the document rather than from the script.
- [ ] Improve documentation.
- [ ] Make a build system.

>I wrote this script at 2 AM one day after I was tired writing Get's and Set's for literaly every task. Thankfully now I have changed my toxic ways.
