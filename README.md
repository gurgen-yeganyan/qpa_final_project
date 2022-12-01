# Project bio
bio - cli tool to process genetic code.
### Setup
Requires Docker isntalled locally.
Cloning this repository would be the first step, of course.
In order to deploy the tool on your local machine, run the following statement in a 
terminal from the project root folder:
```
docker-compose up -d --build
```
Then run the following to get into the app:
```
docker-compose run -it bio
```
This will bring you to the bash terminal inside the applicaton.
We must populate the database of our app first.
When inside the interactive shell, just type:
```
 populate
```
#### Test if it works
Type `test` when inside the interactive shell.
(python's default unittest will inform you if everything's OK)
### That's it. We're ready to crunch some genetic code!

### Main functions
`transcribe` - transcribe a DNA sequence into mRNA sequence
`translate` - translate an mRNA sequence into amino acid chain(stop codons are represented by a dot (.) in the output)
`plot` - calculate GC content distribution in a given DNA sequence, with a given window size, this feature creates a .png file representing the plot (you can find the image in the root directory).
### How to use
Simple!
To launch the program:
```
docker-compose run -it bio
```
The app has an alias `bio` in the shell as well.
##### transcription(DNA -> mRNA)
For transcription just write a valid DNA sequence(consisting of only "A", "T", "G" and "C characters") after the command `bio transcribe`:
**your input:**
```
bio transcribe ATGCCG
```
**output:**
```
AUGCCGU
```
##### translation(mRNA -> protein)
Write a valid RNA sequence(consisting of only "A", "U", "G" and "C characters") after the command `bio translate`:
**your input:**
```
bio translate GCUAACUAACAUCUUUGGCACUGUU
```
**output:**
```
AN.HLWHC
```
##### GC ratio plotting
Input a valid DNA sequence and a number reperesenting the plotting window after the command
`bio plot`
**your input:**
```
bio plot ATTTGGCTACTAACAATCTA 3
```
**Output** will be saved as  a PNG file inside the root directory(*/app*)

#### Reading from files
##### Important!
**If you wish to process files in the program, you  must add them to the
*project/data* directory before the setup phase.**

> There are some sample files included in the project

All previously described functions work the same way, you just need to add  the `file` command  first and indicate your file name at the end:
**your input:**
```
bio file transcribe sample_dna.txt
```
**output:**
```
ACUACGUAGCUAGCUAGCUGCUGAUCGAUGCUGAUCGUAGCUAGUGAUCGAUCGUAGCUGAU
```
___________________________________________________________________
**your input:**
```
bio file translate sample_rna.txt
```
**output:**
```
TDRTYVRTYVAS.LRTYVRTY
```
__________________________________________________________________
**your input:**
```
bio file plot sample_dna.txt 5
```

### When you're done
1. Type ```exit``` to quit from bash.
2. Run the following from your initial terminal to switch Docker containers off:
```
docker-compose down
```
