# Biopython problem set

## Install Biopython on your machine


```
% mamba create --name bio
% mamba activate bio
(bio)% mamba install --channel conda-forge --channel bioconda biopython 
```
> **If** you are on your own computer and not using one of the course machines you will have to download mamba
> 
> [mamba-installation](https://mamba.readthedocs.io/en/latest/installation/mamba-installation.html)
> 

## FASTA Parser

1. Create a new FASTA parser that uses BioPython to get the sequence name, description, and sequence.
2. Add in some code to print out stats about your FASTA records in your mult-FASTA file:
   -  total number of sequences
   -  total number of nucleotides
   -  average length of sequences
   -  shortest sequence length
   -  longest sequence length
   -  average GC content
   -  highest GC content
   -  lowest GC content
  ```
  sequence count: ? 
  total number of nucleotides: ? 
  avg len: ? 
  shortest len: ? 
  longest len: ? 
  avg GC content: ? 
  lowest GC content: ? 
  highest GC content: ?

  ```
  
3. Test your code with a small test set of 2 or 3 very short sequences.
4. Run your code on [Python_08.fasta](../files/Python_08.fasta)

## Parsing BLAST output
### Preparation for problem

Preparation:

1.  Download uniprot_sprot using the Unix command 'wget':

```
curl -OL ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_sprot.fasta.gz
```
**Make sure to not add this to your gitHub Repository. It is tooooo big and with cause problems**

2. Unzip the file using the Unix command 'gunzip':

```
gunzip uniprot_sprot.fasta.gz
```
This will create a file `uniprot_sprot.fasta`

**Do not add uniprot_sprot.fasta to your github repo. It is too big.*** To be safe, find your .gitignore in the root of your github repository. Add `uniprot_sprot.fasta*` anywhere in the file. Make sure to add this file to our index as you are updating your repo.

Here is a way to ENSURE that you don't mistakenly commit a large file. Get help from TA if you do not know where your .git directory is. You might have already completed this on day 1 in teh Unix exercises.
```
cd .git/hooks/
curl -OL https://raw.githubusercontent.com/prog4biol/pfb2024/master/setup/pre-commit
```


3. What does the uniprot_sprot.fasta file contain? How many records? Does it look intact? How do you know?

Extract IDs from fasta file

1. with the `Bio.SeqIO` module, generate a list of all the IDs in the fasta file. How many are there?

2. Make a list of all the descriptions. The description field almost always has a field OS=... that includes a species or strain designation. Here's an example

```
sp|A9N862|AAEB_SALPB p-hydroxybenzoic acid efflux pump subunit AaeB OS=Salmonella paratyphi B (strain ATCC BAA-1250 / SPB7) GN=aaeB PE=3 SV=1
```

Here the genus is _Salmonella_ and the species is _paratyphi_. There is also a strain 'B (strain ATCC BAA-1250 / SPB7). You can ignore this part. Using regular expressions, extract just the genus and species and count the number of sequences present for that genus/species combination. List comprehensions make this kind of data processing quick to code, but you might want to start by going step by step in a for loop.

3. Make a new fasta file of all the sequences containing the species 'Salmonella paratyphi B'. Include the 'B' for this part of the exercise. Call this protein file s_paratyphi.prot.fa. You'll want to loop through all the sequence records, extract the description, find matches to 'Salmonella paratyphi B' and convert to fasta.

__Running BLAST Locally__
These questions will take some research and set up. Spend some time reading about how to run blast and ask for help as needed.
1. Blast a protein such as [purH](https://raw.githubusercontent.com/prog4biol/pfb2024/master/files/purH.aa.fa) against the S. paratyphi B proteins. You can do this remotely or locally with a blast binary or with biopython.
2. Print the E-value and the score and the length of the alignment and the % similiarity (not % identity)


__Install NCBI Blast+__
1. Install NCBI Blast using conda fomr bioconda
```
conda install -c bioconda blast
```
2. Now in a NEW terminal window, you will have the blast executables available. (blastn, blastx, tblastn, tblastx, blastp, makeblastdb, blastdbcmd)

__Run BLAST+__
1. First format you FASTA file so that BLAST+ can use it as a database
  `makeblastdb -in [FASTAFILE] -dbtype [nucl or prot] -parse_seqids`
      - `-in` is the switch for the FASTA formated sequence file that you want to use as your BLAST db
      - `-dbtype` needs to be `prot` or `nucl`. This has to correspond to the sequence type in your FASTA file
      - `parse_seqids` makes it possible for you to retrieve individual sequences by name using `blastdbcmd`
2. Run `blastp -help` for information about running the command and formatting output.
3. Run `blastp -query [Your Query FASTA File] -db [BLAST FORMATED DB FASTA FILE] -out [output file name] -evalue [evalue cutoff] -outfmt [5 for XML; 6 for TAB; etc]`
      - `-query`  A FASTA formated sequence file with one or more query sequences
      - `-db` The file name of the FASTA formated file you formated with `makeblastdb`
      - `-out` A name of your choice for your output file, otherwise, the output is printed to the screen
      - `-evalue` The Expectation value (E) threshold for returning hits. 1e-5 is a common cutoff (Bill will say 1e-2, but we will be a tad more conservative)
      - `-outfmt` Choose the output format of your BLAST report as XML(5) `-outfmt 5` .  TAB(6) is also common output but unparsable by BioPython.  
      
__Parse BLAST Output__

1. Use BioPython to parse your XML BLAST results. Print out all the hit sequence ID that are better than 1e-5 as well as their descriptions in tab separated columns.
  
