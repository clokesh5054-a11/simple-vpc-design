output "vpc_id" {
  description = "The ID of the VPC."
  value       = aws_vpc.main.id
}

output "public_subnet_id" {
  description = "The ID of the Public Subnet."
  value       = aws_subnet.public.id
}

output "private_subnet_id" {
  description = "The ID of the Private Subnet."
  value       = aws_subnet.private.id
}

output "web_server_public_ip" {
  description = "The public IP address of the Web Server."
  value       = aws_instance.web.public_ip
}

output "web_server_private_ip" {
  description = "The private IP address of the Web Server."
  value       = aws_instance.web.private_ip
}

output "app_server_private_ip" {
  description = "The private IP address of the Application Server."
  value       = aws_instance.app.private_ip
}

output "web_security_group_id" {
  description = "The ID of the Web Server Security Group."
  value       = aws_security_group.web_sg.id
}

output "app_security_group_id" {
  description = "The ID of the Application Server Security Group."
  value       = aws_security_group.app_sg.id
}
