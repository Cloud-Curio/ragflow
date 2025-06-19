variable "compartment_name" {
  description = "Name for the OCI compartment"
  type        = string
  default     = "cloudcurio"
}

variable "db_name" {
  description = "Autonomous Database name"
  type        = string
  default     = "CLOUDCURIODB"
}

variable "admin_password" {
  description = "Admin password for the database"
  type        = string
}
