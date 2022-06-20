import argparse
import os
import subprocess
import multiprocessing

import tensorflow as tf
physical_devices = tf.config.experimental.list_physical_devices('GPU')
if len(physical_devices) > 0:
    tf.config.experimental.set_memory_growth(physical_devices[0], True)



from settings.default import (
    QUANDL_TICKERS,
    CPD_QUANDL_OUTPUT_FOLDER,
    CPD_DEFAULT_LBW,
)

def main(lookback_window_length: int):
    if not os.path.exists(CPD_QUANDL_OUTPUT_FOLDER(lookback_window_length)):
        os.mkdir(CPD_QUANDL_OUTPUT_FOLDER(lookback_window_length))

    for i in range(0, len(QUANDL_TICKERS), 2):
        
        new_tickers = QUANDL_TICKERS[i:i+2]
        processes=[]
    
        for ticker in new_tickers:

        #ticker = QUANDL_TICKERS[0]
            command = ["python", "-m", "examples.cpd_quandl" , f'{ticker}', f'{os.path.join(CPD_QUANDL_OUTPUT_FOLDER(lookback_window_length), ticker + ".csv")}',  "1990-01-01" ,"2021-12-31", f"{lookback_window_length}"]
            process = subprocess.Popen(command)
            processes.append(process)
        for process in processes:
            process.wait()
    




if __name__ == "__main__":

    def get_args():
        """Returns settings from command line."""

        parser = argparse.ArgumentParser(
            description="Run changepoint detection module for all tickers"
        )
        parser.add_argument(
            "lookback_window_length",
            metavar="l",
            type=int,
            nargs="?",
            default=CPD_DEFAULT_LBW,
            help="CPD lookback window length",
        )
        return [
            parser.parse_known_args()[0].lookback_window_length,
        ]

    main(*get_args())