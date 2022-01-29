from p4utils.mininetlib.network_API import NetworkAPI

net = NetworkAPI()

# Network general options
net.setLogLevel('info')
net.enableCli()

# Network definition
net.addHost('h1')
net.addHost('h2')
net.addHost('h3')
net.addHost('h4')
net.addP4Switch('s1', cli_input='s1-commands.txt')
net.setP4Source('s1', 'ip_forwarding.p4')
net.addP4Switch('s2', cli_input='s2-commands.txt')
net.setP4Source('s2', 'ip_forwarding.p4')
net.addP4Switch('s3', cli_input='s3-commands.txt')
net.setP4Source('s3', 'ip_forwarding.p4')
net.addP4Switch('s4', cli_input='s4-commands.txt')
net.setP4Source('s4', 'ip_forwarding.p4')



net.addLink("h1", "s1", 1 , 1)
net.addLink("h2", "s1", 2 , 2)
net.addLink("h3", "s2", 1 , 1)
net.addLink("h4", "s2", 2 , 2)
net.addLink("s1", "s3", 3 , 1)
net.addLink("s1", "s4", 4 , 2)
net.addLink("s2", "s3", 3 , 2)
net.addLink("s2", "s4", 4 , 1)

net.setIntfName('h1', 's1', 'h1-s1')
net.setIntfName('h2', 's1', 'h2-s1')
net.setIntfName('h3', 's2', 'h3-s2')
net.setIntfName('h4', 's2', 'h4-s2')
net.setIntfName('s1', 's3', 's1-s3')
net.setIntfName('s1', 's4', 's1-s4')
net.setIntfName('s2', 's3', 's2-s3')
net.setIntfName('s2', 's4', 's2-s4')






# Assignment strategy
net.mixed()

# Nodes general options
net.enablePcapDumpAll()
net.enableLogAll()

# Start network
net.startNetwork()