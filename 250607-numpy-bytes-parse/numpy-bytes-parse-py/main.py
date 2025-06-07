import numpy
import numpy.random


def main():
    data = numpy.random.randint(0, 10, (2, 2)).reshape((-1, 1))
    data = data.astype(numpy.int64)
    # data = data.astype(">i8")  # big-endian
    print(data)
    with open("../data/data.bin", "wb") as f:
        f.write(data.tobytes())


if __name__ == "__main__":
    main()
