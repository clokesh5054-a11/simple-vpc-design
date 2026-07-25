variable "aws_region" {
  description = "The AWS region to deploy resources into."
  type        = string
  default     = "us-east-1"
}

variable "vpc_cidr" {
  description = "The CIDR block for the VPC."
  type        = string
  default     = "10.0.0.0/16"
}

variable "public_subnet_cidr" {
  description = "The CIDR block for the public subnet."
  type        = string
  default     = "10.0.1.0/24"
}

variable "private_subnet_cidr" {
  description = "The CIDR block for the private subnet."
  type        = string
  default     = "10.0.2.0/24"
}

variable "allowed_ssh_ip" {
  description = "The IP address range allowed to SSH into the web server (CIDR notation)."
  type        = string
  default     = "0.0.0.0/0" # In a production environment, restrict this to your specific IP
}

variable "instance_type" {
  description = "The EC2 instance type for the servers."
  type        = string
  default     = "t2.micro"
}

variable "project_name" {
  description = "The name of the project, used for resource tagging."
  type        = string
  default     = "simple-vpc-design"
}

variable "environment" {
  description = "The environment name, used for resource tagging."
  type        = string
  default     = "Dev"
}
