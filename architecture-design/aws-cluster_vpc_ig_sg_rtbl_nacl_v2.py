from diagrams import Diagram, Cluster, Edge
from diagrams.aws.network import VPC, InternetGateway, RouteTable, Nacl
from diagrams.aws.compute import EC2
from diagrams.aws.general import User, Client

graph_attr = {
    "splines": "ortho",
    "nodesep": "0.5",
    "ranksep": "0.75",
}

with Diagram("AWS VPC Architecture", show=False, graph_attr=graph_attr):
    user = Client("User")

    with Cluster("VPC"):
        vpc = VPC("main-vpc")

        igw = InternetGateway("main-gateway")
        user >> Edge(label="Internet connection") >> igw

        with Cluster("Public Subnet"):
            subnet = RouteTable("main-public-subnet")  # Using RouteTable to represent Subnet

            route_table = RouteTable("main-public-rt")
            subnet >> Edge(label="Route Table Association") >> route_table
            igw >> Edge(label="Default Route") >> route_table

            nacl = Nacl("main-acl")
            subnet >> Edge(label="Network ACL Association") >> nacl

            ec2 = EC2("WebServerInstance")
            ec2 - Edge(label="Subnet") - subnet
