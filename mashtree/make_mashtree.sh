#!/usr/bin/env bash

# Run mashtree with all assemblies
mashtree --numcpus 12 ../fasta/qc/*.fasta > sb27.nwk

# Remove '_scaffolds' to match ids in metadata
sed -i -e 's/_scaffolds//g' sb27.nwk

