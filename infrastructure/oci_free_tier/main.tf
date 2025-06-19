terraform {
  required_version = ">= 1.5"
  required_providers {
    oci = {
      source  = "oracle/oci"
      version = ">= 5.0.0"
    }
  }
}

provider "oci" {}

resource "oci_identity_compartment" "cloudcurio" {
  name          = var.compartment_name
  description   = "Compartment for CloudCurio resources"
  enable_delete = false
}

resource "oci_database_autonomous_database" "cloudcurio_db" {
  compartment_id = oci_identity_compartment.cloudcurio.id
  db_name        = var.db_name
  admin_password = var.admin_password
  cpu_core_count = 1
  data_storage_size_in_tbs = 1
  db_workload = "OLTP"
  is_free_tier = true
}

output "db_connection_string" {
  value = oci_database_autonomous_database.cloudcurio_db.connection_strings[0]."cdb-default"
}
