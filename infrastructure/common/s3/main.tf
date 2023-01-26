terraform {
  backend "s3" {
    bucket = "my-terraform-state-bucket"
    key    = "path/to/my/state/file"
    region = "us-west-2"
  }
}