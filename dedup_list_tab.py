# Filters tab delimited text file that is sorted by taxid and then contig N50
# run with: python dedup_list_tab.py metazoa_plus_taxonomy.txt

import sys

metazoa_filename = sys.argv[1]

taxid = "Hi"
annotation = False
annotation_in_initial = False
orig_line = ""
with open(metazoa_filename) as infile:
    with open("metazoa_filtered.txt", "w") as outfile:
        for count, line in enumerate(infile):
            if count == 0:
                outfile.write(line)
            else:
                line_list = line.split("\t")
                new_taxid = line_list[0]
                if new_taxid == taxid:
                    if not annotation:
                        if line_list[8] == "GENOME_GFF":
                            annotation = True
                            annotation_name = line_list[12]
                else:
                    if annotation_in_initial:
                        outfile.write(orig_line)
                    elif annotation:
                        orig_line_list = orig_line.split("\t")
                        to_write = "\t".join(orig_line_list[:8] + ["other: " + annotation_name] + orig_line_list[9:])
                        outfile.write(to_write)
                    else:
                        outfile.write(orig_line)
                    annotation = False
                    annotation_in_initial = False
                    orig_line = line
                    taxid = line.split("\t")[0]
                    if line.split("\t")[8] == "GENOME_GFF":
                        annotation = True
                        annotation_in_initial = True
        if annotation_in_initial:
            outfile.write(orig_line)
        elif annotation:
            orig_line_list = orig_line.split("\t")
            to_write = "\t".join(orig_line_list[:8] + ["other: " + annotation_name] + orig_line_list[9:])
            outfile.write(to_write)
        else:
            outfile.write(orig_line)

