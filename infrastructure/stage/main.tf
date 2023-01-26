terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.9.0"
    }
  }
}

variable "region" {
  default = "us-east-1"
}

provider "aws" {
  region = var.region
}

  ##############################################
  #                    S3                        #
  ################################################
module "s3_tfstate" {
  source      = "../common/s3"
  bucket_name = "${local.stage}-tfstate-clients"
}

module "s3_frontend" {
  source      = "../common/s3-static"
  bucket_name = "${local.stage}-frontend-clients"
}

terraform {
    backend "s3" {
      bucket  = "${local.stage}-tfstate-clients"
      key     = "terraform/state/${local.stage}.tfstate"
      region  = var.region
      encrypt = true
    }
  }