import pandas as pd
import numpy as np
import multiprocessing
from multiprocessing import Process


def run_cpu_heavy_function_with_multiprocessing(data):
    num = len(data.index)
    num_of_process = multiprocessing.cpu_count() - 1  # multiprocessing.cpu_count() will give the total cpu numbers=number of logical cores
    chunk_size = num // (num_of_process - 1)  # remember to -1 here because the remainder needs a process to run them

    jobs = []
    manager = multiprocessing.Manager()
    df_res_dict = manager.dict()  # You use a Manager dictionary to communicate with processes/this allows df_res_dict to be passed across processes

    for process_i in range(num_of_process):
        p = Process(target=cpu_heavy_function, args=(data, df_res_dict, process_i, chunk_size, num, num_of_process))
        jobs.append(p)
        p.start()
    for job in jobs:
        job.join() # wait until all processes finished

    df_final = pd.DataFrame(columns=["a"])
    df_final.index.name = "index"

    for process in range(num_of_process):
        df_final = pd.concat(
            [df_final, df_res_dict[process]], axis=0
        )  # concat vertically / by row. combine all results from different processes into one final dataframe
    return df_final


def cpu_heavy_function(data, df_res_dict, process, chunk_size, num, num_of_process):
    """
    make some calculation for each row
    """
    if process == num_of_process - 1:
        index_list = data.index[process * chunk_size :]
    else:
        index_list = data.index[process * chunk_size : (process + 1) * chunk_size]
    df_res = pd.DataFrame(columns=["a"])
    df_res.index.name = "index"
    for index in index_list:
        value = data.loc[index, "a"]
        res = sum(i * i for i in range(abs(int(value))))
        df_res.loc[index, "a"] = res
    df_res_dict[process] = df_res


if __name__ == "__main__":
    df = pd.DataFrame(np.random.randn(1000, 2) * 1000, index=[i for i in range(1000)], columns=["a", "b"])
    df.to_csv("original_dataframe.csv")
    df_output = run_cpu_heavy_function_with_multiprocessing(data=df)
    df_output.to_csv("final_dataframe.csv")
