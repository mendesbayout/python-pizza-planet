locals {
  stage            = "prod"
  region           = "us-east-1"
  ecr_name         = "${local.stage}-pizza-ecr"
  lambda_role_name = "${local.stage}-api-lambda-role"
  lambda_func_name = "${local.stage}-api-lambda-function"
}

