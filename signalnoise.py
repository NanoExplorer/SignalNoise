import random
import winclip
def main():
    message = "start"
    p = float(input("Bitflip probability: "))
    while message != "":
        out = ""
        message = input("Write message: ")
        flips = 0
        numbers = [ord(c) for c in message]
        bitprobs = [[random.random() for y in range(8)]for x in range(len(message))]
        for i,byte in enumerate(bitprobs):
            number= 0
            for j,bit in enumerate(byte):
                if bit < p:
                    number = number | 1 << j
                    flips += 1
            #print("{:b}".format(number))
            out = out + chr( numbers[i]  ^ number)
        print(out)
        print("{} bits flipped".format(flips))
        winclip.copy(out)
if __name__ == "__main__":
    main()
