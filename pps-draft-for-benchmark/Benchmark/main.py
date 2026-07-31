from .elements.BenchmarkGraph import BenchmarkGraph
from .elements.TimeSpaceGraph4Benchmark import TimeSpaceGraph4Benchmark

if __name__ == "__main__":
    # Đường dẫn file map benchmark
    map_file_path = "Benchmark/benchmark.map" 

    # Khởi tạo BenchmarkGraph và sinh graph từ file map
    benchmark_graph = BenchmarkGraph()
    benchmark_graph.generate_space_graph(map_file_path)
    benchmark_graph.export_space_graph_dimacs_file()

    # Khởi tạo TimeSpaceGraph4Benchmark 
    time_horizon = 5
    time_step = 1
    tsg = TimeSpaceGraph4Benchmark(time_horizon, time_step)

    # Build TSG từ benchmark_graph 
    tsg.build_tsg_4_benchmark(benchmark_graph)

    # Xuất file DIMACS cho TSG
    tsg.export_tsg_dimacs_file()

    print("✅ Đã sinh xong file TSG.txt cho MAPF benchmark MovingAI!")