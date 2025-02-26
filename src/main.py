from src.data_transfer_factory import TransferFactory
from src.transfer import Transfer


def main():
    transfer = TransferFactory()
    src = transfer.src
    dest = transfer.dest

    Transfer(src=src, dest=dest).run()


if __name__ == "__main__":
    main()
