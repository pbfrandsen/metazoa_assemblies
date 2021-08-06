# Metazoa Assemblies

This repository houses the scripts for the manuscript, "Towards a genome sequence for every animal: where are we now?"

*dedup_list_tab.py* takes as input genome assembly metadata harvested from NCBI through the [NCBI datasets tool](https://www.ncbi.nlm.nih.gov/datasets/) in the form of a csv. The CSV must be sorted first by taxid and second by contig N50. Then it will choose the assembly for each taxon with the longest contig N50. The script will also discover whether an annotation exists for that species on NCBI (for any assembly).

*scrape_assembly_info.py* is a web scraper based on [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) that will scrape metadata that is not included in the standard NCBI datasets metadata. All it needs is an accession number.