#!/usr/bin/env bash

# Download analysis data of entire ENA E. coli collection
wget https://cgps.ams3.digitaloceanspaces.com/sb27/e_coli_amrwatch_records.tar.gz

# Extract data
tar -zxvf e_coli_amrwatch_records.tar.gz

# Extract cgmlst results
gunzip Escherichia\ coli__cgmlst.csv.gz 
