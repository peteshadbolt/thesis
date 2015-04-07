\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{shadbolt-thesis}[2013/04/06 v0.1 Pete Shadbolt]
\LoadClass[12pt, twoside, a4paper]{book}

% Some definitions
%TODO: get rid of this, useless
\def\degreeyear#1{\gdef\@degreeyear{#1}}
\def\degreemonth#1{\gdef\@degreemonth{#1}}
\def\degree#1{\gdef\@degree{#1}}
\def\advisor#1{\gdef\@advisor{#1}}
\def\department#1{\gdef\@department{#1}}
\def\field#1{\gdef\@field{#1}}
\def\university#1{\gdef\@university{#1}}
\def\universitycity#1{\gdef\@universitycity{#1}}
\def\universitystate#1{\gdef\@universitystate{#1}}

% Required packages
\RequirePackage{mathrsfs}
\RequirePackage{tabularx}
\RequirePackage{graphicx}
\RequirePackage{hyperref}
\RequirePackage{fancyhdr}
\RequirePackage{enumitem}
\RequirePackage{complexity}
\RequirePackage{xcolor}
\RequirePackage{xspace}
\RequirePackage{tikz} 
\RequirePackage{quotchap} 
\RequirePackage{setspace} 
\RequirePackage{titling}
\RequirePackage[centertags]{amsmath}
\RequirePackage{amssymb}
\RequirePackage[numbers, comma, sort&compress]{natbib}
\RequirePackage[md, sc]{titlesec}
\RequirePackage{verbatim}
\RequirePackage{color}
\RequirePackage{url}
\RequirePackage[titles]{tocloft}
\RequirePackage{pdfsync} 
\RequirePackage{listings}
\RequirePackage[]{siunitx}
\RequirePackage{chapterbib}
\RequirePackage[xindy, nonumberlist]{glossaries}
%\renewcommand{\glsdisplayfirst}[4]{\textit{#1 #4}}


% Setup hyperlinks
\definecolor{dark-red}{rgb}{0.0, 0, 0.3}
\definecolor{dark-blue}{rgb}{0.15,0.15,0.4}
\definecolor{medium-blue}{rgb}{0,0,0.5}
\definecolor{rr}{rgb}{0.7,0.1,0.1}
\definecolor{gg}{rgb}{0.5,0.5,0.5}
\hypersetup{
    colorlinks, linkcolor={black},
    citecolor={black}, urlcolor={medium-blue}
}

% Drawing
\usetikzlibrary{arrows,matrix,positioning}

% Table of contents, labelling
\setcounter{tocdepth}{3}
\renewcommand{\cftchapfont}{\normalsize \scshape}
\renewcommand{\refname}{}
\renewcommand\listfigurename{Listing of figures}
\renewcommand{\cfttoctitlefont}{\hfill\Huge\bfseries}
\renewcommand{\cftaftertoctitle}{\hfill}
\renewcommand{\cftloftitlefont}{\hfill\Huge\bfseries}
\renewcommand{\cftafterloftitle}{\hfill}
\renewcommand{\cftlottitlefont}{\hfill\Huge\bfseries}
\renewcommand{\cftafterlottitle}{\hfill}
\AtBeginDocument{%
  \renewcommand\listtablename{Tables}
  \renewcommand\listfigurename{Figures}
  \renewcommand\contentsname{Table of Contents}
}

% Leaders for chapter entries
\renewcommand\cftchapdotsep{\cftdotsep}
% Add space to account for new chapter numbering schema
\renewcommand\cftchapnumwidth{3em}
\renewcommand\cftsecindent{3em}
% Redefine representation for chapter (and section) counters
\renewcommand\thechapter{\arabic{chapter}}
\renewcommand\thesection{\arabic{chapter}.\arabic{section}}

% Chapter spacing
\titlespacing*{\chapter}{0pt}{130pt}{40pt}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% The front page
%TODO: get rid of this, its a bad way to do it
\renewcommand{\maketitle}{ 
	\thispagestyle{empty}
	\vspace*{\fill} 
    \begin{center}
    \includegraphics[width=150pt]{frontmatter/bristol.pdf}
    \vspace{70pt} 

	\Huge 
    \onehalfspacing
    \textit{\thetitle}\\
    \normalsize 
    \singlespacing
    \vspace{42pt}

	{\Large \sc \theauthor}\\ 
	\vspace{6pt}
    Department of Physics
	\vspace{32pt}


    A thesis submitted to the University of Bristol in accordance with the requirements for the degree of Doctor of Philosophy in the Faculty~of~Science, Department~of~Physics\\
    \vspace{22pt}
    February 2014
	\end{center} \vspace*{\fill}
}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Fonts
%\RequirePackage[bitstream-charter]{mathdesign}
\RequirePackage[T1]{fontenc}

% Geometry
\RequirePackage[a4paper,inner=3.5cm,outer=2.5cm,top=2.5cm,bottom=3cm,pdftex]{geometry}
% \RequirePackage[text={6in,8.3in},centering]{geometry} % This looks better on screen

% Wider line spacing
\renewcommand{\baselinestretch}{1.3}
