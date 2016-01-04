class Firewall2:
    def __init__(self):
        self.table = table = iptc.Table(iptc.Table.FILTER)
        table.autocommit = False

    def accept_established(self):
        table = self.table
        rule = iptc.Rule()
        rule.target = iptc.Target(rule, 'ACCEPT')
        match = iptc.Match(rule, 'state')
        match.state = 'ESTABLISHED,RELATED'
        rule.add_match(match)
        chain = iptc.Chain(table, 'INPUT')
        chain.insert_rule(rule)

    def set_policy(self, chain_name, pol_name):
        table = self.table
        chain = iptc.Chain(table, chain_name)
        pol = iptc.Policy(pol_name)
        chain.set_policy(pol)

    def accept_localhost(self):
        table = self.table
        rule = iptc.Rule()
        rule.in_interface = 'lo'
        rule.target = iptc.Target(rule, 'ACCEPT')
        chain = iptc.Chain(table, 'INPUT')
        chain.insert_rule(rule)

    def accept_port(self, port):
        table = self.table
        rule = iptc.Rule()
        rule.protocol = 'tcp'
        match = iptc.Match(rule, 'tcp')
        match.dport = port
        rule.add_match(match)
        rule.target = iptc.Target(rule, 'ACCEPT')
        chain = iptc.Chain(table, 'INPUT')
        chain.insert_rule(rule)

    def accept_ip(self, ip):
        table = self.table
        rule = iptc.Rule()
        rule.src = ip
        rule.target = iptc.Target(rule, 'ACCEPT')
        chain = iptc.Chain(table, 'INPUT')
        chain.insert_rule(rule)

    def clear(self):
        table = self.table
        table.flush()
        for chain in table.chains:
            for rule in chain.rules:
                chain.delete_rule(rule)
        self.set_policy('INPUT'  , 'ACCEPT') # iptables -P INPUT   ACCEPT
        self.set_policy('OUTPUT' , 'ACCEPT') # iptables -P OUTPUT  ACCEPT
        self.set_policy('FORWARD', 'ACCEPT') # iptables -P FORWARD ACCEPT

    def close(self):
        self.table.commit()
        self.table.autocommit = True

    # TODO reset if cannot connect to internet

def test_firewall():
    fw = Firewall()
    fw.clear()

    table = fw.table
    rule = iptc.Rule()
    rule.target = iptc.Target(rule, 'DROP')
    chain = iptc.Chain(table, 'INPUT')
    chain.insert_rule(rule)

    table = fw.table
    rule = iptc.Rule()
    rule.target = iptc.Target(rule, 'DROP')
    chain = iptc.Chain(table, 'FORWARD')
    chain.insert_rule(rule)

    table = fw.table
    rule = iptc.Rule()
    rule.target = iptc.Target(rule, 'ACCEPT')
    chain = iptc.Chain(table, 'OUTPUT')
    chain.insert_rule(rule)

    #fw.set_policy('INPUT', 'DROP')     # 拒绝
    #fw.set_policy('OUTPUT', 'ACCEPT')  # 开放出口
    #fw.set_policy('FORWARD', 'DROP')   # 拒绝

    fw.accept_established()
    fw.accept_localhost()
    #fw.accept_ip('10.0.0.0/8')
    #fw.accept_ip('172.16.0.0/12')
    #fw.accept_ip('192.168.0.0/16')

    fw.accept_port('9200')
    fw.accept_port('23080')
    #fw.accept_port('28080')

    fw.close()
    os.system('iptables -vL')
