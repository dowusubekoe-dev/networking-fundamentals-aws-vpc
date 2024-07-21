from diagrams import Diagram, Edge
from diagrams.aws.compute import EC2
from diagrams.aws.network import InternetGateway, RouteTable, VPC, PublicSubnet, Nacl
from diagrams.aws.general import General

with Diagram("AWS Architecture", show=False):
    vpc = VPC("VPC")
    
    igw = InternetGateway("Internet Gateway")
    vpc - igw

    subnet = PublicSubnet("Public Subnet")
    vpc - subnet

    route_table = RouteTable("Route Table")
    vpc - route_table
    route_table - igw  # Show that the route table is associated with the internet gateway

    nacl = Nacl("Network ACL")
    subnet - nacl

    security_group = General("Security Group")
    ec2 = EC2("EC2 Instance")
    
    subnet - ec2
    ec2 - Edge(label="Security Group", reverse=True) >> security_group

    subnet - route_table

    # Showing VPC associations
    vpc - subnet
    vpc - nacl
    vpc - security_group
