from time import perf_counter

import cursor
from colorama import Fore


class ProgressBar:

    def __init__(self, total: int, text: str = "Progress",
                 width: int = None) -> None:

        self.START = perf_counter()
        self.END = None
        self.TOTAL = total

        self.text = text
        self.width = width if width else 80 - (len(text) + 15)

        self.progress = 1e-12

    def update(self, current: int) -> None:
        """_summary_

        Args:
            current (int): _description_
        """

        self.progress = (current + 1) / (self.TOTAL - 1)  # Quick fix.

        percentage = round(self.progress * 100, 4)
        completed = round(self.progress * self.width)
        remaining = self.width - completed

        # Value boundary adjustments:

        percentage = percentage if percentage <= 100.00 else 100.00

        if self.progress < 0:
            self.progress = 1e-12
        elif self.progress > 1:
            return None

        SYMBOL = '━'
        ICON = '√' if self.progress == 1 else '@'
        COLORS = {
            "text": Fore.GREEN if self.progress == 1 else Fore.RED,
            "progress": Fore.GREEN if self.progress == 1 else Fore.YELLOW,
            "remaining": Fore.BLACK
        }

        # Cursor display:

        if self.progress == 1:
            cursor.show()
        else:
            cursor.hide()

        # Progress bar display:

        elapsed = perf_counter() - self.START

        eta = (elapsed / self.progress) * (1 - self.progress) + 1
        eta_format = f"{str(int(eta // 60)).zfill(2)}:{str(int(eta % 60)).zfill(2)}"
        percentage_format = f"{f'{percentage:.2f}'.rjust(6)} %"

        if self.progress < 1:
            print(
                f" {COLORS.get('text')}{ICON} {COLORS.get('text')}{self.text}"
                f" {COLORS.get('progress')}{SYMBOL * completed}"
                f"{COLORS.get('remaining')}{SYMBOL * remaining}"
                f" {COLORS.get('text')}{f'[{percentage_format}]'}"
                f" {COLORS.get('text')}ETA: {eta_format}",
                end='\r'
            )
        else:
            print(
                f" {COLORS.get('text')}{ICON} {COLORS.get('text')}{self.text}"
                f" {COLORS.get('progress')}{SYMBOL * completed}"
                f"{COLORS.get('remaining')}{SYMBOL * remaining}"
                f" {COLORS.get('text')}{f'[{percentage_format}]'}"
                f" {COLORS.get('text')}Elapsed: {elapsed:.2f}s",
                end='\n'
            )

        self.LAST = perf_counter()


if __name__ == "__main__":
    from time import sleep

    pb = ProgressBar(90, text="Progress")

    for i in range(101):
        pb.update(i)
        sleep(0.1)
