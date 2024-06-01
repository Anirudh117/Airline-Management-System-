if(vertex is not s):
            T[vertex] = float("inf")

    # Priority Queue, q, of vertices keyed by T
    q = queue.PriorityQueue()
    for vertex in G.vertices:
        q.put(Schedule(vertex, T[vertex]))

    while not q.empty():
        v = q.get()

        for adjacentVertex in v.vertex.adjacentVertices:
            if Schedule(adjacentVertex, T[adjacentVertex]) in q.queue:

                p = queue.PriorityQueue()
                for flight in F:
                    if(flight.origin == v.vertex and 
                    flight.dest == adjacentVertex):
                        if(flight.departT >= T[v.vertex]):
                            p.put(flight)

                t = float("inf")

                if not p.empty():
                    t = p.queue[0].arrivalT

                # relaxation
                if t < T[adjacentVertex]:
                    T[adjacentVertex] = t
                    q.put(Schedule(adjacentVertex, t))

            else:
                break
    
    earliestTime = T[d]
    
    return earliestTime
