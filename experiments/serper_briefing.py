#!/usr/bin/env python3
"""Quick Serper.dev briefing helper for AI-agent news.

Usage:
    SERPER_API_KEY=xxx python3 experiments/serper_briefing.py "AI agents for enterprise"
"""
from __future__ import annotations

import os
import sys
from textwrap import shorten

import requests

API_KEY = os.getenv("SERPER_API_KEY")
BASE_URL = "https://google.serper.dev/search"
DEFAULT_QUERY = "AI agents enterprise automation"


def fetch(query: str, num: int = 5) -> dict:
    if not API_KEY:
        raise SystemExit("SERPER_API_KEY env var not set")
    resp = requests.post(
        BASE_URL,
        headers={"X-API-KEY": API_KEY, "Content-Type": "application/json"},
        json={"q": query, "num": num},
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()


def format_results(data: dict) -> str:
    organic = data.get("organic", [])
    lines = []
    for idx, item in enumerate(organic, start=1):
        title = item.get("title", "(sin título)")
        link = item.get("link", "")
        snippet = shorten(item.get("snippet", ""), width=200)
        lines.append(f"{idx}. {title}\n   {link}\n   {snippet}\n")
    return "\n".join(lines) if lines else "(Sin resultados)"


def main():
    query = " ".join(sys.argv[1:]).strip() or DEFAULT_QUERY
    data = fetch(query)
    print(f"Resultados para: {query}\n")
    print(format_results(data))


if __name__ == "__main__":
    main()
