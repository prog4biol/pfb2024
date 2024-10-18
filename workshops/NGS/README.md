NGS File Formats Workshop Excercises
=======================

The purpose of this workshop is to gain experience working with the various file formats discussed in the [NGS file formats lecture](bio_info_formats.pdf) and the tools designed to manipulate them. We will use real *E. coli* data to find candidate frameshift mutants in a strain of interest.

1. First, create a new `ngs` directory for this workshop in which to perform these exercises, then change directory into it.

2. Install the following command line software using Minimamba:
    ```bash
    # add channels to download tools from:
    $ mamba config append channels conda-forge
    $ mamba config append channels bioconda

    # create an environment and activate it
    $ mamba create --name ngs
    $ mamba activate ngs

    # Install tools for analysis
    $ mamba install wget gnuplot
    $ mamba install -c bioconda bwa fastqc samtools bcftools bedtools 
    ```

3. Download the Java-based GATK sofware required for this tutorial using `wget`:
    ```bash
    # 1. Fetch each software package .zip archive file:
    $ wget https://github.com/broadinstitute/gatk/releases/download/4.6.0.0/gatk-4.6.0.0.zip

    # 2. Unpack the .zip archive:
    $ unzip gatk-4.6.0.0.zip
    ```

4. Download the following genome files with `wget`:
    ```bash
    # Genome sequence:
    $ wget https://raw.githubusercontent.com/prog4biol/pfb2024/master/workshops/NGS/data/Ecoli.fasta.gz
    $ wget https://raw.githubusercontent.com/prog4biol/pfb2024/master/workshops/NGS/data/Ecoli.fasta.gz.md5

    # Genome annotation:
    $ wget https://raw.githubusercontent.com/prog4biol/pfb2024/master/workshops/NGS/data/Ecoli.gff3.gz
    $ wget https://raw.githubusercontent.com/prog4biol/pfb2024/master/workshops/NGS/data/Ecoli.gff3.gz.md5

    $ md5sum Ecoli.fasta.gz Ecoli.gff3.gz
    ```
    - Check that your download completed successfully by running `md5sum` on each file and checking that the outputted MD5 checksum string match the ones provided above. If they are not identical, it means your file is truncated and needs to be downloaded again.


5. Decompress both files with `gunzip`, then index the genome FASTA to make it quickly searchable by BWA, GATK, and other tools.
    ```bash
    $ gunzip Ecoli.fasta.gz
    $ samtools faidx Ecoli.fasta
    $ samtools dict Ecoli.fasta >Ecoli.dict
    $ bwa index Ecoli.fasta
    ```
    - Use the _E. coli_ FASTA file to determine how many of the sequences are chromosomes? How many plasmids?
    - Use the _E. coli_ FASTA file to determine the genome size?


6. Use `wget` to download the FASTQ file of sequencing reads for our strain of interest, check the completeness of your download (as you did above), then use Unix commands to examine the FASTQ file:
    ```bash
    # Whole-genome sequnecing reads:
    $ wget https://raw.githubusercontent.com/prog4biol/pfb2024/master/workshops/NGS/data/SRR21901339.fastq.gz
    $ wget https://raw.githubusercontent.com/prog4biol/pfb2024/master/workshops/NGS/data/SRR21901339.fastq.gz.md5

    $ SRR21901339.fastq.gz

    $ gunzip SRR21901339.fastq.gz
    ```
    - How long are the reads? (*HINT*: you can use `head`, `tail`, and `wc`)
    - Are these reads single-end or paired-end? Explain how can you tell. 
    - Which Phred quality encoding (ASCII offset) are the reads in and how can you tell?


7. Run FastQC on the FASTQ file and examine the report:
    ```bash
    # Run FastQC to generate a sequence quality metrics report:
    $ fastqc --extract SRR21901339.fastq

    # Open a file from the macOS Unix command line by:
    $ open SRR21901339_fastqq.html
    ```
    - How many read pairs are included in the FASTQ file?
    - For which metrics are there Warnings? For which are there Failures?
    - Do these reads have good per-base sequencing quality?
    - Are there any nucleotide biases along the reads?
    - Is there a biased GC content?
    - Is there an abundance of Ns (failed base calls) along the reads?
    - What percentage of reads are duplicates?
    - Are there any over-represented sequences? If so, which?


