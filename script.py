#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='10.0.0.0/8')

    info( '*** Adding controller\n' )
    c0=net.addController(name='c0',
                      controller=Controller,
                      protocol='tcp',
                      port=6633)

    info( '*** Add switches\n')
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)
    s5 = net.addSwitch('s5', cls=OVSKernelSwitch)
    s7 = net.addSwitch('s7', cls=OVSKernelSwitch)
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch)
    s10 = net.addSwitch('s10', cls=OVSKernelSwitch, failMode='standalone')
    s6 = net.addSwitch('s6', cls=OVSKernelSwitch)
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch)
    s8 = net.addSwitch('s8', cls=OVSKernelSwitch)
    s9 = net.addSwitch('s9', cls=OVSKernelSwitch, failMode='standalone')
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch)

    info( '*** Add hosts\n')
    h4 = net.addHost('h4', cls=Host, ip='10.0.0.4', defaultRoute=None)
    h11 = net.addHost('h11', cls=Host, ip='10.0.0.11', defaultRoute=None)
    h6 = net.addHost('h6', cls=Host, ip='10.0.0.6', defaultRoute=None)
    h7 = net.addHost('h7', cls=Host, ip='10.0.0.7', defaultRoute=None)
    h10 = net.addHost('h10', cls=Host, ip='10.0.0.10', defaultRoute=None)
    h8 = net.addHost('h8', cls=Host, ip='10.0.0.8', defaultRoute=None)
    h9 = net.addHost('h9', cls=Host, ip='10.0.0.9', defaultRoute=None)
    h3 = net.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
    h12 = net.addHost('h12', cls=Host, ip='10.0.0.12', defaultRoute=None)
    h5 = net.addHost('h5', cls=Host, ip='10.0.0.5', defaultRoute=None)

    info( '*** Add links\n')
    s2s1 = {'bw':1000,'delay':'10','loss':1}
    net.addLink(s2, s1, cls=TCLink , **s2s1)
    s1s3 = {'bw':200,'delay':'20','loss':2}
    net.addLink(s1, s3, cls=TCLink , **s1s3)
    s1s4 = {'bw':50,'delay':'100','loss':5}
    net.addLink(s1, s4, cls=TCLink , **s1s4)
    h1s5 = {'bw':500,'delay':'10','loss':1}
    net.addLink(h1, s5, cls=TCLink , **h1s5)
    s5s2 = {'bw':700,'delay':'5','loss':1}
    net.addLink(s5, s2, cls=TCLink , **s5s2)
    s6s2 = {'bw':300,'delay':'5','loss':1}
    net.addLink(s6, s2, cls=TCLink , **s6s2)
    s7s3 = {'bw':100,'delay':'20','loss':1}
    net.addLink(s7, s3, cls=TCLink , **s7s3)
    s3s8 = {'bw':100,'delay':'20','loss':1}
    net.addLink(s3, s8, cls=TCLink , **s3s8)
    s9s4 = {'bw':20,'delay':'50','loss':5}
    net.addLink(s9, s4, cls=TCLink , **s9s4)
    s4s10 = {'bw':30,'delay':'50','loss':1}
    net.addLink(s4, s10, cls=TCLink , **s4s10)
    s5h2 = {'bw':200,'delay':'5','loss':1}
    net.addLink(s5, h2, cls=TCLink , **s5h2)
    h3s6 = {'bw':200,'delay':'10','loss':1}
    net.addLink(h3, s6, cls=TCLink , **h3s6)
    s6h4 = {'bw':100,'delay':'5','loss':1}
    net.addLink(s6, h4, cls=TCLink , **s6h4)
    h5s7 = {'bw':30,'delay':'30','loss':2}
    net.addLink(h5, s7, cls=TCLink , **h5s7)
    s7h6 = {'bw':70,'delay':'30','loss':2}
    net.addLink(s7, h6, cls=TCLink , **s7h6)
    s8h7 = {'bw':50,'delay':'30','loss':2}
    net.addLink(s8, h7, cls=TCLink , **s8h7)
    s8h8 = {'bw':50,'delay':'30','loss':2}
    net.addLink(s8, h8, cls=TCLink , **s8h8)
    h9s9 = {'bw':10,'delay':'50','loss':1}
    net.addLink(h9, s9, cls=TCLink , **h9s9)
    s9h10 = {'bw':10,'delay':'50','loss':1}
    net.addLink(s9, h10, cls=TCLink , **s9h10)
    s10h11 = {'bw':15,'delay':'50','loss':1}
    net.addLink(s10, h11, cls=TCLink , **s10h11)
    s10h12 = {'bw':15,'delay':'50','loss':1}
    net.addLink(s10, h12, cls=TCLink , **s10h12)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s1').start([c0])
    net.get('s5').start([c0])
    net.get('s7').start([c0])
    net.get('s4').start([c0])
    net.get('s10').start([])
    net.get('s6').start([c0])
    net.get('s3').start([c0])
    net.get('s8').start([c0])
    net.get('s9').start([])
    net.get('s2').start([c0])

    info( '*** Post configure switches and hosts\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

