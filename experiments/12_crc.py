"""Generate and verify a CRC codeword using modulo-2 division."""

import argparse


def validate_bits(value: str, label: str) -> None:
    if not value or set(value) - {"0", "1"}:
        raise ValueError(f"{label} must contain only 0 and 1")


def modulo2_remainder(bits: str, generator: str) -> str:
    validate_bits(bits, "data")
    validate_bits(generator, "generator")
    if len(generator) < 2 or generator[0] != "1" or generator[-1] != "1":
        raise ValueError("generator must have at least two bits and begin/end with 1")

    work = list(bits)
    for offset in range(len(bits) - len(generator) + 1):
        if work[offset] == "1":
            for index, bit in enumerate(generator):
                work[offset + index] = str(int(work[offset + index]) ^ int(bit))
    return "".join(work[-(len(generator) - 1):]).zfill(len(generator) - 1)


def encode(data: str, generator: str) -> tuple[str, str]:
    validate_bits(data, "data")
    remainder = modulo2_remainder(data + "0" * (len(generator) - 1), generator)
    return remainder, data + remainder


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", help="binary message; prompted for if omitted")
    parser.add_argument("--generator", help="binary generator polynomial; prompted for if omitted")
    args = parser.parse_args()
    data = args.data if args.data is not None else input("Data bits: ").strip()
    generator = (
        args.generator if args.generator is not None else input("Generator bits: ").strip()
    )

    try:
        remainder, codeword = encode(data, generator)
        check = modulo2_remainder(codeword, generator)
    except ValueError as error:
        parser.error(str(error))
    print(f"CRC remainder: {remainder}")
    print(f"Transmitted codeword: {codeword}")
    print(f"Receiver check remainder: {check}")
    print("Result: valid codeword" if set(check) == {"0"} else "Result: error detected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
