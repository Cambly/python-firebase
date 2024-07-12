import atexit

from ._async import process_pool, _process_pool
from .firebase import *


@atexit.register
def close_process_pool():
    """
    Clean up function that closes and terminates the process pool
    defined in the ``async`` file.
    """
    # if the pool doesn't already exist, don't create it just to stop it.
    if _process_pool is not None:
        process_pool.close()
        process_pool.join()
        process_pool.terminate()
