#!/usr/bin/env python3
import struct
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "dist" / "traffic.pcap"
NOTE = "ZWR1X2N0Znt0cmFmZmljX25vdGVfZm91bmR9"


def checksum(data: bytes) -> int:
    if len(data) % 2:
        data += b"\x00"
    total = sum(struct.unpack("!" + "H" * (len(data) // 2), data))
    while total >> 16:
        total = (total & 0xFFFF) + (total >> 16)
    return (~total) & 0xFFFF


def packet(payload: bytes, src_ip: bytes, dst_ip: bytes, src_port: int, dst_port: int, seq: int, ack: int) -> bytes:
    eth = bytes.fromhex("66778899aabb0011223344550800")
    tcp_len = 20 + len(payload)
    total_len = 20 + tcp_len
    ip_no_sum = struct.pack("!BBHHHBBH4s4s", 0x45, 0, total_len, 1, 0x4000, 64, 6, 0, src_ip, dst_ip)
    ip = ip_no_sum[:10] + struct.pack("!H", checksum(ip_no_sum)) + ip_no_sum[12:]
    tcp_no_sum = struct.pack("!HHIIBBHHH", src_port, dst_port, seq, ack, 0x50, 0x18, 4096, 0, 0)
    pseudo = src_ip + dst_ip + struct.pack("!BBH", 0, 6, tcp_len)
    tcp_sum = checksum(pseudo + tcp_no_sum + payload)
    tcp = tcp_no_sum[:16] + struct.pack("!H", tcp_sum) + tcp_no_sum[18:]
    return eth + ip + tcp + payload


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    body = f"status=ok\nnote={NOTE}\nmessage=uchebnaya-zametka\n".encode("ascii")
    response = (
        b"HTTP/1.1 200 OK\r\n"
        b"Server: ctf-training-lab\r\n"
        b"Content-Type: text/plain; charset=utf-8\r\n"
        + f"Content-Length: {len(body)}\r\n".encode("ascii")
        + b"Connection: close\r\n\r\n"
        + body
    )
    packets = [
        packet(b"GET /note.txt HTTP/1.1\r\nHost: lab.local\r\n\r\n", b"\x0a\x00\x00\x02", b"\x0a\x00\x00\x01", 43110, 80, 1, 1),
        packet(response, b"\x0a\x00\x00\x01", b"\x0a\x00\x00\x02", 80, 43110, 1, 44),
    ]
    global_header = struct.pack("<IHHIIII", 0xA1B2C3D4, 2, 4, 0, 0, 65535, 1)
    now = int(time.mktime((2026, 1, 1, 12, 0, 0, 0, 1, -1)))
    records = []
    for index, frame in enumerate(packets):
        records.append(struct.pack("<IIII", now + index, 0, len(frame), len(frame)) + frame)
    OUT.write_bytes(global_header + b"".join(records))


if __name__ == "__main__":
    main()
