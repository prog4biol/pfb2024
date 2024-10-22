Python 6 - Sets and IO - Problem Set
===================

1. Make a set using the two different syntaxes for creating a set `myset = set()` and `myset2 = {}`.  

```python
mySet = set('ATGTGGG')
mySet2 = {'ATGTGGG'}
```
-  What is the difference?
-  Does it matter which method you use?
-  How many items are in mySet and mySet2?



2. Write a script that creates 2 sets using the collections of numbers below. Find the intersection, difference, union, and symetrical difference between these two sets.  
    - 3, 14, 15, 9, 26, 5, 35, 9
    - 60, 22, 14, 0, 9  


3. Create a set using the function `set()` and a DNA sequence, what will you get back? Try it with this sequence:

```
GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTNNGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCGTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACX
```

4.  **Nucleotide Composition**. Write a script that:

  - determines the unique characters in this sequence

  ```
GAACTCCAAAAATGAAAACATAGTAGCAATCAAAGCATCCCACTATTTTTTGTCTCTCGTTTCATTAGCGTTGTAAATTACTGATACCCTACTATACCTCTACAAGGCCTTTGTCATCTTTTTACTCAAGTGTGAAATCATCACTTATTGTATGAAGGATGAGCTTTCCGTTCGCTAGTTTGCTGAAAAGGCCTTCTGCAATAAGCTCTCTATTATCTTTAAAAAAACCTGGTTCCTGGTCTTCCATTCTGCTAAAAGCTGTAGGGGTTTTATCACGAGATTCCCGTTGGCATTCTGACTTATTAAAAATGCTTACAGAAGAAATGGATTCTTTAAATGGTCAAATTAATACGTGGACAGATAATAATCCTTTATTAGATGAAATTACGAAGCCATACAGAAAATCTTCAACTCGTTTTTTTCATCCGCTTCTTGTACTTCTAATGTCTAGAGCATCAGTAAATGGGGATCCACCGAGTCAGCAACTATTTCAAAGGTACAAACAACTTGCCCGTGTAACAGAATTGATTCATGCTGCCAATATAATTCATATTAATATTGGAGAAGAACAAAGCAACGAACAGATTAAACTTGCAACGTTGGTTGGAGATTATTTACTCGGAAAGGCGTCTGTTGATTTAGCACATTTAGAAAACAACGCTATTACAGAAATTATGGCTTCTGTTATTGCAAACTTAGTTGAAGGGCACTTCGGAAGCCGACAAAATGGCTCTGTTGGTTTGTCAAACGAACGAACCATCCTTCTGCAATCAGCCTTTATGCCAGCAAAGGCATGTTTATGCGCAAGCATATTGAATAACTCATCACAATACATTAATGATGCGTGTTTCAATTATGGAAAATTTCTAGGCTTATCGCTGCAACTGGCCCATAAGCCTGTATCTCCTGACGCCCAAGTTTTGCAAAAGAATAATGACATTTTGAAAACATATGTTGAGAATGCCAAGAGCTCATTGTCTGTTTTCCCCGATATAGAGGCTAAGCAAGCTCTCATGGAAATCGCTAATAGTGTTTCGAAGTAATCGACAGGTATTGTATCCTGGATTAATATTAGGGTGGCTCATGCATGCTCGTGCAATCGTAACAAATATGTCTTTCTTTTACGAATTTTAACGCTTCAATATAAATCATATTTTTCCTCA
  ```

  - iterate over each unique character and count the number found in the sequence
  - store each count in a dictionary. example: `nt_comp['A']=2`
  - when you are done counting nucleotides, report the number of each unique nucleotide
  - also when you are done counting, calculate and report the GC content (G_count + C_count / total_nucleotides ).


