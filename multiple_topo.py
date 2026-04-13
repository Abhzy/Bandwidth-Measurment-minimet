from mininet.topo import Topo

class LinearTopo(Topo):
    def build(self, n=3):
        # Create switches
        switches = []
        for i in range(1, n+1):
            switches.append(self.addSwitch(f's{i}'))

        # Create hosts and connect to switches
        for i in range(1, n+1):
            host = self.addHost(f'h{i}')
            self.addLink(host, switches[i-1])

        # Connect switches linearly
        for i in range(n-1):
            self.addLink(switches[i], switches[i+1])

topos = {'lineartopo': (lambda: LinearTopo())}
