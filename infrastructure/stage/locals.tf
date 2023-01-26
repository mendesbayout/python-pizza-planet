locals {
  stage = "dev"

  dev = {
    bucket_name = "my-dev-terraform-state-bucket"
    frontend_bucket_name = "my-dev-frontend-bucket"
    db_username = "dev_admin"
    db_password = "mydevpassword"
    db_name = "devdb"
    vpc_id = "vpc-xxxxxxx"
    subnet_ids = ["subnet-xxxxxxx", "subnet-yyyyyyy"]
  }

  prod = {
    bucket_name = "my-prod-terraform-state-bucket"
    frontend_bucket_name = "my-prod-frontend-bucket"
    db_username = "prod_admin"
    db_password = "myprodpassword"
    db_name = "proddb"
    vpc_id = "vpc-zzzzzzz"
    subnet_ids = ["subnet-zzzzzzz", "subnet-wwwwwww"]
  }
}