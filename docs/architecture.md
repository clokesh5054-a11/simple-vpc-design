# AWS VPC Architecture Specification

This document details the configuration and technical specifications of all resources deployed in this project.

---

## 1. Virtual Private Cloud (VPC)

* **Resource Name (Terraform)**: `aws_vpc.main`
* **CIDR Block**: `10.0.0.0/16`
* **Total IP Addresses**: 65,536
* **DNS Settings**:
  * `enable_dns_hostnames = true` (Instances receive public DNS hostnames matching their public IPs)
  * `enable_dns_support = true` (AWS DNS resolution is enabled)
* **Tags**:
  * `Name`: `simple-vpc-design-vpc`
  * `Project`: `simple-vpc-design`
  * `Environment`: `Dev`

---

## 2. Internet Gateway (IGW)

* **Resource Name (Terraform)**: `aws_internet_gateway.gw`
* **Attachment**: Bound directly to `aws_vpc.main`.
* **Function**: Enables bidirectional communication between resources inside the public subnet and the public internet.
* **Tags**:
  * `Name`: `simple-vpc-design-igw`
  * `Project`: `simple-vpc-design`
  * `Environment`: `Dev`

---

## 3. Subnets

### Public Subnet
* **Resource Name (Terraform)**: `aws_subnet.public`
* **CIDR Block**: `10.0.1.0/24` (256 IP addresses)
* **Availability Zone**: Dynamically selected by AWS in the target region.
* **Public IPs**: Enabled (`map_public_ip_on_launch = true`). Instances launched here automatically receive a public IPv4 address.
* **Associated Route Table**: Public Route Table (`aws_route_table.public`).

### Private Subnet
* **Resource Name (Terraform)**: `aws_subnet.private`
* **CIDR Block**: `10.0.2.0/24` (256 IP addresses)
* **Availability Zone**: Same region, dynamically selected by AWS.
* **Public IPs**: Disabled. Instances only receive private IPs (`10.0.2.x`).
* **Associated Route Table**: Main (Default) Route Table. Since this default table has no internet route, the subnet remains private.

---

## 4. Route Tables

### Public Route Table
* **Resource Name (Terraform)**: `aws_route_table.public`
* **Routes**:
  1. `10.0.0.0/16` ➔ `local` (Allows internal communication to all VPC subnets)
  2. `0.0.0.0/0` ➔ `igw-xxxxxx` (Directs all external traffic to the Internet Gateway)
* **Associations**: Associated with the Public Subnet.

---

## 5. Security Groups

### Web Server Security Group (`web_sg`)
* **Resource Name (Terraform)**: `aws_security_group.web_sg`
* **Description**: Stateful firewall protecting the Web Server.
* **Rules**:
  * **Inbound Rules**:
    * **SSH (Port 22)**: Sourced from `var.allowed_ssh_ip` (user's specific IP/subnet for secure management).
    * **HTTP (Port 80)**: Sourced from `0.0.0.0/0` (allows any browser to access the website).
    * **HTTPS (Port 443)**: Sourced from `0.0.0.0/0` (allows secure web traffic).
  * **Outbound Rules**:
    * **All Traffic (All Ports)**: Destined to `0.0.0.0/0` (allows the server to fetch software updates).

### Application Server Security Group (`app_sg`)
* **Resource Name (Terraform)**: `aws_security_group.app_sg`
* **Description**: Stateful firewall protecting the Application Server.
* **Rules**:
  * **Inbound Rules**:
    * **All TCP Traffic (Ports 0-65535)**: Allowed ONLY if the traffic originates from instances associated with the Web Server Security Group (`web_sg`).
  * **Outbound Rules**:
    * **All Traffic (All Ports)**: Destined to `0.0.0.0/0`.

---

## 6. Compute Instances (EC2)

### Web Server
* **Resource Name (Terraform)**: `aws_instance.web`
* **Location**: Public Subnet (`10.0.1.x`)
* **AMI**: Latest Amazon Linux 2023 (`al2023-ami-2023.*-kernel-6.1-x86_64`)
* **Instance Type**: `t2.micro` (eligible for AWS Free Tier)
* **Security Group**: Associated with Web Server Security Group (`web_sg`).
* **IP Details**: Receives both a Private IP (`10.0.1.x`) and a Public IP.

### Application Server
* **Resource Name (Terraform)**: `aws_instance.app`
* **Location**: Private Subnet (`10.0.2.x`)
* **AMI**: Latest Amazon Linux 2023 (`al2023-ami-2023.*-kernel-6.1-x86_64`)
* **Instance Type**: `t2.micro` (eligible for AWS Free Tier)
* **Security Group**: Associated with Application Server Security Group (`app_sg`).
* **IP Details**: Receives only a Private IP (`10.0.2.x`).
