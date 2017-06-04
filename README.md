# CSE 182 Final Project
### Goals
- [x] Create a web server to store and display genome annotations
- [x] Be able to read in standard-format annotations automatically
- [x] Convert data load to use pandas (req headers)
- [x] Allow user to search for annotations
- [ ] Allow user to download information --> Waiting on project 1
- [x] Implement statitistics for hits at bottom of table --> Waiting on project 1
- [ ] Parse and standardize annotations --> Waiting on project 1
- [x] Allow user to click row and go to raw annotation in separate page
- [ ] (?) Process given FASTA file for alignments and annotations


--> File serving: https://djangosnippets.org/snippets/365/

---

To load data:
    Go to ANNOTATIONS
    python3 load_data.py --clear

Raw alignments must be in ANNOTATIONS/raw\_aligns; filenames must be form of <sequence>.txt (what shows up in the 'Sequence' field

Annotations must have header in form 

| Sequence | BLAST | Pfam | Prosite | ALL\_OTHER\_ANNOTATIONS | Comments |
