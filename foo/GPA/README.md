Abaixo, consta o conteúdo do arquivo "README.md" do software GPA de Sautter, obtido em 2017 do repositório https://github.com/rsautter/GPA, cujos códigos desta versão específica do software, utilizados nesta dissertação, constam neste diretório.

---------------------------------------------------------------------------------

# Concentric Gradient Pattern Analysis
This is a Concentric Gradient Pattern Analysis (CGPA) prototype developed in Cython + Python

#### Notes
In this version:
    Ga = (A/T)*(2-D)

Where:
 - A = number of asymmetric vectors
 - T = number of vectors
 - D = vectorial divesity = sum(v/sum(v))

### Requirements
 - Python 2.7 or greater
 - Matplotlib
 - Cython
 - Numpy

### Compilation

This code uses the Cython library, to improve the perfomence. 
Go to the gpa Folder and type:

    python compile.py build_ext --inplace

### Execution

If you want to analyse a single image, and/or if you want to display it:

    python main.py filename tol rad_tol ptol

If you want to compute multiple images:

    python main.py -l filelist tol rad_tol ptol output

The parameter tol is the vectorial modulus and phase tolerance (float), and posTol is the position tolerance (integer)

### Execution Examples
#### Single file

    python main.py test/m4.txt 0.02 0.01 1

Must output the image:

![mapExampleIt19](/gpa/Figures/exampleOutput_m4.png)

#### Multiple files

    python main.py -l configexample.txt 0.03 0.01 1 gas.csv


Must outputs in file gas.csv:

\# | Ga	| Diversity |	Total | Asymmetric
------- | ------- | ------- | ------- | -------
test/m2.txt |	0.215842843056	| 0.12310577184	| 400 | 46
test/m3.txt | 0.203546822071 | 0.149574398994 | 400 | 44
test/m4.txt | 1.18959379196 | 0.0498461723328 | 400 | 244


## References
https://en.wikipedia.org/wiki/Gradient_pattern_analysis

http://cython.org/
