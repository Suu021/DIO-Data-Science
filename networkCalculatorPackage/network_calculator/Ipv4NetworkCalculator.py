import re


class Ipv4NetworkCalculator():
    def __init__(self, ip: str, prefix: int = 0, mask: str = '', network='',
                 broadcast='', num_ips=''):
        self.ip = ip
        self.prefix = prefix
        self.mask = mask
        self.network = network
        self.broadcast = broadcast
        self.num_ips = num_ips

        self.ip_with_prefix()

        if not self.is_ip():
            raise ValueError("Invalid IP.")

        if not self.prefix and not self.mask:
            raise ValueError("Or prefix or mask should be informed")

        if self.mask:
            self.mask_bin: str = self.decimalIP_to_binary(ip=self.mask)
            self.mask_prefix()

        self.set_ip_nums()
        self.set_network_broadcast()
        self.prefix_mask()
        for key, value in self.get_all().items():
            print(f'{key}: {value}')

    def prefix_mask(self):
        bin_mask = ''

        for i in range(32):
            if i < self.prefix:
                bin_mask += '1'
            else:
                bin_mask += '0'
        dec_mask = self.binIP_to_decimal(bin_mask)
        self.mask = dec_mask

    def set_network_broadcast(self):
        ip_bin = self.decimalIP_to_binary(self.ip).replace('.', '')

        network = ''
        broadcast = ''
        for count, bit in enumerate(ip_bin):
            if count < self.prefix:
                network += bit
                broadcast += bit
            else:
                network += '0'
                broadcast += '1'
        self.network = self.binIP_to_decimal(network)
        self.broadcast = self.binIP_to_decimal(broadcast)

    def binIP_to_decimal(self, ip):
        newIP = str(int(ip[0:8], 2)) + '.'
        newIP += str(int(ip[8:16], 2)) + '.'
        newIP += str(int(ip[16:24], 2)) + '.'
        newIP += str(int(ip[24:32], 2))
        return newIP

    def mask_prefix(self):
        mask_bin = self.mask_bin.replace('.', '')
        count = 0

        for bit in mask_bin:
            if bit == '1':
                count += 1

        self.prefix = count

    def set_ip_nums(self):
        host_bits = 32-self.prefix
        self.num_ips = pow(2, host_bits)

    def ip_with_prefix(self):
        # ex: 192.168.52.75/24
        ip_prefix_regex = re.compile("^(?:2[0-4][0-9]|25[0-5]|1?[0-9]?[0-9])[.](?:2[0-4][0-9]|25[0-5]|1?[0-9]?[0-9])[.](?:2[0-4][0-9]|25[0-5]|1?[0-9]?[0-9])[.](?:2[0-4][0-9]|25[0-5]|1?[0-9]?[0-9])[/][0-9]{1,3}$")

        if not ip_prefix_regex.search(self.ip):
            return

        split_ip = self.ip.split('/')
        self.ip = split_ip[0]
        self.prefix = int(split_ip[1])

    def is_ip(self):
        ip_regex = re.compile("^(?:2[0-4][0-9]|25[0-5]|1?[0-9]?[0-9])[.](?:2[0-4][0-9]|25[0-5]|1?[0-9]?[0-9])[.](?:2[0-4][0-9]|25[0-5]|1?[0-9]?[0-9])[.](?:2[0-4][0-9]|25[0-5]|1?[0-9]?[0-9])$")
        if ip_regex.search(self.ip):
            return True
        return False

    def decimalIP_to_binary(self, ip: str = ''):
        if not ip:
            ip = self.ip
        ip_bin = []
        ip_block = ip.split('.')
        for block in ip_block:
            binaryBlock = bin(int(block))[2:].zfill(8)
            ip_bin.append(binaryBlock)
        ip_bin = '.'.join(ip_bin)
        return ip_bin

    def get_all(self):
        return {
            'ip': self.ip,
            'prefix': self.prefix,
            'mask': self.mask,
            'gateway': self.network,
            'broadcast': self.broadcast,
            'total number of IPs': self.num_ips,
            'total number of available hosts': (self.num_ips - 2)
        }


# if __name__ == '__main__':
#     ipv4 = Ipv4NetworkCalculator(ip='')
#     print(ipv4.get_all())
