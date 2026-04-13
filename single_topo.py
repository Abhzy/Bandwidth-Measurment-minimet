from mininet.topo import Topo

class SingleTopo(Topo):
    def build(self):
        # Add hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')

        # Add switch
        s1 = self.addSwitch('s1')

        # Add links
        self.addLink(h1, s1)
        self.addLink(h2, s1)

# To run this topology
topos = {'singletopo': (lambda: SingleTopo())}
