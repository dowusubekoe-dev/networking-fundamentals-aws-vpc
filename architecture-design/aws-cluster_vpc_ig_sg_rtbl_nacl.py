from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import EC2
from diagrams.aws.network import InternetGateway, RouteTable, VPC, PublicSubnet, Nacl
from diagrams.generic.compute import Rack
from diagrams.aws.general import User

with Diagram("AWS Architecture", show=False):
    user = User("User")

    with Cluster("VPC"):
        igw = InternetGateway("Internet Gateway")
        
        subnet = PublicSubnet("Public Subnet")
        
        route_table = RouteTable("Route Table")
        nacl = Nacl("Network ACL")
        
        security_group = Rack("Security Group")
        ec2 = EC2("EC2 Instance")
        
        igw - route_table
        subnet - route_table
        subnet - nacl
        subnet - ec2
        ec2 - security_group

    user - Edge(label="SSH/HTTP") - ec2