8. Write a python script to trim poor-quality bases from the ends of the FASTQ sequences and output a new FASTQ file and output the trimmed reads to a file named `SRR21901339.trim.fastq`. Your script should take as input from the command line: one FASTQ file name and one integer value (the minimum base quality threshold). ***HINT*: Use the following approach**:
    1. Iterate from the 3'-end of the read to the 5'-end, examining the quality values at each base position (see the [lecture notes](bio_info_formats.pdf) for how to convert quality string characters to numeric values;  
    2. `break` at the first base with a quality value greater-than or equal-to your inputted quality threshold;  
    3. then use string slicing to extract the high-quality portion of both the sequence and quality strings.  


9. Align the trimmed reads to the genome sequence using BWA-MEM (*i.e.* the `bwa` command). Make sure to specify a Read Group string (via `-R`) that, *at a minimum*, includes `ID`, `SM`, and `PL` tags. This Read Group information is required by GATK. Then, convert the output file to BAM format, sort the BAM file, and then index it (Execute `bwa mem` or `samtools` without any arguments to see all available options for each):
    ```bash
    # Use BWA's MEM algorithm to align reads to the genome as paired-ends,
    # and piping the SAM output directly to samtools to convert to BAM:
    $ bwa mem -Mp -t4 -R '@RG\tID:SRR21901339\tSM:Ecoli\tPL:ILLUMINA' Ecoli.fasta SRR21901339.trim.fastq | samtools view -1 - >SRR21901339.bam

    # Sort the alignments by genomic coordinates:
    $ samtools sort -m 1g -o SRR21901339.srt.bam SRR21901339.bam

    # Index the sorted alignments:
    $ samtools index SRR21901339.srt.bam
    ```


10. Run `samtools stats` and `plot-bamstats` on the BAM file and examine the `.html` report.
    ```bash
    $ samtools stats --ref-seq Ecoli.fasta SRR21901339.srt.bam >SRR21901339.stats
    $ plot-bamstats -s Ecoli.fasta >Ecoli.gc
    $ plot-bamstats -r Ecoli.gc -p SRR21901339 SRR21901339.stats

    # Finally, open the output HTML file in your web Safari browser:
    $ open SRR21901339.html
    ```
    - What fraction of reads were mapped to the genome?
    - What is the mode insert size of the sequencing library? Is insert size reasonably Normally-distributed?
    - Are the majority of reads pairs mapped in Inward (forward-revers, FR), Outward (reverse-forward, RF), or other orientation?
    - Below which base-quality value does the majority of mismatches occur? **Record this value to use for Problem 12.**
       >*NOTE*: The reads were generated from a strain different from the reference strain and signal from biological SNP differences will also be reflected in the plot.


11. Use `samtools view` to filter your BAM file to keep alignments with `PAIRED` and `PROPER_PAIR` flags, AND *DO NOT* contain `UNMAP`, `MUNMAP`, `SECONDARY`, `QCFAIL`, `DUP`, or `SUPPLEMENTARY` flags; write the output to a new BAM file and index it. What fraction of the reads are properly paired?
    ```bash
    # Get the SAM flags for properly-paired reads, do:
    $ samtools flags PAIRED,PROPER_PAIR
    0x3	     3	   PAIRED,PROPER_PAIR

    # Get the SAM flags value to exclude poor quality data:
    $ samtools flags UNMAP,MUNMAP,SECONDARY,QCFAIL,DUP,SUPPLEMENTARY
    0xf0c	3852	UNMAP,MUNMAP,SECONDARY,QCFAIL,DUP,SUPPLEMENTARY

    # Then filter reads with `samtools view` to output to a new BAM
    # file, selecting _for_ reads that are properly-paired and
    # _removing_ the poor-quality reads:
    $ samtools view -b -f3 -F3852 SRR21901339.srt.bam >SRR21901339.srt.proper.bam

    # Now, index the new BAM file:
    $ samtools index SRR21901339.srt.proper.bam
    ```
    > *NOTE*: Execute `samtools flags` without arguments for help with bit flags.


12. Run the GATK HaplotypeCaller to call variants using the final filtered BAM file, set `--min-base-quality-score` to the value you determined in *Problem 10*. **NOTE**: Run GATK in the backgound (i.e., `nohup gatk HaplotypeCaller ... &`) or open a second terminal window and work on Problems 13 and 14 while GATK is running.
    ```bash
    ./gatk-4.6.0.0/gatk HaplotypeCaller \
         --minimum-mapping-quality 30 \
         --min-base-quality-score ${YOUR_MINIMUM_BASE_QUALITY_SCORE} \
         --read-validation-stringency SILENT \
         --sample-ploidy 1 \
         --reference Ecoli.fasta \
         --input SRR21901339.srt.proper.bam \
         --output SRR21901339.vcf
    ```
    > *NOTE*: Execute `./gatk-4.6.0.0/gatk HaplotypeCaller --help` for more options.


13. Use the `samtools depth` command to calculate the per-site read depths across the genome and output to a file. The output file will contain three columns:
    1. Chromosome name,
    2. Position (1-based), and
    3. Depth of coverage.
    
    For example:
    ```
    chrI	1	15
    chrI	2	15
    chrI	3	14
    chrI	4	16
    chrI	5	16
    ```
    > *NOTE*: Execute `samtools depth` without arguments for more options.
    

15. Write a python script that computes the genome-wide [mean](https://en.wikipedia.org/wiki/Arithmetic_mean) and [standard deviation](https://en.wikipedia.org/wiki/Standard_deviation) parameters for read depth.


16. Using command-line tools, extract CDS features present in `Ecoli.gff3` and create a new GFF3 file. Then use `bedtools intersect` to determine how many SNPs and InDels in the VCF file intersect these CDS features.
    > *NOTE*: Execute `bedtools intersect --help` for more options.


17. Compress your new VCF of variants in CDS regions with `bgzip`, then index it with `bcftools index --tbi your.vcf.gz`.


18. Find frame-shift mutations:
    1. Calculate variant consequence using the `bcftools csq` tool (inputting `Ecoli.gff3` and *NOT* the CDS-specific GFF3) and output to a new VCF file.
        > *NOTE*: Execute `samtools csq` without arguments for more options.
    2. Write a python script to parse variant consequence annotations from the INFO BCSQ tag and calculate the [Z-score](https://en.wikipedia.org/wiki/Standard_score) from the Sample DP field in this new VCF; output this information to a tab-delimited file summarizing the framehift variants. Use the genome-wide mean and standard deviation calculated in Problem 14 as input parameters to your script to calculate the depth Z-score at each locus.
        - How many variants induce frameshifts?
        - How many frameshifts cause stop codons to be lost? How many gained?
        - How many of these frameshift variants have read depth Z-scores between -2 and +2?
        - Why might we be skeptical of variants with very low or very high read depths?
