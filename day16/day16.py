def hex_to_bin(hex):
    lookup = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111',
    }
    return "".join([lookup[h] for h in hex])

def unpack(packet):
    version = packet[:3]
    type_id = packet[3:6]
    rest = packet[6:]

    return int(version,2), int(type_id,2), rest

def parse_literals(packet):
    # literal value
    literal = ""
    while True:
        literal += packet[1:5]
        start = packet[0]
        packet = packet[5:]
        if start=="0":
            break
    return int(literal, 2), packet

def product(X):
    result = 1
    for x in X:
        result *= x
    return result

def decode_packet(packet, version_sum):
    version, type_id, rest = unpack(packet)

    version_sum += version

    if type_id==4:
        literal, rest = parse_literals(rest)
    else:
        length_type_id = int(rest[0])
        literals = list()
        if length_type_id==0:
            # next 15 bits are number that represents total length in bits of sub-packets contained by this package
            total_length = int(rest[1:16], 2)
            sub_packet =  rest[16:(16+total_length)]
            rest = rest[(16+total_length):]
            while len(sub_packet) > 0:
                literal, sub_packet, version_sum = decode_packet(sub_packet, version_sum)
                literals.append(literal)
        elif length_type_id==1:
            # next 11 bits are number that represents number of sub-packets immediately contained in packet
            n_sub_packets = int(rest[1:12], 2)
            rest = rest[12:]
            for _ in range(n_sub_packets):
                literal, rest, version_sum = decode_packet(rest, version_sum)
                literals.append(literal)
        else:
            raise ValueError(f"{length_type_id} is not a valid length type id")
    
    
    if type_id==0:
        literal = sum(literals)
    if type_id==1:
        literal = product(literals)
    if type_id==2:
        literal = min(literals)
    if type_id==3:
        literal = max(literals)
    if type_id==5:
        literal = 1 if literals[0] > literals[1] else 0
    if type_id==6:
        literal = 1 if literals[0] < literals[1] else 0
    if type_id==7:
        literal = 1 if literals[0] == literals[1] else 0

    return literal, rest, version_sum


# part 1 tests
assert decode_packet(hex_to_bin("8A004A801A8002F478"),0)[2]==16
assert decode_packet(hex_to_bin("620080001611562C8802118E34"),0)[2]==12
assert decode_packet(hex_to_bin("C0015000016115A2E0802F182340"),0)[2]==23
assert decode_packet(hex_to_bin("A0016C880162017C3686B18A3D4780"),0)[2]==31

# part 2 tests
assert decode_packet(hex_to_bin("C200B40A82"),0)[0]==3
assert decode_packet(hex_to_bin("04005AC33890"),0)[0]==54
assert decode_packet(hex_to_bin("880086C3E88112"),0)[0]==7
assert decode_packet(hex_to_bin("CE00C43D881120"),0)[0]==9
assert decode_packet(hex_to_bin("D8005AC2A8F0"),0)[0]==1
assert decode_packet(hex_to_bin("F600BC2D8F"),0)[0]==0
assert decode_packet(hex_to_bin("9C005AC2F8F0"),0)[0]==0
assert decode_packet(hex_to_bin("9C0141080250320F1802104A08"),0)[0]==1

if __name__=='__main__':
    with open("day16/inputs/input1.txt", "r") as f:
        input1 = f.read()

    literal, rest, version_sum = decode_packet(hex_to_bin(input1),0)
    print(version_sum)
    print(literal)