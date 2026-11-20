#!/usr/bin/env python3
"""Refresh and update Five-Member Council through its host's plugin manager."""

import argparse
import json
import subprocess
import sys

MARKETPLACE = "five-member-council"
PLUGIN = f"five-member-council@{MARKETPLACE}"


def run_json(*command):
    result = subprocess.run(command, check=True, stdout=subprocess.PIPE, text=True)
    return json.loads(result.stdout)


def update_claude():
    installed = run_json("claude", "plugin", "list", "--json")
    if not any(entry.get("id") == PLUGIN for entry in installed):
        raise ValueError("Five-Member Council is not installed in Claude Code.")

    subprocess.run(["claude", "plugin", "marketplace", "update", MARKETPLACE], check=True)
    subprocess.run(["claude", "plugin", "update", PLUGIN], check=True)
    print("Run /reload-plugins in Claude Code or start a new session to apply the update.")


def update_codex():
    installed = run_json("codex", "plugin", "list", "--marketplace", MARKETPLACE, "--json")
    if not any(entry.get("pluginId") == PLUGIN for entry in installed["installed"]):
        raise ValueError("Five-Member Council is not installed in Codex.")

    refresh = run_json("codex", "plugin", "marketplace", "upgrade", MARKETPLACE, "--json")
    if refresh.get("errors"):
        raise ValueError(f"Codex could not refresh the marketplace: {refresh['errors']}")

    result = run_json("codex", "plugin", "add", PLUGIN, "--json")
    print(f"Five-Member Council {result['version']} is installed. Start a new Codex session to load it.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("client", choices=("claude", "codex"), help="The CLI where the plugin is installed.")
    client = parser.parse_args().client

    try:
        if client == "claude":
            update_claude()
        else:
            update_codex()
    except FileNotFoundError:
        print(f"{client} was not found on PATH. Run the update where the plugin is installed.", file=sys.stderr)
        return 1
    except (subprocess.CalledProcessError, KeyError, ValueError) as error:
        print(f"Council update stopped: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
