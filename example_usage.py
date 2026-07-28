from client import ContextCompressorClient

def main():
    client = ContextCompressorClient()
    res = client.compress_context(messages=['msg1', 'msg2', 'msg3', 'msg4'])
    print(f"Result for compressed_summary: {res['compressed_summary']}")

if __name__ == "__main__":
    main()
