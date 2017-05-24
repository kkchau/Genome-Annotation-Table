GO_slim documentation.

Gene Ontology - Slim Versions - aka GO slims.
---------------------------------------------

For many purposes, in particular reporting the results of GO annotation
of a genome or cDNA collection, it is very useful to have a high level
view of the three GO ontologies.  These have become known as "GO slims".
The first such high level view was made for the Drosophila annotation
(Adams et al. 2000).

It is clear that there would be great advantages in sharing GO slims,
this would make comparisons of summary GO term distributions very
easy.  It is also clear that different groups will need different GO slims,
tailored to their needs.

For this reason GO provides a directory for the archiving of different
GO slims (go/GO_slims/).

It is envisaged that there will be two general classes of GO slim file archived
in this directory.

One or more generic GO slims, usually, but not necessarily, made by the
Consortium.  These will be dynamic files, updated to reflect changes
in the GO files themselves.  They will be versioned, dated and old
versions will be archived.

Archival GO slims deposited by members of the community.  These
will normally, we expect, be the GO slims used in a particular
publication or analysis.  They would be deposited for two reasons.  The first
to give easy access to the GO terms used in a particular publication or
analysis; the second for reuse by others in the community. It is
recognised that these GO slims may come to include concepts obsoleted by
GO.  Authors of these GO slims can, of course, maintain them should they
consider this to be useful.

GO slim files can be deposited by sending them by email to:
cherry@genome.stanford.edu.

File structure.

Header lines:

!GO_slim_name: <name>
!GO_slim_version: <version>
!GO_slim_date: <YYYYMMDD)
!GO_slim_authors: <author_name1,author_name2..>
!GO_slim_contact: <contact_email>
!GO_slim_reference: <reference>

Naming convention:

GO_slim/goslim_generic
.. e.g. for the GO Consortium's current "generic" GO slim.
GO_slim/goslim_Drosophila.0200
.. e.g. for the slim used for the Drosophila annotation.
GO_slim/goslim_Apis_EST.0402
.. e.g. for the slim used for the recent bee EST annotation.

File structure:

GO slim files should be structured in the same syntax as the GO flat files.
A single GO slim file should contain GO concepts from one, two or all three
of the GO ontologies.

Note.
-----

Before reusing an archived GO slim file please check that all of the
terms are current in the most recent versions of the GO ontology
files and that the relationships among terms have not changed.  If
you use, but edit, an archived GO slim please deposit your version
with a !comment note explaining its origin.

=======
Version 0.3 April 27 2000.

Gene Ontology - Slim Versions - aka GO slims.
--------------------------------------------

For many purposes, in particular reporting the results of GO
annotation of a genome or cDNA collection, it is very useful to have a
high level view of the three GO ontologies.  These have become known
as "GO slims".  The first such high level view was made for the
Drosophila annotation (Adams et al. 2000).

It is clear that there would be great advantages in sharing GO slims,
this would make comparisons of summary GO term distributions very
easy.  It is also clear that different groups will need different GO
slims, tailored to their needs.

For this reason GO provides a directory for the archiving of different
GO slims (go/GO_slims/).

It is envisaged that there will be two general classes of GO slim file
archived in this directory.

One or more generic GO slims, usually, but not necessarily, made by
the Consortium.  These will be dynamic files, updated to reflect
changes in the GO files themselves.  They will be versioned, dated and
old versions will be archived.

Archival GO slims deposited by members of the community.  These will
normally, we expect, be the GO slims used in a particular publication
or analysis.  They would be deposited for two reasons.  The first to
give easy access to the GO terms used in a particular publication or
analysis; the second for reuse by others in the community. It is
recognised that these GO slims may come to include concepts obsoleted
by GO.  Authors of these GO slims can, of course, maintain them should
they consider this to be useful.

GO slim files can be deposited by sending them by email to:

  goslim@geneontology.org


Header lines:

!GO_slim_name: <name>
!GO_slim_version: <version>
!GO_slim_date: <YYYYMMDD)
!GO_slim_authors: <author_name1,author_name2..>
!GO_slim_contact: <contact_email>
!GO_slim_reference: <reference>

Naming convention:

GO_slim/goslim_generic
.. e.g. for the GO Consortium's current "generic" GO slim.
GO_slim/goslim_Drosophila.2000
.. e.g. for the slim used for the Drosophila annotation.
GO_slim/goslim_ApisEST.20002
.. e.g. for the slim used for the recent bee EST annotation.

File structure:

GO slim files should be structured in the same syntax as the GO flat
files.  A single GO slim file should contain GO concepts from one, two
or all three of the GO ontologies.

