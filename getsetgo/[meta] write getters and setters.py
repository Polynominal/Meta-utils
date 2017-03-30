# What this does is it finds the private/public variables and prompts you to write
# comments or other meaningfull data and then uses it to construct both a setter and getter.
# There are two ways to write the data.
# Setter then getter or Setters and getters individualy.
# Enjoy.
# Written by Mikus Sabanskis. License: MIT.
##Pre-Messages
EXECUTABLE = True
Version = "1.03"
Name = "Get Set Go!"
Changelog = " - Set Get's and Set's to follow a [get get, set set] format as per guidelines of Dr Newton \n"
Changelog = Changelog + "\n - Added user check for adding (final) to the names"
if EXECUTABLE:
    print("Welcome to "+Name+" Version: "+Version)
    print("Changelog:")
    print(Changelog)
    print("Made in 08 March 2017 \n")
    def UserInput(*args, **kwargs):
        return input(arg,kwargs)
else:
    def UserInput(*arg):
        return "PLEASE WRITE YOUR OWN USER INPUT FUNCTION!"
##Options
OVERWRITE = False
##CLASS DEF
CLSig = "class"
Terminator = ";"
Whitespace = " "
whitespace = " "
## COMMENTS
CParam = "@param"
CReturn = "@return"
CWhitespace = " "
CStart = "/**"
CMiddle = "*"
CEnd = "*/"
##Signature
SPublic = "public"
SPrivate = "private"
SVoid = "void"
SNewLine = "\n"
##Syntax
SyReturn = "return"
SyBracketOpen = "("
SyBracketClosed = ")"
SyNewLine = "\n"
##Body
BWhitespace = "\t"
BWhitespaceElement = " "
BEquals = "="
BStart = "{"
BEnd = "}"
BThis = "this."
BNewLine = "\n"

import re
import os
import tkinter as tk
from tkinter import filedialog


PROMPTUSER = True
class Variable:
    def __init__(self,typeName,name):
        self.typeName = typeName
        self.name = name
def askFormated(forWhat):
    if PROMPTUSER:
        additional = ""
        if "?" in forWhat:
            additional = "[Y or N]"
        result = UserInput("[input] "+ forWhat + " " + additional + " \n")
        return result
    else:
        return ""
    
def getCamelCase(x):
    return x[0].upper() + x[1:]
    
def promptUserMaybe(forWhat,defaultstuff):
    result = askFormated(forWhat)
    if result == "":
        return defaultstuff
    else:
        return result 
        
def promptUser(forWhat):
    return promptUserMaybe(forWhat,"")
    
def promptUserBoolean(forWhat):
    result = askFormated(forWhat)
    if len(result) == 0:
        return True
    key = result.lower()[0]
    if key == "n":
        return False
    else:
        return True
def defaultToComment(old,default):
    if old == "":
        return default
    else:
        return old
def writeReturnComment(variable):
    defaultCommentReturn = "returns the variable "+variable.name+" with type "+variable.typeName;
    return CReturn + Whitespace + variable.typeName + Whitespace + variable.name + Whitespace + defaultToComment(promptUser("Type short description for getter of: " + variable.name + " :"),defaultCommentReturn)
    
def writeParamComment(variable):
    defaultCommentParam = "sets the appropriate "+variable.typeName+" to the variable "+variable.name;                                                                                       
    return CParam + Whitespace + variable.typeName + Whitespace + variable.name + Whitespace + defaultToComment(promptUser("Type short description for setter of: " + variable.name + " :"),defaultCommentParam)
    

def newLineComment():
    return "\n" + CMiddle + CWhitespace

def writeMultilineComment(variable,context,getter):
    stream = CStart + newLineComment()
    stream = stream + promptUser("Type short description for" + context + ": \n") + newLineComment()
    if getter:
        stream = stream +  writeReturnComment(variable) + newLineComment()
    else:
        stream = stream +  writeParamComment(variable) + newLineComment()
    stream = stream + "\n"
    stream = stream + CEnd + "\n"
    return stream

def addElement(element):
    return element + whitespace

def writeFnTitle(variable,element):
    return getCamelCase(variable.name) + SyBracketOpen + element + SyBracketClosed + SNewLine

