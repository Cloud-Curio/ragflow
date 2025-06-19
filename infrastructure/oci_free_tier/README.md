# Oracle Cloud Free Tier Database with Terraform

This folder contains an example Terraform configuration to provision an Autonomous Database on Oracle Cloud Infrastructure (OCI) using the free tier.

The configuration creates:

- An OCI compartment
- An Autonomous Database instance
- Networking resources required to access the database

## Prerequisites

- [Terraform](https://www.terraform.io/downloads) 1.5+
- An OCI account with free tier resources available
- API credentials configured locally (`~/.oci/config`)

## Usage

1. Update the variables in `variables.tf` to match your OCI tenancy and desired database name.
2. Run `terraform init` to download the OCI provider.
3. Execute `terraform apply` to create the resources.
4. After provisioning, the database connection details will be output.

Remember that the free tier allows limited resources. Adjust the shape and storage values accordingly to stay within the free quota.
