import tiktoken
# encoding = tiktoken.encoding_for_model("cl100k_base") 
encoding = tiktoken.get_encoding("cl100k_base")

# encoding = tiktoken.encoding_for_model("gemini-pro")  # Or the specific model you're using
text = '''
Can you help me with step by step instructions to solve the below problem statement?

<ps>
Deployment of Multicloud App.
Course-end Project 2
Description
To deploy a multi cloud app using two load balancer setups in AWS and Azure platform.

Background of the problem statement:

A B2C company serving the global audience wants to ensure high availability for its end users using their web app which can be accessed from anywhere in the world. Since the web app gets multimillion traffic on a daily basis, the company cannot afford to have downtime on their app. So, they have decided to deploy the web app on two cloud platforms, on AWS and Azure to ensure that the resiliency is maintained.

Create an architecture and the step-by-step guide to provide a solution for the above problem statement.

You must use the following:

Azure​
AWS
</ps>'''


response = '''
Step-by-Step Guide for Deploying a Multi-Cloud App with Load Balancers in AWS and Azure
This guide outlines a multi-cloud deployment strategy for high availability, using AWS and Azure. It leverages load balancers in both environments and a DNS failover mechanism for global traffic distribution.

Phase 1: AWS Deployment

Create AWS Resources:

EC2 Instances (Web Servers): Launch multiple EC2 instances in at least two different Availability Zones within a chosen region. Install the web application on each instance.

Application Load Balancer (ALB): Create an ALB in the same region. Configure listeners on port 80 (HTTP) and/or 443 (HTTPS).

Target Group: Create a target group for the ALB. Register the EC2 instances as targets in the target group. This ensures the ALB distributes traffic across the healthy instances.

Security Groups: Configure security groups to allow traffic on ports 80/443 to the EC2 instances from the ALB. Also, restrict SSH access to your IP address or a bastion host for management.

Amazon Machine Image (AMI): Consider creating a custom AMI with your application pre-installed for faster deployment and scaling.

Test AWS Deployment:

Access the ALB's DNS name in your web browser. Verify that the application is accessible and the load balancer is distributing traffic across the instances.

Phase 2: Azure Deployment

Create Azure Resources:

Virtual Machines (VMs): Create multiple VMs in at least two different Availability Zones within a chosen region. Install the web application on each VM.

Azure Load Balancer: Create a Load Balancer in the same region. Configure a frontend IP configuration and a backend pool.

Health Probes: Configure health probes to monitor the health of the VMs.

Load Balancing Rules: Create load balancing rules to distribute traffic on ports 80/443 to the backend pool.

Network Security Group (NSG): Configure an NSG to allow traffic on ports 80/443 to the VMs from the Load Balancer. Also, restrict SSH access to your IP address or a bastion host.

Virtual Machine Scale Sets (Optional): Consider using VM Scale Sets for automatic scaling based on demand.

Test Azure Deployment:

Access the Azure Load Balancer's public IP address or DNS name in your web browser. Verify that the application is accessible and the load balancer is distributing traffic.

Phase 3: DNS Failover Configuration (Using a DNS Service like Route 53 or Azure DNS)

Choose a DNS provider: Select either AWS Route 53 or Azure DNS. We'll use Route 53 as an example.

Create a Hosted Zone: Create a hosted zone for your domain (e.g., example.com).

Create DNS Records:

Create an 'A' record: Point your domain (e.g., www.example.com) to the AWS ALB's DNS name. Set a low TTL (Time To Live) like 60 seconds. This allows for faster failover.

Create a second 'A' record: Point your domain to the Azure Load Balancer's public IP address or DNS name. Set the same low TTL.

Configure Health Checks: Configure health checks in Route 53 to monitor the health of both the AWS ALB and the Azure Load Balancer.

Configure Failover Routing Policy: Create a failover routing policy that directs traffic to the Azure Load Balancer if the AWS ALB becomes unhealthy, and vice versa.

Phase 4: Testing and Monitoring

Test Failover: Simulate a failure in one cloud environment (e.g., stop the AWS EC2 instances). Verify that traffic automatically switches to the other cloud (Azure).

Monitoring: Implement monitoring tools (e.g., CloudWatch in AWS, Azure Monitor) to track the health and performance of your application and infrastructure in both cloud environments. Set up alerts for critical events.

Key Considerations:

Database: Choose a database solution that works across both clouds or replicate your database to both environments.

Data Synchronization: If your application requires data synchronization between clouds, implement appropriate mechanisms (e.g., message queues).

Cost Optimization: Analyze the pricing models of both cloud providers to optimize costs.

Security: Implement robust security measures in both cloud environments, including network security, access control, and data encryption.

This comprehensive approach ensures high availability and resilience for your web application by distributing traffic across multiple cloud platforms. Remember to thoroughly test and monitor your deployment to ensure optimal performance and reliability.
'''
num_tokens = len(encoding.encode(text))
num_tokens_res = len(encoding.encode(response))
print(f"Number of tokens: {num_tokens}")
print(f"Number of tokens in response: {num_tokens_res}")