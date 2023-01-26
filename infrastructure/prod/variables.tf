variable "region" {
  default = "us-east-1"
}

variable "image_tag" {
  default = "latest"
}

variable "db_username" {
  default = "admin"
}

variable "db_password" {
  default = "mysecretpassword"
}

variable "db_name" {
  default = "prod_clients_db"
}

variable "db_instance_type" {
  default = "db.t2.micro"
}

variable "ec2_instance_type" {
  default = "t2.micro"
}