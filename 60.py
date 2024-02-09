lugat = {'V': [10, 12], 'VI': [10], 'VII': [10, 20, 30, 40], 'VIII': [20], 'IX': [10, 30, 50, 70], 'X': [80]}
eng_qisqa = min(lugat.values(), key=len)
eng_qisqa_key = [k for k, v in lugat.items() if v == eng_qisqa]
print(eng_qisqa_key)
