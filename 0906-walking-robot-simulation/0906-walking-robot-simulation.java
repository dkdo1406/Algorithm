class Solution {
    public int robotSim(int[] commands, int[][] obstacles) {
        int[] robot = new int[2];
        int[] dr = {1, 0, -1, 0};
        int[] dc = {0, 1, 0, -1};
        int dir = 0;
        int res = 0;
        Set<Point> block = new HashSet<Point>();
        for (int[] obstacle : obstacles) {
            block.add(new Point(obstacle[1], obstacle[0]));
        }
        for (int command : commands) {
            if (command == -1) {
                dir = (dir + 1) % 4;
            } else if (command == -2) {
                dir = (4 + dir - 1) % 4;
            } else {
                // command값만큼 이동
                for (int idx = 0; idx < command; idx++) {
                    robot[0] += dr[dir];
                    robot[1] += dc[dir];
                    if (block.contains(new Point(robot[0], robot[1]))) {
                        // 중복이 있다면 뒤로 돌아간다.
                        robot[0] -= dr[dir];
                        robot[1] -= dc[dir];
                        break;
                    }
                }
                res = Math.max(res, robot[0] * robot[0] + robot[1] * robot[1]);
            }
        }
        
        return res;
    }
    public class Point {
        private final int r;
        private final int c;

        public Point(int r, int c) {
            this.r = r;
            this.c = c;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (!(o instanceof Point)) return false;
            Point point = (Point)o;
            return r == point.r && Objects.equals(c, point.c);
        }

        @Override
        public int hashCode() {
            return Objects.hash(r, c);
        }
    }
}