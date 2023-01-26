terraform {
  backend "s3" {
    bucket = "my-terraform-state-bucket"
    key    = "path/to/my/terraform_state/terraform.tfstate"
    region = "us-west-2"
  }
}

provider "aws" {
  region = "us-west-2"
}

resource "aws_s3_bucket" "my_terraform_state_bucket" {
  bucket = "my-terraform-state-bucket"
  acl    = "private"
}

resource "aws_cloudfront_distribution" "my_distribution" {
  origin {
    domain_name = "my-frontend-bucket.s3.amazonaws.com"
    origin_id   = "S3-my-frontend-bucket"

    s3_origin_config {
      origin_access_identity = aws_cloudfront_origin_access_identity.example.cloudfront_access_identity_path
    }
  }
  // other cloudfront configuration
  enabled = false
  default_cache_behavior {
    allowed_methods        = []
    cached_methods         = []
    target_origin_id       = ""
    viewer_protocol_policy = ""
  }
  restrictions {}
  viewer_certificate {}
}

resource "aws_rds_instance" "my_rds_instance" {
  engine                  = "postgres"
  engine_version          = "12.4"
  instance_class          = "db.t2.micro"
  // other RDS configuration
}

resource "aws_instance" "my_ec2_instance" {
  ami           = "ami-0ff8a91507f77f867"
  instance_type = "t2.micro"

  vpc_security_group_ids = [aws_security_group.example.id]
  // other EC2 configuration
}