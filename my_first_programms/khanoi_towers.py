step = 1


def hanoi_towers(from_tower=1, to_tower=3, over_tower=2, ring_count=3):
    global step
    if ring_count != 0:
        hanoi_towers(from_tower, over_tower, to_tower, ring_count - 1)
        print(f'шаг {step}: со стержня {from_tower} >>> на стержень {to_tower}')
        step += 1
        hanoi_towers(over_tower, to_tower, from_tower, ring_count - 1)


# def hanoi_towers(from_tower=1, to_tower=3, over_tower=2, ring_count=3):
#     global step
#     if ring_count > 1:
#         hanoi_towers(from_tower, over_tower, to_tower, ring_count - 1)
#     print(f'шаг {step}: со стержня {from_tower} >>> на стержень {to_tower}')
#     step += 1
#     if ring_count > 1:
#         hanoi_towers(over_tower, to_tower, from_tower, ring_count - 1)


def main():
    hanoi_towers()


if __name__ == '__main__':
    main()
