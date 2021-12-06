import java.io.*;
import java.util.*;
import static java.lang.Math.max;

public class dijkstra {
    private static InputReader in;
    private static PrintWriter out;

    public static void main(String[] args) throws IOException {
        InputStream inputStream = System.in;
        in = new InputReader(inputStream);
        OutputStream outputStream = System.out;
        out = new PrintWriter(outputStream);

        int N = in.nextInt();
        Graph BSD = new Graph(N);

        String node; String hInput;
        for (int n = 0; n < N; n++) {
            node = in.next();
            hInput = in.next();

            if (hInput.equals("hospital")) BSD.addNode(node, true);
            else BSD.addNode(node, false);
        }

        int E = in.nextInt();

        String N1; String N2; int w;
        for (int e = 0; e < E; e++) {
            N1 = in.next();
            N2 = in.next();
            w = in.nextInt();

            BSD.addEdge(N1, N2, w);
        }

        String x = "21";
        String dijkstra = BSD.dijkstraNearestHospital(x);

        out.println(dijkstra);
        out.close();
    }

    static class InputReader {
        public BufferedReader reader;
        public StringTokenizer tokenizer;
 
        public InputReader(InputStream stream) {
            reader = new BufferedReader(new InputStreamReader(stream), 32768);
            tokenizer = null;
        }
 
        public String next() {
            while (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    tokenizer = new StringTokenizer(reader.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return tokenizer.nextToken();
        }
 
        public int nextInt() {
            return Integer.parseInt(next());
        }
 
    }
}

class Graph {
    int vertices;
    HashMap<String, Node> nodes;
    HashMap<String[], Edge> edges;

    // for dijkstra implementation
    PriorityQueue<Path> pq; 
    PriorityQueue<Node> hospitals;

    Graph(int vertices) {
        this.vertices = vertices;
        nodes = new HashMap<>();
        edges = new HashMap<>();
    }

    public void addNode(String name, Boolean isHospital) {
        Node node = new Node(name, isHospital);
        nodes.put(name, node);
    }

    public void addEdge(String n1, String n2, int w) {
        Node N1; Node N2; 
        String[] fromto = new String[2];
        if (nodes.containsKey(n1) && nodes.containsKey(n2)) {
            N1 = nodes.get(n1); N2 = nodes.get(n2);

            Edge edge1 = new Edge(N1, N2, w);
            fromto[0] = n1; fromto[1] = n2;
            edges.put(fromto, edge1);
            N1.addEdge(edge1);

            Edge edge2 = new Edge(N2, N1, w);
            fromto[0] = n2; fromto[1] = n1;
            edges.put(fromto, edge2);
            N2.addEdge(edge2);
        }
    }

    private void clearAll() {
        for (String N : nodes.keySet()) {
            nodes.get(N).reset();
        }
    }

    private void dijkstra(Node src) {
        pq = new PriorityQueue<Path>();
        hospitals = new PriorityQueue<Node>();
        clearAll();

        pq.add(new Path(src, 0));
        src.cost = 0;

        int c;
        while (!(pq.isEmpty())) {
            Path p = pq.remove();
            Node n1 = p.dest;

            for (Edge e : n1.edges.keySet()) {
                Node n2 = e.des;
                int w = e.weight;

                c = n1.cost + w;

                if (n2.cost > c) {
                    n2.cost = c;
                    n2.prev = n1;

                    pq.add(new Path(n2, n2.cost));
                }
            }
        }
    }

    public String dijkstraNearestHospital(String N) {
        Node node; int cost = 0; String res = "Dijkstra: ";
        if (nodes.containsKey(N)) {
            node = nodes.get(N);

            dijkstra(node);

            for (String n : nodes.keySet()) {
                node = nodes.get(n);
                if (node.isHospital) hospitals.add(node);
            }

            node = hospitals.remove();
            cost = node.cost;
            res = res + node.name;
        }

        
        res = res + " ";
        res = res + cost;

        return res;
    }

}

class Path implements Comparable<Path> {
    public Node dest;  // w
    public int cost;   // d(w)

    public Path(Node des, int c) {
        this.dest = des;
        this.cost = c;
    }

    public int compareTo(Path p) {
        int other = p.cost;
        return this.cost < other ? -1 : this.cost > other ? 1 : 0;
    }
}

class Node implements Comparable<Node> {
    public String name;
    public Boolean isHospital;
    public HashMap<Edge, Integer> edges;
    // dijkstra
    public Node prev;
    public int cost;
    public HashMap<Path, Integer> paths;

    public Node(String name, Boolean isHospital) {
        this.name = name;
        this.isHospital = isHospital;
        edges = new HashMap<>();

        this.prev = null;
        this.cost = Integer.MAX_VALUE;
    }

    public void reset() {
        this.prev = null;
        this.cost = Integer.MAX_VALUE;
    }

    public void addEdge(Edge edge) {
        edges.put(edge, edge.weight);
    }

    public int compareTo(Node n) {
        int other = n.cost;
        return this.cost < other ? -1 : this.cost > other ? 1 : 0;
    }

}

class Edge {
    public Node src;
    public Node des;
    public int weight;

    public Edge(Node src, Node des, int weight) {
        this.src = src;
        this.des = des;
        this.weight = weight;
    }
}