5. Write a script to do the following to [Python_06.txt](https://raw.githubusercontent.com/prog4biol/pfb2024/master/files/Python_06.txt)
   - Open and read the contents.  
   - Uppercase each line
   - Print each line to the STDOUT


6. Modify the script in the previous problem to write the contents to a new file called "Python_06_uc.txt"



7. Open and print the reverse complement of each sequence in [Python_06.seq.txt](https://raw.githubusercontent.com/prog4biol/pfb2024/master/files/Python_06.seq.txt). Each line is the following format:    `seqName\tsequence\n.` Make sure to print the output in FASTA format including the sequence name and a note in the description that this is the reverse complement. Print to STDOUT and capture the output into a file with a command line redirect '>'. 
   - **Remember is is always a good idea to start with a test set for which you know the correct output.**

8. FASTQ File Parsing:
___ 
FASTQ File Overview based on wikipedia [wikipedia/FASTQ](https://en.wikipedia.org/wiki/FASTQ_format):
___  

A FASTQ file has 4 lines per sequence record:  
  1. Begins with a '@' character and is followed by a sequence identifier and an optional description (like a FASTA title line).
  2. The raw sequence letters
  3. Begins with a '+' character and is optionally followed by the same sequence identifier (and any description) again.
  4. The quality values for each sequence character. This line is required to contain the same number of symbols as letters in the sequence.  
  
A FASTQ file containing a single sequence will have a format like this:
```text
@SEQ_ID  
GATTTGGGGTTCAAAGCAGTATCGATCAAATAGTAAATCCATTTGTTCAACTCACAGTTT  
+  
!''*((((***+))%%%++)(%%%%).1***-+*''))**55CCF>>>>>>CCCCCCC65  
```

The quality scores are denoded with ASCII characters. The byte representing quality runs from 0x21 (lowest quality; '!' in ASCII) to 0x7e (highest quality; '~' in ASCII). 

Here are the quality value characters in left-to-right increasing order of quality (ASCII):  
!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~

___  

For this problem open the [FASTQ](https://en.wikipedia.org/wiki/FASTQ_format) file [Python_06.fastq](https://raw.githubusercontent.com/prog4biol/pfb2024/master/files/Python_06.fastq) and read each line to calculate and report:  
    - total number of lines  
    - total number of sequence IDs  
    - total number of characters  
    - total number of nucleotides  
    - average line length of all the lines  
    - average line length of the lines that contain sequences.     


10. Write your first FASTA parser script. This is a script that reads in a FASTA file ([Python_06.fasta](../files/Python_06.fasta)) and stores each FASTA record separately for easy access for future analysis.

Things to keep in mind:
   - open your file
   - read each line
   - is your line a header line? is it a sequence line?
   - does a single FASTA record have one line of sequence or multiple lines of sequence?

   HINTS: use file I/O, if statements and dictionaries to write your first FASTA parser. Some other useful functions and methods are find, split, string concatenation.

   At the end, your script should return the following:

   fastaDict = {
      'seq1' : 'AAGAGCAGCTCGCGCTAATGTGATAGATGGCGGTAAAGTAAATGTCCTATGGGCCACCAATTATGGTGTATGAGTGAATCTCTGGTCCGAGATTCACTGAGTAACTGCTGTACACAGTAGTAACACGTGGAGATCCCATAAGCTTCACGTGTGGTCCAATAAAACACTCCGTTGGTCAAC' ,
      'seq2' : 'GCCACAGAGCCTAGGACCCCAACCTAACCTAACCTAACCTAACCTACAGTTTGATCTTAACCATGAGGCTGAGAAGCGATGTCCTGACCGGCCTGTCCTAACCGCCCTGACCTAACCGGCTTGACCTAACCGCCCTGACCTAACCAGGCTAACCTAACCAAACCGTGAAAAAAGGAATCT' ,
      'seq3' : 'ATGAAAGTTACATAAAGACTATTCGATGCATAAATAGTTCAGTTTTGAAAACTTACATTTTGTTAAAGTCAGGTACTTGTGTATAATATCAACTAAAT' ,
      'seq4' : 'ATGCTAACCAAAGTTTCAGTTCGGACGTGTCGATGAGCGACGCTCAAAAAGGAAACAACATGCCAAATAGAAACGATCAATTCGGCGATGGAAATCAGAACAACGATCAGTTTGGAAATCAAAATAGAAATAACGGGAACGATCAGTTTAATAACATGATGCAGAATAAAGGGAATAATCAATTTAATCCAGGTAATCAGAACAGAGGT' }




10. Goal of this problem: generate a couple of gene list that are saved in files, add their contents to sets, and compare them. 

__Generate Gene Lists:__


_Get all genes:_

1. Go to [Ensembl Biomart](http://useast.ensembl.org/biomart/martview).
2. In dropdown box, select "Ensembl Genes 113"  (or most current version)
3. In dropdown box, select "Ferret Genes" 
4. On the left, click Attributes
5. Expand GENE:
6. Deselect "transcript stable ID", "Gene stable ID version", and "transcript stable ID version".
7. Click Results (top left)
8. Export all results to "File" "TSV" --> GO
9. Rename the file to "ferret_all_genes.tsv"

_In the same Ensembl window, follow the steps below to get genes that have been labeled with Gene Ontology term "stem cell proliferation". For extra information on stem cell proliferation, check out  [stem cell proliferation](http://purl.obolibrary.org/obo/GO_0072089)_

11. Click "Filters"
12. Under "Gene Ontology", check "Go term name" and enter "stem cell proliferation" (clear out any previous GO term names)
13. Click Results (top left)
14. Export all results to "File" "TSV" --> GO
15. Rename the file to "ferret_stemcellproliferation_genes.tsv"

_In the same Ensembl window, follow the steps below to get genes that have been labeled with Gene Ontology term "pigmentation". For extra information on pigmentation, check out [pigmentation](http://purl.obolibrary.org/obo/GO_0043473)_. Make sure that the previous Stem Cell Proliferation GO term is replaced with the Pigmintation GO term


16. Click "Filters"
17. Under "Gene Ontology", check "Go term name" and enter "pigmentation"
18. Click Results (top left)
19. Export all results to "File" "TSV" --> GO
10. Rename the file to "ferret_pigmentation_genes.tsv"


__Open each of the three files and add the geneIDs (Gene stable ID) to a Set. One Set per file.__

A. Find all the genes that are not cell proliferation genes.  
B. Find all genes that are both stem cell proliferation genes and pigment genes.  
*Note* Make sure to NOT add the header to your set.  

__Now, let do it again with transciption factors.__

1. Go back to your Ensembl Biomart window
2. Deselect the "GO Term Name"
3. Select "GO Term Accession"
4. Enter these two accessions IDs which in most organisms will be all the transcription factors
   - GO:0006355 is "regulation of transcription, DNA-dependent”. 
   - GO:0003677 is "DNA binding"
5.  Click Results (top left)
6. Export all results to "File" "TSV" --> GO
7. Rename the file to "ferret_transcriptionFactors.tsv"

__Open these two files: 1) the transcription factor gene list file and 2) the cell proliferation gene list file. Add each to a Set, One Set per file__

A. Find all the genes that are transcription factors for cell proliferation


__Now do the same on the command line with `comm` command. You might need to `sort` each file first.__

Are you still committing your files as you go?

## Extra: Expand on the nucleotide composition exercise 
  - get the raw file [Python_06.seq.txt](https://raw.githubusercontent.com/prog4biol/pfb2024/master/files/Python_06.seq.txt)
  - in a script, open this file
  - iterate over each line in this file (seqName\tsequence\n)
     - for each sequence:
         - calculate and store the count of each unique nucleotide character in a dictionary
         - report the name, total of each nucleotide count, and the GC content 

