import pstats
from pstats import SortKey

p = pstats.Stats('profiling_results')

p.sort_stats(SortKey.TIME).print_stats(20)

