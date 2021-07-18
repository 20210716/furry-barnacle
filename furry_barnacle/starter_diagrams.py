from diagrams import Cluster, Diagram
from diagrams.generic.storage import Storage
from diagrams.onprem.client import Client
from diagrams.onprem.compute import Server
from diagrams.onprem.database import Postgresql
from diagrams.onprem.network import Apache
from diagrams.programming.flowchart import PredefinedProcess

with Diagram("Starter Diagram", show=False, direction="LR"):
    with Cluster("server1"):
        web = Apache("web")
        db = Postgresql("db")
        data = Storage("fs")

    with Cluster("server3"):
        ftp = Server("ftp")

    with Cluster("operations"):
        console = Client("console")
        engine = PredefinedProcess("engine")

    provider = Client("provider")

    console - data
    console - web
    console << db
    console >> engine >> db
    ftp - data
    provider >> ftp
    web - data
    web - db
