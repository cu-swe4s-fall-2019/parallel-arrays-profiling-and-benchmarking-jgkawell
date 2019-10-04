import sys
import gzip
import data_viz
import argparse


parser = argparse.ArgumentParser(
    description='Plot a gene data visualization from a file.')
parser.add_argument(
    '--gene_reads',
    type=str,
    help='The file name of the gene data')
parser.add_argument(
    '--sample_attributes',
    type=str,
    help='The file name of the gene sample attributes data')
parser.add_argument(
    '--gene',
    type=str,
    help='The gene to plot the data for')
parser.add_argument(
    '--group_type',
    type=str,
    help='Either tissue groups (SMTS), or tissue types (SMTSD)')
parser.add_argument(
    '--output_file',
    type=str,
    help='The file name for the plot')
parser.add_argument(
    '--search_type',
    type=str,
    default='b',
    help='The search type (b=binary, l=linear)')


def linear_search(key, array):

    for i in range(len(array)):
        curr = array[i]
        if key == curr:
            return i
    return -1


def binary_search(key, array):

    lo = -1
    hi = len(array)
    while (hi - lo > 1):
        mid = (hi + lo) // 2

        if key == array[mid][0]:
            return array[mid][1]

        if (key < array[mid][0]):
            hi = mid
        else:
            lo = mid

    return -1


def get_sample_info(sample_file, group_col_name):
    sample_id_col_name = 'SAMPID'
    samples = []
    sample_info_header = None
    for l in open(sample_file):
        if sample_info_header is None:
            sample_info_header = l.rstrip().split('\t')
        else:
            samples.append(l.rstrip().split('\t'))

    group_col_idx = sample_info_header.index(group_col_name)
    sample_id_col_idx = sample_info_header.index(sample_id_col_name)

    groups = []
    members = []

    for row_idx in range(len(samples)):
        sample = samples[row_idx]
        sample_name = sample[sample_id_col_idx]
        curr_group = sample[group_col_idx]

        try:
            curr_group_idx = groups.index(curr_group)
        except ValueError:
            curr_group_idx = len(groups)
            groups.append(curr_group)
            members.append([])

        members[curr_group_idx].append(sample_name)

    return groups, members


def get_group_counts(data_file_name, gene_name, groups, members, search_type):
    version = None
    dim = None
    data_header = None
    gene_name_col = 1
    group_counts = [[] for i in range(len(groups))]

    for l in gzip.open(data_file_name, 'rt'):
        if version is None:
            version = l
            continue

        if dim is None:
            dim = [int(x) for x in l.rstrip().split()]
            continue

        if data_header is None:
            data_header = []
            i = 0
            for field in l.rstrip().split('\t'):
                data_header.append([field, i])
                i += 1
            data_header.sort(key=lambda tup: tup[0])

            continue

        A = l.rstrip().split('\t')

        if A[gene_name_col] == gene_name:
            for group_idx in range(len(groups)):
                for member in members[group_idx]:
                    if search_type == 'b':
                        member_idx = binary_search(member, data_header)
                    elif search_type == 'l':
                        member_idx = linear_search(member, data_header)
                    else:
                        print(f"ERROR: Invalid search type ({search_type})")
                        sys.exit(1)
                    if member_idx != -1:
                        group_counts[group_idx].append(int(A[member_idx]))
            break

    return group_counts


def main():

    # Parse args and read in data from the files
    args = parser.parse_args()

    # Get the data from the sample file
    groups, members = get_sample_info(
        args.sample_attributes, args.group_type)

    # Get the data from the gene read file
    group_counts = get_group_counts(
        args.gene_reads, args.gene, groups, members, args.search_type)

    # Plot the data
    try:
        data_viz.boxplot(group_counts, args.output_file, args.gene,
                         args.group_type, "Gene read counts", groups,
                         (10, 3), 300)
    except FileExistsError:
        print(f"ERROR: That file already exists ({args.output_file})."
              + "Try another name or delete it and run again.")
        sys.exit(1)


if __name__ == '__main__':
    main()
