"""
zadanie:
graf skierowany
mówimy że jakiś wierzchołek, jest dobrym początkiem, jeśli z niego są osiągalne wszystkie
musimy znależć, jeśli jest,
pomysł:
szukamy silnie spójnych składowych
sortujemy je topologicznie - bierzemy pierwszą silnie spójną składową
sprawdzamy czy damy radę przejść ścieżką
implementacja:
żeby złożyć kilka wierzchołków w jeden reprezentujący silnie spójną składową
"""