terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.9.0"
    }
  }
  backend "s3" {
    bucket  = "prod-tfstate-pizza"
    key     = "terraform/state/clients.tfstate"
    region  = "us-east-1"
    encrypt = true
  }
}

provider "aws" {
  region = "us-east-1"
}

################################################
#                    S3                        #
################################################

module "s3_tfstate" {
  source      = "../common/s3"
  bucket_name = "prod-tfstate-clients"
}

module "s3_frontend" {
  source      = "../common/s3-static"
  bucket_name = "prod-frontend-clients"
}

################################################
#                    EC2                       #
################################################
module "ec2_clients" {
  source   = "../common/ec2"
  ec2_name = "prod-clients-app"
}