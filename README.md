# arthropod_αCA

This repository contains the data and scripts required to reproduce the results in [Evolutionary history of Alpha Carbonic Anhydrase (αCA) gene family across the phylum Arthropoda](Insert%20link%20here)

Each folder contains data required to recreate the results in each section of the manuscript.

For questions, please contact [yz937\@duke.edu](mailto:yz937@duke.edu){.email} or [carollee\@wisc.edu](mailto:carollee@wisc.edu){.email}

---
## Details

#### `Arthropod_Chordate_aCA/` 
contains amino acid and nucleotide sequences for all arthropod and chordate αCA used in this study. 
- **XXX_aCA_aa.fasta** -- amino acid sequences
- **XXX_aCA_cds.fasta** -- nucleotide sequences

#### `Arthropod_phylogeny/` 
contains documents required to recreate the arthropod phylogeny generated in this study
- **unedited_arthropod_aCA.fasta** -- unedited amino acid sequences of arthropod and poriferan αCA used for the phylogeny and alignment-free clustering method. For the alignment-free clustering method, please see [Yeung et al., 2023](https://academic.oup.com/bib/article/24/1/bbac619/6987820?login=true) and its [GitHub repository](https://github.com/esbgkannan/chumby).
- **unlabeled_arthropod_aCA_phylogeny.contree** -- arthropod αCA phylogeny that is not labeled
- **labeled_arthropod_aCA_phylogeny.tbi** -- arthropod αCA phylogeny that is labeled.

#### `dN-dS_Evolution_Rate/` 
contains documents required to recreate the rate of evolution(dN/dS) analysis for 1) arthropod, 2) chordates, and 3) arthropod vs. chordates  
- `Arthropod_dN-dS/`
    * for `Cytosolic/`, `E&Mb/`, and `CARP/`
      + **cst-edited_aCA.fasta** -- edited arthropod CARP αCA nucleotide alignment used for dN/dS analysis. Only codons where its corresponding aminoacid has 50% homology across sequences within each arthropod clades were kept.
      + **phylogeny.contree** -- arthropod CARP αCA phylogeny used for dN/dS analysis. 
      + **dn-ds.json** -- unparsed, raw dN/dS value for all branches and nodes. 
      + **final_omega.xlsx** -- parsed dN/dS values for branches and nodes for arthropod CARP αCA nucleotide

- `Chordate_dN-dS/`
   * for `Cytosolic/`, `E&Mb/`, and `CARP/`
      + **cst-edited_aCA.fasta** -- edited chordate CARP αCA nucleotide alignment used for dN/dS analysis. Only codons where its corresponding aminoacid has 50% homology across sequences within each chordate clades were kept.
      + **phylogeny.contree** -- chordate CARP αCA phylogeny used for dN/dS analysis. 
      + **dn-ds.json** -- unparsed, raw dN/dS value for all branches and nodes. 
      + **final_omega.xlsx** -- parsed dN/dS values for branches and nodes for chordate CARP αCA nucleotide
     
- `Arthropod_vs_Chordate_dN-dS/`
   * for `Cytosolic/`, `E&Mb/`, and `CARP/`
   * The **XXX** below is meant to be substituted by either arthropod or chordate.
      + **XXX_cst-edited_aCA.fasta** -- edited CARP αCA nucleotide alignment used for dN/dS analysis. Only codons where its corresponding aminoacid has 50% homology across sequences within both arthropod and chordate clades  were kept.
      + **XXX_phylogeny.contree** -- CARP αCA phylogeny used for dN/dS analysis. 
      + **XXX_dn-ds.json** -- unparsed, raw dN/dS value for all branches and nodes. 
      + **XXX_final_omega.xlsx** -- parsed dN/dS values for branches and nodes for CARP αCA nucleotide

- **cst_alignment_homology_getter.py** -- a python script that returns the column number of an input alignment where the homology of that column is above an user-inputed threshold. For example, if the cut-off of interest is 50, this script returns all columns where more than 50% of the sequences show the same amino acid/nucleotide. This script is intended to generate the **Auxillary file** required to use the cst editing mode in [ClipKit](https://jlsteenwyk.com/ClipKIT/). 
- **cst_aa-to-cds.py** -- a python script that returns 
- ****
- ****



#### `selection_pressure_analysis/` 
- contains
  
---

::: {align="center"}
<p align="center">

<img src="https://github.com/Yf-Joye-Z/arthropod_aCA/blob/main/Homepage.png" width="800" height="540"/>

</p>
:::
