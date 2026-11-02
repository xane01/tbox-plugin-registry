"""Harmless TBOX integration-test plugin."""


def run(args=None):
    print("Hello from the TBOX plugin registry!")
    print("Plugin installation and execution test: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
