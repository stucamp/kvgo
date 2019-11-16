import string
from typing import List

import kv_pb2
import kv_pb2_grpc
import grpc
import time
import statistics
import random
import itertools


def measure_unary(grpc_endpoint, request) -> float:
    t0 = time.perf_counter()
    grpc_endpoint(request)
    t1 = time.perf_counter()
    return t1-t0


def get_random_strings(length=10) -> str:
    return ''.join([random.choice(string.ascii_letters) for _ in range(length)])


def make_keyvals(sample_size=10000, key_str='sample_key') -> List[kv_pb2.KeyValue]:
    key = kv_pb2.Key(key=key_str)
    return [kv_pb2.KeyValue(key=key, value=kv_pb2.Value(value=get_random_strings())) for _ in range(sample_size)]


def run_performance() -> List[float]:
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = kv_pb2_grpc.KeyValueStoreStub(channel)
        key_vals = make_keyvals()
        grpc_update_requests = [(stub.Update, kv_pb2.UpdateRequest(keyValue=kv)) for kv in key_vals]
        times = [measure_unary(endpoint, request) for endpoint, request in grpc_update_requests]
    return times


def print_perf_results(times: List[float]) -> None:
    sorted_times = sorted(times, reverse=True)
    longest_5_times = ['{:0.5f}s'.format(time_) for time_ in sorted_times[:5]]
    shortest_5_times = ['{:0.5f}s'.format(time_) for time_ in sorted(sorted_times[-5:])]
    print('Mean time: {:.5f}s'.format(sum(times) / len(times)))
    print('Longest 5 times: {}'.format(longest_5_times))
    print('Shortest 5 times: {}'.format(shortest_5_times))
    print('Std dev: {:.5f}'.format(statistics.pstdev(times)))
    print('Number of requests over 1ms: {}'.format(len(list(itertools.takewhile(lambda x: x > 1e-3, times)))))


if __name__ == '__main__':
    results = run_performance()
    print_perf_results(results)
