resource "aws_rds_instance" "my_rds_instance" {
  engine                  = "postgres"
  engine_version          = "12.4"
  instance_class          = "db.t2.micro"
  // other RDS configuration
}