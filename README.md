# You thought it was over? Part II

> Using github without command line for pull requests is fine (but discouraged), though, creating unnecessarily many commits will be awarded -ve marks.

  I mean, surely you didn't. Of course there are more steps to getting your marks than mere human approval. Of course there are.
    
  Let's start with commiting your solutions to this repository.
  
  First, [fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) the repository, and clone it. Then follow the instructions given below to make changes
  ## What changes will you make to the repo?

  The real reason for this whole charade is to build a book out of your assignments for future use. Remember your MatGeo Book that is Oh-So-Crucial for the quizzes in your course? Unfortunately, it didn't appear out of thin air. It too was made by piecing together assignments from unexpecting students who, like you, probably thought they were done when they submitted them.

  ### Your To-Do List:

>1. Add your Tex files, to the specific section folder
You'll find that there exist folders with all the chapter names and section names. Navigate to the folder and create a folder for your section for your question set (Ex: 15-30), and add your tex file

>2. If there are multiple sections in your typing assignment, seperate them into multiple tex files.
For example if your main tex file contains `\section{}` more than once, make another tex file with a relevant name and move the section content into it. Place each tex file in it's respective section/question_set folder
  
>3. Comment out the lines with `\begin{enumerate}` and `\end{enumerate}`, but leave the `\item`s. This is to ensure consistent numbering in the assignments. If for any reason, you didn't use enumerate, make sure you add `\item` before each question. Also remove `\begin{document}` and `\end{document}`

>4. Make sure to move the `\section{}` command to the preamble between `\iffalse` and `\fi` 

>5. Make sure that `\section{}`, `\author{}` are present in the preamble and nowhere else in the file. These are used to tell latexgen who's submission it is, and also what section to put it in, in the book 
  
Example code:

Suppose your main LaTeX file looks something like this:

  ```latex
    %\iffalse
    \documentclass[journal]{IEEEtran}
    \usepackage[a5paper, margin=10mm]{geometry}
    \setlength{\headheight}{1cm} 
    \setlength{\headsep}{0mm}  
    \usepackage{gvv-book}
    \usepackage{gvv}
    .
    .
    .
    %Whatever preamble you have between %\iffalse and %\fi (or %\endif)
    . 
    . 
    \makeindex

    \begin{document}
    \bibliographystyle{IEEEtran}
    \onecolumn

    \title{Assignment}
    \author{Student Name}
    \maketitle
    \bigskip

    \renewcommand{\thefigure}{\theenumi}
    \renewcommand{\thetable}{\theenumi}
    %\fi

    \section{Fill in the Blanks}
      \begin{enumerate}
        \item Question 1 and Options

        \item Question 2 and Options
      \end{enumerate}
    \section{Section 2}
      \begin{enumerate}
        \item Question 1 and Options

        \item Question 2 and Options

    \end{enumerate}

    \section{Section 3}
      \begin{enumerate}
        \item Question 1 and Options

        \item Question 2 and Options

        \item Question 3 and Options

        \item Question 4 and Options
      \end{enumerate}
    \end{document}
   ```
  You are supposed to make 3 files, ideally in different folders, with only the tex file and any figs, codes and tables folders you might have.

After changes, the tex files may look like this

In `fitb/1-2` Folder,
  ```latex
  \iffalse
    \title{Assignment}
    \author{Student Name}
    \section{fitb}
  \fi

  % \section{Fill in the Blanks}
    % \begin{enumerate}
      \item Question 1 and Options

      \item Question 2 and Options
    % \end{enumerate}
  % \end{document}
  ```
  In `mcq-single/1-2` folder
  ```latex

  \iffalse
    \title{Assignment}
    \author{Student Name}
    \section{mcq-single}
  \fi
  % \section{Section 2}
  %   \begin{enumerate}
      \item Question 1 and Options

      \item Question 2 and Options

  % \end{enumerate}
  ```
  In `matrix-match/1-4` folder
  ```latex
   \iffalse
      \title{Assignment}
      \author{Student Name}
      \section{matrix-match}
    \fi
  % \section{Section 3}
  %   \begin{enumerate}
      \item Question 1 and Options

      \item Question 2 and Options

      \item Question 3 and Options

      \item Question 4 and Options
    % \end{enumerate}
  ```

After doing this, you have to run 
```bash
  python3 latexgen.py
```

### Errors you may get while running the python script 

  > Skipped processing file JEE/Circle/Section 1/1-15/main.tex Reason: Did not match conditions given in key "pdf.conditions.validlatex" in json file pdfc.json

This means that you have not included the `\iffalse` and `\fi` flags in your tex files.

  > Exception: Fatal Error: JEE/Circle/Section 2/30-45/main.tex has no \section macro

As you can see, this error means that you forgot to include the `\section{}` macro in your tex file.

  > Exception: Fatal Error: JEE/Circle/Section 2/30-45/main.tex does not contain desciptor command \\author

Also self explanatory, but this means that you forgot to include the `\author{}` macro in your tex files.

  > Exception: Fatal Error: JEE/Circle/Section 2/30-45/main.tex possible values for \section are: dict_keys(['true-false', 'matrix-match', 'mcq-single', 'mcq-multiple', 'fitb', 'ar', 'paragraph, 'subjective', 'mains', 'integer'])

There are specific section names you can use. The list includes
  
  1. true-false : For True Or False Type 
    
  2. matrix-match : For Match The Following
    
  3. mcq-single : Single correct Answers
   
  4. mcq-multiple : Multiple correct Answers

  5. fitb : Fill In The Blanks

  6. integer : Integer Type Questions

  7. subjective : Subjective type

  8. paragraph : Comprehension Based

  9. mains : Section-B Mains/AIEEE

  10. ar : Assertion and Reason Type 


Then run
```sh
  pdflatex main.tex
  pdflatex main.tex
```
Yes - Twice

To generate a PDF file. Check if the formatting of all your questions is correct, and then Open a pull request


  For details about how to make and manage "Pull Requests", follow this [Link](https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-a-project)

