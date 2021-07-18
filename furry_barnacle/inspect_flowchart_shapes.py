import diagrams.programming.flowchart as fc
from diagrams import Diagram, Node

with Diagram("flowchart stuff", show=False):
    a = None
    for n in dir(fc):
        o = getattr(fc, n)
        if isinstance(o, type):
            if issubclass(o, Node):
                if not n.startswith("_"):
                    b = o(n)
                    if a is not None:
                        a >> b
                    a = b
