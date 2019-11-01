
echo "With Hash"
for i in `seq 1 1 10`; do
    rm *.png
    $HOME/miniconda3/envs/swe4s/bin/time -f '%e\t%M' python plot_gtex.py \
        --gene_reads GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz \
        --sample_attributes GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt \
        --gene ACTA2 \
        --group_type SMTS \
        --output_file ACTA2.png \
        --use_hash True
done

echo "Without Hash"
for i in `seq 1 1 10`; do
    rm *.png
    $HOME/miniconda3/envs/swe4s/bin/time -f '%e\t%M' python plot_gtex.py \
        --gene_reads GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz \
        --sample_attributes GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt \
        --gene ACTA2 \
        --group_type SMTS \
        --output_file ACTA2.png \
        --use_hash False
done
