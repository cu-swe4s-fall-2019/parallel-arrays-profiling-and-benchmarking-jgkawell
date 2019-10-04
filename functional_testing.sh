# Check code styling for all python files
pycodestyle *.py

# Download and setup ssshtest
test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

rm *.png

run basic_test python plot_gtex.py \
--gene_reads GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz \
--sample_attributes GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt \
--gene ACTA2 \
--group_type SMTS \
--output_file ACTA2.png

assert_no_stderr
assert_exit_code 0

run duplicate_file_test python plot_gtex.py \
--gene_reads GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz \
--sample_attributes GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt \
--gene ACTA2 \
--group_type SMTS \
--output_file ACTA2.png

assert_in_stdout "ERROR"
assert_exit_code 1
