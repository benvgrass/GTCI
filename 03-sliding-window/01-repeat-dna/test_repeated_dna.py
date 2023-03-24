import pytest
from repeated_dna import find_repeated_sequences


@pytest.mark.parametrize("s, k, output", [
    ('AAAAACCCCCAAAAACCCCCC', 8, {'AAAAACCC', 'AAAACCCC', 'AAACCCCC'}),
    ('GGGGGGGGGGGGGGGGGGGGGGGGG', 12, {'G'*12}),
    ('TTTTTCCCCCCCTTTTTTCCCCCCCTTTTTTT', 10, {'TTTTTCCCCC', 'TTTTCCCCCC',
                                              'TTTCCCCCCC', 'TCCCCCCCTT',
                                              'TTCCCCCCCT', 'CCCCCCCTTT',
                                              'CCCCCCTTTT', 'CCCCCTTTTT',
                                              'CCCCTTTTTT', 'CCCCTTTTTT'}),
    ('AAAAAACCCCCCCAAAAAAAACCCCCCCTG', 10, {'AAAAAACCCC', 'AAAAACCCCC',
                                            'AAAACCCCCC', 'AAACCCCCCC'}),
    ('ATATATATATATATAT', 6, {'ATATAT', 'TATATA'})
])
def test_find_repeated_sequences(s, k, output):
    assert find_repeated_sequences(s, k) == output
