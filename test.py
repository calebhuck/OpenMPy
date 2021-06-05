import sys
sys.path.append('/Users/calebhuck/PycharmProjects/OpenMPy/preprocessor/ompy')
import sys
import jarray
from omp import *
from runtime import *
from Queue import Queue
from threading import current_thread


_num_threads_ = 1
var = 0
_num_threads_ = 8
def _target_0(_manager_):
    global var

    print var
_manager_outer_ = RuntimeManager(_num_threads_)
submit(_target_0, _num_threads_, args=(_manager_outer_,))