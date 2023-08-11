def lzw_encode(data):
    dictionary = {chr(i): i for i in range(256)}
    current_code = 256
    result = []
    buffer = ""

    for char in data:
        new_buffer = buffer + char
        if new_buffer in dictionary:
            buffer = new_buffer
        else:
            result.append(dictionary[buffer])
            dictionary[new_buffer] = current_code
            current_code += 1
            buffer = char

    if buffer:
        result.append(dictionary[buffer])

    return result


def lzw_decode(encoded_data):
    dictionary = {i: chr(i) for i in range(256)}
    current_code = 256
    result = []

    prev_code = encoded_data[0]
    result.append(dictionary[prev_code])

    for code in encoded_data[1:]:
        if code in dictionary:
            entry = dictionary[code]
        elif code == current_code:
            entry = dictionary[prev_code] + dictionary[prev_code][0]
        else:
            raise ValueError("Invalid code")

        result.append(entry)
        dictionary[current_code] = dictionary[prev_code] + entry[0]
        current_code += 1
        prev_code = code

    return ''.join(result)


def main():
    input_file = "input.txt"
    output_encoded_file = "encoded_output.txt"
    output_decoded_file = "decoded_output.txt"

    with open(input_file, 'r') as file:
        data = file.read()

    encoded_data = lzw_encode(data)
    decoded_data = lzw_decode(encoded_data)

    with open(output_encoded_file, 'w') as file:
        file.write(' '.join(map(str, encoded_data)))

    with open(output_decoded_file, 'w') as file:
        file.write(decoded_data)

    print("LZW encoding and decoding completed.")


if __name__ == "__main__":
    main()
