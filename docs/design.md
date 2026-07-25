# AWS VPC Network Design Concepts

This document provides a beginner-friendly overview of the core AWS networking concepts implemented in this project.

---

## 1. What is a VPC (Virtual Private Cloud)?

A **Virtual Private Cloud (VPC)** is a logically isolated virtual network that you define within the AWS cloud. It closely resembles a traditional network that you'd operate in your own data center, but with the benefits of using the scalable infrastructure of AWS.

### Key Characteristics:
* **Logically Isolated**: Your VPC is private. Resources inside it are protected from unauthorized access by default.
* **IP Address Control**: You select the IP address range (CIDR block) for the VPC. In this project, we use `10.0.0.0/16`, providing 65,536 private IP addresses.
* **Regional Resource**: A VPC is bound to a single AWS region but spans all Availability Zones (AZs) in that region.

---

## 2. Public vs. Private Subnets

A **Subnet** is a range of IP addresses in your VPC. Subnets allow you to group resources based on security and routing needs.

| Attribute | Public Subnet | Private Subnet |
| :--- | :--- | :--- |
| **CIDR Block** | `10.0.1.0/24` (256 IPs) | `10.0.2.0/24` (256 IPs) |
| **Internet Access** | Direct access (inbound and outbound) | No direct access (isolated) |
| **Public IP Mapping** | Enabled (`map_public_ip_on_launch = true`) | Disabled |
| **Typical Resources** | Web Servers, Load Balancers, NAT Gateways | Application Servers, Databases, Cache nodes |

### Why separate them?
By separating resources into public and private subnets, you implement the **Principle of Least Privilege** at the network level. Publicly accessible resources (like the Web Server) are exposed to the internet, while sensitive backend services (like the Application Server) remain inaccessible from the outside world.

---

## 3. Why use an Internet Gateway (IGW)?

An **Internet Gateway** is a horizontally scaled, redundant, and highly available VPC component that allows communication between resources in your VPC and the internet.

### Purpose:
1. **Provide a Target**: It serves as a target in your VPC route tables for internet-bound traffic (`0.0.0.0/0`).
2. **Network Address Translation (NAT)**: It performs NAT for instances that have been assigned public IPv4 addresses, ensuring replies from the internet are routed back to the correct instance.

---

## 4. How Route Tables Work

A **Route Table** contains a set of rules, called **routes**, that determine where network traffic from your subnet or gateway is directed.

* **Local Route**: Every route table automatically contains a local route (e.g., `10.0.0.0/16 -> local`). This allows all subnets inside the VPC to communicate with each other by default.
* **Default Route / Internet Route**: To connect to the internet, a route table must have a route specifying `0.0.0.0/0` (all IPv4 traffic) pointing to the Internet Gateway (`igw-xxxxxx`).
* **Subnet Association**: Each subnet must be associated with a route table. If not explicitly associated, it is implicitly associated with the main (default) route table of the VPC.

In this design:
* The **Public Subnet** is explicitly associated with a route table containing a route to the IGW.
* The **Private Subnet** is not associated with the public route table, ensuring it remains isolated.

---

## 5. Security Groups (Stateful Firewalls)

A **Security Group** acts as a virtual firewall for your EC2 instances to control inbound and outbound traffic.

### Crucial Concepts:
* **Stateful**: If you send a request from your instance, the response traffic is allowed to flow in regardless of inbound security group rules (and vice versa).
* **Deny-by-Default**: All inbound traffic is blocked by default until you add rules to allow it.
* **Target Security Groups**: You can configure a security group to accept traffic *only* from instances associated with a specific security group (rather than an IP range). This is used in our project to ensure the App Server only talks to the Web Server.

---

## 6. AWS Networking Best Practices

1. **Least Privilege**: Only allow required ports and protocols. Keep database and application servers in private subnets.
2. **Avoid Wildcard Access**: Avoid opening Port 22 (SSH) to `0.0.0.0/0`. Restrict it to your personal public IP address or use AWS Systems Manager (SSM) Session Manager.
3. **Multi-AZ Deployment**: For production, deploy subnets across multiple Availability Zones to ensure high availability and disaster recovery.
4. **Use NAT Gateways**: If resources in private subnets need outbound internet access (e.g., for software updates), use a NAT Gateway in the public subnet instead of exposing them in a public subnet.
