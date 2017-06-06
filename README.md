# CSE 182 Final Project
### Goals
- [x] Create a web server to store and display genome annotations
- [x] Be able to read in standard-format annotations automatically
- [x] Convert data load to use pandas (req headers)
- [x] Allow user to search for annotations
- [x] Allow user to download information
- [x] Implement statitistics for hits at bottom of table
- [ ] Parse and standardize annotations --> Waiting on project 1
- [x] Allow user to click row and go to raw annotation in separate page

---

* To load data: Go to ANNOTATIONS; update to_read.txt for list of files to read; python3 load\_data.py --clear

* Null fields (no hit) must have marker "NULL" or "null" (case-sensitive)

* Raw alignment files must be organized into their own folders for each tool; filename must be <protein\_id>_anything.txt. E.g. BLAST/ABO10513.txt

* Keywords must have descriptive annotations, not just things like family name

* Annotations must have header in form 

| Sequence | BLAST | Pfam | Prosite | ALL\_OTHER\_ANNOTATIONS | Comments |
| -------- | ----- | ---- | ------- | ----------------------- | -------- |
| ABO10513 | blast_hit | pfam_hit | null | null | generic_comment |
