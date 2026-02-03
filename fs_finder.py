import sys

SIGNATURES = [
    #compression
    (b"\x1F\x8B",        "gzip"),
    (b"\x5D\x00\x00",    "lzma"),
    (b"\xFD\x37\x7A\x58\x5A\x00", "xz"),
    (b"\x89\x4C\x5A",    "lzo"),

    #filesystems
    (b"hsqs",            "SquashFS"),
    (b"\x28\xCD\x3D\x45","CRAMFS"),
    (b"-rom1fs-",        "ROMFS"),
    (b"070701",          "CPIO (initramfs)"),
    (b"UBI#",            "UBI"),
    (b"\x53\xEF",        "EXT (superblock)"),
]

def scan(filename):
    with open(filename, "rb") as f:
        data = f.read()

    print(f"[...] File size: {len(data)} bytes\n")

    found = False

    for sig, name in SIGNATURES:
        start = 0
        while True:
            pos = data.find(sig, start)
            if pos == -1:
                break
            print(f"[!] Found {name:<20} at offset 0x{pos:08X} ({pos})")
            found = True
            start = pos + 1

    if not found:
        print("[-] No known FS or compression signatures found")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} firmware.bin")
        sys.exit(1)

    scan(sys.argv[1])
