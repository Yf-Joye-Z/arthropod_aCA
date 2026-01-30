# arthropod_αCA

This repository contains the data and scripts required to reproduce the results in [Evolutionary history of Alpha Carbonic Anhydrase (αCA) gene family across the phylum Arthropoda](Insert%20link%20here)

Each folder contains data required to recreate the results in each section of the manuscript.

For questions, please contact [yz937\@duke.edu](mailto:yz937@duke.edu) or [carollee\@wisc.edu](mailto:carollee@wisc.edu)

---
## Details

### `Arthropod_Chordate_aCA/` 
contains amino acid and nucleotide sequences for all arthropod and chordate αCA used in this study. 
- **XXX_aCA_aa.fasta** -- amino acid sequences
- **XXX_aCA_cds.fasta** -- nucleotide sequences

### `Arthropod_phylogeny/` 
contains documents required to recreate the arthropod phylogeny generated in this study
- **unedited_arthropod_aCA.fasta** -- unedited amino acid sequences of arthropod and poriferan αCA used for the phylogeny and alignment-free clustering method. 
- **unlabeled_arthropod_aCA_phylogeny.contree** -- arthropod αCA phylogeny that is not labeled
- **labeled_arthropod_aCA_phylogeny.tbi** -- arthropod αCA phylogeny that is labeled.

### `Arthropod_alignment_free_clustering/` 
contains labels, summary, and the final result from the alignment-free αCA clustering performed in this study. For the alignment-free clustering method, please see [Yeung et al., 2023](https://academic.oup.com/bib/article/24/1/bbac619/6987820?login=true) and its [GitHub repository](https://github.com/esbgkannan/chumby).
* for `arthropod/` and `copepod/`
  - **aCA_labels_Phylogeny.csv** -- the labels required for the coloring of the final UMAP file
  - **aCA_colors_phylogeny.json** -- json file that includes the color specification for the final UMAP file.
  - **statistics_summary.csv** -- summary statistics (spearman rank correlation and trustworthiness) generated for each distance metric and representation method used to create the final visualization. 
  - **mean_of_residue_tokens_ts_ss.eps** -- final UMAP file in eps (embedding vector is derived from mean of residue token and distance is calculated via ts-ss).
  - **mean_of_residue_tokens_ts_ss.html** -- final UMAP file in html (embedding vector is derived from mean of residue token and distance is calculated via ts-ss).

### `Gene_tree-species_tree_reconciliation/` 
contains documents required to recreate the gene tree-species tree reconciliation of arthropod and chordate αCA through [GeneRax](https://github.com/BenoitMorel/GeneRax/wiki)
- **alignment.txt** -- edited amino acid sequences of arthropod, chordate, and poriferan αCA. 
- **family.txt** -- a neccessary family file that specifies the starting_gene_tree, alignment, and mapping files.
- **gene_tree.treefile** -- arthropod+chordate gene tree used for reconciliation.
- **mapping.txt** -- a neccessary text file that shows the relationship between species and their gene names. It specifies how [GeneRax](https://github.com/BenoitMorel/GeneRax/wiki) should map each αCA sequence to species. 
- **species_tree.txt** -- arthropod+chordate species tree used for reconciliation.
- **result_aca_reconciliated.xml** -- Output after running GeneRax. the gene reconcilied species tree
- **result_geneTree.newick** -- Output after running GeneRax. the species reconcilied gene tree

### `dN-dS_Evolution_Rate/` 
contains documents required to recreate the rate of evolution(dN/dS) analysis for 1) arthropod, 2) chordates, and 3) arthropod vs. chordates  
- `Arthropod_dN-dS/`
    * for `Clade II/`, `Clade III/`, and `Clade I/`
      + **cst-edited_aCA.fasta** -- edited arthropod CARP αCA nucleotide alignment used for dN/dS analysis. Only codons where its corresponding aminoacid has 50% homology across sequences within each arthropod clades were kept.
      + **phylogeny.contree** -- arthropod CARP αCA phylogeny used for dN/dS analysis. 
      + **dn-ds.json** -- unparsed, raw dN/dS value for all branches and nodes. 
      + **final_omega.xlsx** -- parsed dN/dS values for branches and nodes for arthropod CARP αCA nucleotide

- `Chordate_dN-dS/`
    * for `Clade II/`, `Clade III/`, and `Clade I/`
      + **cst-edited_aCA.fasta** -- edited chordate CARP αCA nucleotide alignment used for dN/dS analysis. Only codons where its corresponding aminoacid has 50% homology across sequences within each chordate clades were kept.
      + **phylogeny.contree** -- chordate CARP αCA phylogeny used for dN/dS analysis. 
      + **dn-ds.json** -- unparsed, raw dN/dS value for all branches and nodes. 
      + **final_omega.xlsx** -- parsed dN/dS values for branches and nodes for chordate CARP αCA nucleotide
     
