import base64

def main():
    input_string = input("Nhap thong tin can ma hoa: ")

    encoded_bytes = base64.b64encode(input_string.encode("utf-8"))
    encoded_string = str(encoded_bytes, "utf-8")

    with open("data.txt", "w") as file:
        file.write(encoded_string)

    print("Da ma hoa va ghi vao data.txt")

if __name__ == "__main__":
    main()