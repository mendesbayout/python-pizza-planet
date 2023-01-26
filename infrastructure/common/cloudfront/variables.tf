variable "Pizza_planet_service" {
  type        = string
  description = "The domain name of the origin server that CloudFront will use to retrieve content."
}

variable "origin_path" {
  type        = string
  default     = ""
  description = "The path to the origin that CloudFront will use to retrieve content."
}

variable "viewer_protocol_policy" {
  type    = string
  default = "redirect-to-https"
  description = "The protocol that viewers use to access the files. Valid values are 'allow-all', 'https-only', or 'redirect-to-https'."
}

variable "default_root_object" {
  type    = string
  default = "index.html"
  description = "The object that you want CloudFront to return when a viewer requests the root URL for your distribution."
}

variable "price_class" {
  type    = string
  default = "PriceClass_200"
  description = "The price class for this distribution. Valid values are 'PriceClass_100' (for the US, Europe, and Asia), 'PriceClass_200' (for all of the above plus Australia), and 'PriceClass_All' (for all locations)."
}

variable "aliases" {
  type    = list(string)
  default = []
  description = "An array of domain names that you want to associate with your CloudFront distribution"
}

variable "ssl_certificate_id" {
  type    = string
  description = "The ARN of the ACM certificate that you want to use for the distribution"
}

variable "enabled" {
  type    = bool
  default = true
  description = "Indicates whether this distribution is enabled or disabled."
}

variable "custom_error_responses" {
  type    = list(map(string))
  default = []
  description = "A list of custom error responses to configure for this distribution."
}

variable "logging_enabled" {
  type    = bool
  default = false
  description = "Indicates whether logging is enabled for this distribution."
}