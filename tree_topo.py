from mininet.topo import Topo

class TreeTopoCustom(Topo):
    def build(self):
        # Core switch
        s1 = self.addSwitch('s1')

        # Aggregation switches
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')

        # Connect core to aggregation
        self.addLink(s1, s2)
        self.addLink(s1, s3)

        # Hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')

        # Connect hosts
        self.addLink(h1, s2)
        self.addLink(h2, s2)
        self.addLink(h3, s3)
        self.addLink(h4, s3)

topos = {'treetopo': (lambda: TreeTopoCustom())}
