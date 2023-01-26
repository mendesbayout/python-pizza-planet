resource "aws_cloudfront_distribution" "my_distribution" {
  origin {
    domain_name = "my-frontend-bucket.s3.amazonaws.com"
    origin_id   = "S3-my-frontend-bucket"

    s3_origin_config {
      origin_access_identity = "${aws_cloudfront_origin_access_identity.example.cloudfront_access_identity_path}"
    }
  }
  // other cloudfront configuration
  enabled = false
  default_cache_behavior {}
  restrictions {}
  viewer_certificate {}
}