def writeGetter(variable):
    stream = ""
    context = "The getter of " + variable.name
    public = promptUserBoolean(context +" is Public?")
    stream = stream + writeMultilineComment(variable,context,True)
    if public:
        stream = stream + addElement(SPublic) 
    else:
        stream = stream + addElement(SPrivate)
    stream = stream + addElement(variable.typeName) + "get" + writeFnTitle(variable,"")
    stream = stream + BStart + BNewLine
    stream = stream + BWhitespace + SyReturn + BWhitespaceElement + variable.name + Terminator + BNewLine
    stream = stream + BEnd + BNewLine
    return stream
    
def writeSetter(variable):
    stream = ""
    context = "The setter of " + variable.name
    public = promptUserBoolean(context +" is Public?")
    stream = stream + writeMultilineComment(variable,context,False)
    if public:
        stream = stream + addElement(SPublic)
    else:
        stream = stream + addElement(SPrivate)

    newVariableName = promptUserMaybe("The set param name in setter signature: ",variable.name)
    stream = stream + addElement(SVoid) + "set" + writeFnTitle(variable,variable.typeName + whitespace + newVariableName)
    stream = stream + BStart + BNewLine
    stream = stream + BWhitespace 
    if newVariableName == variable.name:
        stream = stream + BThis
    stream = stream + variable.name + BWhitespaceElement + BEquals + BWhitespaceElement + newVariableName + Terminator + BNewLine
    stream = stream + BEnd + BNewLine
    return stream

def WriteFile(buffer,file,variables):
    
    newBuffer = ""
    for variable in variables:
        newBuffer = newBuffer + writeSetter(variable)
    for variable in variables:
        newBuffer = newBuffer + writeGetter(variable)
    finalBuffer = ""
    for line in newBuffer.split("\n"):
        finalBuffer = finalBuffer + BWhitespace + line + "\n"
        
    buffer = buffer + finalBuffer + BEnd
    file.write(buffer)
    file.close()
    pass
def AskForFile():
    root = tk.Tk()
    root.withdraw()
    global OVERWRITE
    OVERWRITE = promptUserBoolean("Y to overwrite file and N to keep both copies"):

    if promptUserBoolean("Y for file N for Directory"):
        ReadFile(filedialog.askopenfilename())
    else:
        ReadFile(filedialog.askdirectory())
    
def ReadFile(whereFrom):
    filename, file_extension = os.path.splitext(whereFrom)
    global PROMPTUSER
    if promptUserBoolean("Ask for user input for file " + os.path.basename(whereFrom) + "?"):
        PROMPTUSER = True
    else:
        PROMPTUSER = False
    
    if os.path.isdir(whereFrom) == True:
        for filename in os.listdir(whereFrom):
            ReadFile(whereFrom + "/" + filename)
        
    inputFile = open(whereFrom,"r")
    
    variables = []
    
    inClass = False
    inClassDef = False
    inClassBody = 0
    fileBuffer = ""
    layer = 0
    for line in inputFile:
        if BStart in line:
            layer = layer + 1
        if BEnd in line:
            layer = layer - 1
            if layer == 0:
                if EXECUTABLE: 
                    print("End of File breaking.")
                break;
                    
        if inClass:
  

            if BStart in line:
                inClassBody = inClassBody +1
                
            if inClassBody == 1:
                words = line.split(" ");
                if len(words) > 0:
                    lastWord = words[len(words)-1].strip()
                    varname = "MISSING!"
                    typename = "MISSING!"
                    buildvariable = False
                    if Terminator in lastWord:
                        varname = lastWord.replace(Terminator,"")
                        varname = varname.replace("\n","")
                        typename = words[len(words) - 2]
                        buildvariable = True
                    if buildvariable:
                        if EXECUTABLE: 
                            print("Found variable: ",varname,typename)
                        variables.append(Variable(typename,varname))
        else:
            if CLSig in line: #We have name now we need to go lower.
                inClass = True

        fileBuffer = fileBuffer + line
        
    for variable in variables:
        print(variable.name,variable.typeName)
    outputFile = None
    if OVERWRITE:
        outputFile = open(filename + file_extension,"w+")
    else:
        outputFile = open(filename + "(final)" + file_extension,"w+")
    
    WriteFile(fileBuffer,outputFile,variables)
    if EXECUTABLE: 
        print("Completed : " + os.path.basename(whereFrom))

#ReadFile("Test.java")
if EXECUTABLE:
    AskForFile()
    print("Written by Mikus Sabanskis. Have a nice day.")
