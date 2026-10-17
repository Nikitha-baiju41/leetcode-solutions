import java.util.*;

class RecentCounter {
    private Queue<Integer> requests = new LinkedList<>();

    public RecentCounter() {
    }

    public int ping(int t) {
        requests.offer(t);

        while (requests.peek() < t - 3000) {
            requests.poll();
        }

        return requests.size();
    }
}
