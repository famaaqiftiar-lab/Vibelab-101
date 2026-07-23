#!/usr/bin/env python3
"""Menjalankan VibeLab 101 menggunakan pustaka standar Python."""

from __future__ import annotations

import argparse
import functools
import http.server
import pathlib
import socketserver
import threading
import webbrowser


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Jalankan VibeLab 101 di browser.")
    parser.add_argument("--port", type=int, default=8000, help="Port lokal (default: 8000)")
    parser.add_argument(
        "--no-browser",
        action="store_true",
        help="Jangan membuka browser secara otomatis.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    site_directory = pathlib.Path(__file__).resolve().parent
    handler = functools.partial(
        http.server.SimpleHTTPRequestHandler,
        directory=str(site_directory),
    )

    with socketserver.ThreadingTCPServer(("127.0.0.1", args.port), handler) as server:
        server.allow_reuse_address = True
        url = f"http://127.0.0.1:{args.port}/"
        print(f"VibeLab 101 berjalan di {url}")
        print("Tekan Ctrl+C untuk menghentikan.")
        if not args.no_browser:
            threading.Timer(0.4, webbrowser.open, args=(url,)).start()
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nServer dihentikan.")


if __name__ == "__main__":
    main()
