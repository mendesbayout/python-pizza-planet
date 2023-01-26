resource "aws_instance" "my_ec2_instance" {
  ami           = "ami-0ff8a91507f77f867"
  instance_type = "t2.micro"

  vpc_security_group_ids = [aws_security_group.example.id]
  // other EC2 configuration
}