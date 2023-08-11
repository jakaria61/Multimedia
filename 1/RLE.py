def encode_rle(data):
    encoded = ""
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            encoded += str(count) + data[i - 1]
            count = 1
    encoded += str(count) + data[-1]
    return encoded


def decode_rle(encoded):
    decoded = ""
    i = 0
    while i < len(encoded):
        count = int(encoded[i])
        char = encoded[i + 1]
        decoded += char * count
        i += 2
    return decoded


def main():
    input_file = "input.txt"
    output_encoded_file = "encoded_output.txt"
    output_decoded_file = "decoded_output.txt"

    with open(input_file, 'r') as file:
        data = file.read()

    encoded_data = encode_rle(data)
    decoded_data = decode_rle(encoded_data)

    with open(output_encoded_file, 'w') as file:
        file.write(encoded_data)

    with open(output_decoded_file, 'w') as file:
        file.write(decoded_data)

    print("RLE encoding and decoding completed.")


if __name__ == "__main__":
    main()
