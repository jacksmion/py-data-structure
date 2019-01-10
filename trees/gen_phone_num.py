

import random


def gen_phone_num():
    num_type = ['130', '133', '134', '180', '187', '189']
    phone_num = "".join([str(random.randint(0,9)) for n in xrange(9)])
    return random.choice(num_type) + phone_num


def main():
    with open('phone.txt', 'w') as fp:
        for n in range(1000):
            fp.write(gen_phone_num() + '\n')

main()