# Genome Annotation Table
### Final project for CSE 182 (Biological Data Analysis)
A simple genome annotation table built with Python3 and Django. All data was provided by collaborating teams (classmates) and organized into an easy-to-use data table.


## Instructions
* To load data: Go to ANNOTATIONS; update to_read.txt for list of files to read; python3 load\_data.py --clear

* Null fields (no hit) must have marker "NULL" or "null" (case-sensitive)

* Raw alignment files must be organized into their own folders for each tool; filename must be \<tool>/<protein\_id>.txt. E.g. BLAST/ABO10513.txt

* Keywords must have descriptive annotations, not just things like family name

* Annotations must have header in form 

| Sequence | BLAST | Pfam | Prosite | ALL\_OTHER\_ANNOTATIONS | Comments |
| -------- | ----- | ---- | ------- | ----------------------- | -------- |
| ABO10513 | blast_hit | pfam_hit | null | null | generic_comment |
