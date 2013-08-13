import sys

def molecular_weight(sequence):
    sequence = sequence.upper()
    base_weights = {'A': 331, 'C': 307, 'G': 347, 'T': 306}
    total_weight = 0
    for base in sequence:
        total_weight += base_weights[base]
    return total_weight

if len(sys.argv) != 2:
    print "Usage: %s <sequence>" % sys.argv[0]
    sys.exit(0)

weight = molecular_weight(sys.argv[1])

print "Weight:", weight, "g/mol"