- `Arthropod_vs_Chordate_dN-dS/`
    * for `Clade II/`, `Clade III/`, and `Clade I/`
   * The **XXX** below is meant to be substituted by either arthropod or chordate.
      + **XXX_cst-edited_aCA.fasta** -- edited CARP αCA nucleotide alignment used for dN/dS analysis. Only codons where its corresponding aminoacid has 50% homology across sequences within both arthropod and chordate clades  were kept.
      + **XXX_phylogeny.contree** -- CARP αCA phylogeny used for dN/dS analysis. 
      + **XXX_dn-ds.json** -- unparsed, raw dN/dS value for all branches and nodes. 
      + **XXX_final_omega.xlsx** -- parsed dN/dS values for branches and nodes for CARP αCA nucleotide

- **cst_alignment_homology_getter.py** -- a python script that returns the column number of an input alignment where the homology of that column is above an user-inputed threshold. For example, if the cut-off of interest is 50, this script returns all columns where more than 50% of the sequences show the same amino acid/nucleotide. This script is intended to generate the *Auxillary file* for amino acid alignment, which is required when using the *cst* editing mode in [ClipKit](https://jlsteenwyk.com/ClipKIT/). 
- **cst_aa-to-cds.py** -- a python script that changes the output of *cst_alignment_homology_getter.py* into column numbers of its corresponding nucleotide codons. Through this script, the user will be able to use the *cst* editing mode in [ClipKit](https://jlsteenwyk.com/ClipKIT/) to find the codons, where its corresponding amino acid has a homology above a user-defined threshold across sequence of interest. This script is used to created the **cst-edited_aCA.fasta** above. 
- **ds_limit_enforcer.py** -- a python script that takes a raw dN/dS json file generated through HyPhy (such as **dn-ds.json** from above) and remove branches and nodes where its 1) dS > 3, 2) dS < 0.0001, and 3) dN/dS > 3. 
- **dn-ds_getter.py** -- a python script that takes a dN/dS json file (generated through HyPhy) and parse it into a human-friendly excel file, where only the node/branch name and its corresponding dN/dS value are retained. This script is intended to be used on the output of **ds_limit_enforcer.py**, which generates the **final_omega.xlsx** seen above. 

### `Signature_of_selection_analysis/` 
contains files required to recreate the aBSREL, MEME, and BUSTED analysis done in this study
- `Clade I/`
   * `aBSREL/`
     + **cst-edited_aCA_with-phylogeny.txt** -- edited arthropod CARP αCA alignment with newick-formatted phylogeny.  
     + **all-branches_foreground.json** -- generated aBSREL results when all branches/nodes were tested. 
     + **Eurytemora_foreground.json** -- generated aBSREL results when only Eurytemora branches/nodes were tested
- `Clade II/`
   * `aBSREL/`
     + **cst-edited_aCA_with-phylogeny.txt** -- edited arthropod Cytosolic αCA alignment with newick-formatted phylogeny.  
     + **all-branches_foreground.json** -- generated aBSREL results when all branches/nodes were tested. 
     + **Eurytemora_foreground.json** -- generated aBSREL results when only Eurytemora branches/nodes were tested
- `Clade III`
   * `aBSREL/`
     + **cst-edited_aCA_with-phylogeny.txt** -- edited arthropod E&Mb αCA alignment with newick-formatted phylogeny.  
     + **all-branches_foreground.json** -- generated aBSREL results when all branches/nodes were tested. 
     + **Eurytemora_foreground.json** -- generated aBSREL results when only Eurytemora branches/nodes were tested
   * `MEME/`
     + **cst-edited_aCA_with-phylogeny.txt** -- edited arthropod E&Mb αCA alignment with newick-formatted phylogeny.  
     + **all_branches_MEME.json** -- generated MEME results when all branches/nodes were tested. 
     + **Eurytemora_MEME.json** -- generated MEME results when only Eurytemora branches/nodes were tested  
   * `BUSTED/`
     + **cst-edited_aCA_with-phylogeny.txt** -- edited arthropod E&Mb αCA alignment with newick-formatted phylogeny.
     + **aCA12_foreground.json** -- generated BUSTED results when the 3 aCA12 paralogs of *Eurytemora affinis* species complex were selected as foreground.

### `Protein_Model/`
contains the folded models generated by alphafold3
- **E.carolleeae_aCA12.fasta** -- amino acid sequence of E.carolleeae_aCA12 protein
- **E.carolleeae_aCA12.pse** -- pymol object of the folded E.carolleeae_aCA12 protein 
- **Residue-highlight_aCA12.pse** -- pymol object of the folded E.carolleeae_aCA12 protein, where the residue under signatures of selection were mapped  
---
<p align="center">

<img src="https://github.com/Yf-Joye-Z/arthropod_aCA/blob/main/Homepage.png" width="800" height="540"/>

</p>

